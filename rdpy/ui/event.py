from PyQt4 import QtGui

from PyQt4.QtGui import QTextCursor

from rdpy.core import rss, log
from rdpy.core.scancode import scancodeToChar
from rdpy.enum.rdp import RDPPlayerMessageType, CapabilityType
from rdpy.pdu.rdp.fastpath import FastPathEventScanCode, FastPathEventMouse, FastPathOrdersEvent, FastPathBitmapEvent
from rdpy.ui.qt4 import RDPBitmapToQtImage


class RSSEventHandler:
    def __init__(self, viewer, text):
        self._viewer = viewer
        self._text = text
        self._write_in_caps = False
    
    def on_event_received(self, event):
        if event.type.value == rss.EventType.UPDATE:
            image = RDPBitmapToQtImage(event.event.width.value, event.event.height.value, event.event.bpp.value, event.event.format.value == rss.UpdateFormat.BMP, event.event.data.value);
            self._viewer.notifyImage(event.event.destLeft.value, event.event.destTop.value, image, event.event.destRight.value - event.event.destLeft.value + 1, event.event.destBottom.value - event.event.destTop.value + 1)

        elif event.type.value == rss.EventType.SCREEN:
            self._viewer.resize(event.event.width.value, event.event.height.value)

        elif event.type.value == rss.EventType.INFO:
            format_args = (event.event.domain.value, event.event.username.value, event.event.password.value, event.event.hostname.value)
            message = "Domain : %s\nUsername : %s\nPassword : %s\nHostname : %s\n" % format_args
            message = message.replace("\x00", "")
            self._text.append(message)
        elif event.type.value == rss.EventType.KEY_SCANCODE:
            code = event.event.code.value
            is_pressed = not event.event.isPressed.value
            if code in [0x2A, 0x36]:
                self._text.insertPlainText("\n<LSHIFT PRESSED>" if is_pressed else "\n<LSHIFT RELEASED>")
                self._write_in_caps = not self._write_in_caps
                self._text.moveCursor(QTextCursor.End)
            elif code == 0x3A and is_pressed:
                self._text.insertPlainText("\n<CAPSLOCK>")
                self._write_in_caps = not self._write_in_caps
                self._text.moveCursor(QTextCursor.End)
            elif is_pressed:
                char = scancodeToChar(code)
                self._text.insertPlainText(char if self._write_in_caps else char.lower())
                self._text.moveCursor(QtGui.QTextCursor.End)
        elif event.type.value == rss.EventType.CLOSE:
            self._text.insertPlainText("\n<Connection closed>")
            self._text.moveCursor(QtGui.QTextCursor.End)


class NewRSSEventHandler:
    """
    Class to manage the display of the RDP player when reading events.
    """

    def __init__(self, viewer, text):
        self._viewer = viewer
        self._text = text
        self._write_in_caps = False

    def on_message_received(self, message):
        """
        For each event in the provided message, handle it, if it can be handled.
        :type message: rdpy.pdu.rdp.recording.RDPPlayerMessagePDU
        """
        if message.type == RDPPlayerMessageType.INPUT:
            self.handle_input_event(message.payload)
        elif message.type == RDPPlayerMessageType.OUTPUT:
            self.handle_output_event(message.payload)
        elif message.type == RDPPlayerMessageType.CLIENT_INFO:
            self.handle_client_info(message.payload)
        elif message.type == RDPPlayerMessageType.CONFIRM_ACTIVE:
            self.handle_resize(message.payload)
        else:
            log.error("Received wrong player message type: {}".format(message.type))

    def handle_output_event(self, payload):
        for event in payload.events:
            if isinstance(event, FastPathOrdersEvent):
                log.debug("Not handling orders event, not coded :)")
            elif isinstance(event, FastPathBitmapEvent):
                log.debug("Handling bitmap event {}".format(event))
                self.handle_image(event)
            else:
                log.debug("Cant handle output event: {}".format(event))

    def handle_input_event(self, payload):
        for event in payload.events:
            if isinstance(event, FastPathEventScanCode):
                log.debug("handling {}".format(event))
                self.handle_scancode(event)
            elif isinstance(event, FastPathEventMouse):
                log.debug("Not handling Mouse event since it has not yet been coded :)")
            else:
                log.debug("Cant handle input event: {}".format(event))

    def handle_scancode(self, event):
        log.debug("Reading scancode {}".format(event.scancode))
        code = event.scancode
        is_pressed = not event.isReleased
        if code in [0x2A, 0x36]:
            self._text.moveCursor(QTextCursor.End)
            self._text.insertPlainText("\n<LSHIFT PRESSED>" if is_pressed else "\n<LSHIFT RELEASED>")
            self._write_in_caps = not self._write_in_caps
        elif code == 0x3A and is_pressed:
            self._text.moveCursor(QTextCursor.End)
            self._text.insertPlainText("\n<CAPSLOCK>")
            self._write_in_caps = not self._write_in_caps
        elif is_pressed:
            char = scancodeToChar(code)
            self._text.moveCursor(QtGui.QTextCursor.End)
            self._text.insertPlainText(char if self._write_in_caps else char.lower())

    def handle_image(self, event):
        """
        :type event: rdpy.pdu.rdp.fastpath.FastPathBitmapEvent
        """
        for bitmapData in event.bitmapUpdateData:
            image = RDPBitmapToQtImage(bitmapData.width, bitmapData.heigth, bitmapData.bitsPerPixel,
                                       True, bitmapData.bitmapStream)
            self._viewer.notifyImage(bitmapData.destLeft, bitmapData.destTop, image,
                                     bitmapData.destRight - bitmapData.destLeft + 1,
                                     bitmapData.destBottom - bitmapData.destTop + 1)
        pass

    def handle_client_info(self, pdu):
        """
        :type pdu: rdpy.pdu.rdp.client_info.RDPClientInfoPDU
        """
        self._text.insertPlainText("--------------------")
        self._text.insertPlainText("\nUSERNAME: {}\nPASSWORD: {}\nDOMAIN: {}\n"
                          .format(pdu.username.replace("\0", ""),
                                  pdu.password.replace("\0", ""),
                                  pdu.domain.replace("\0", "")))
        self._text.insertPlainText("--------------------\n")

    def handle_resize(self, pdu):
        """
        :type pdu: rdpy.pdu.rdp.data.RDPConfirmActivePDU
        """
        self._viewer.resize(pdu.parsedCapabilitySets[CapabilityType.CAPSTYPE_BITMAP].desktopWidth,
                            pdu.parsedCapabilitySets[CapabilityType.CAPSTYPE_BITMAP].desktopHeight)