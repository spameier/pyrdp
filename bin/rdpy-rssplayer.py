#!/usr/bin/python
#
# Copyright (c) 2014-2015 Sylvain Peyrefitte
#
# This file is part of rdpy.
#
# rdpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
"""
rss file player
"""
import argparse
import logging
import sys, os, getopt, socket

from PyQt4 import QtGui, QtCore

from rdpy.core import log, rss
from rdpy.ui.qt4 import QRemoteDesktop, RDPBitmapToQtImage
from rdpy.core.scancode import scancodeToChar
from rdpy.ui.event import RSSEventHandler

# Sets the log level for the RDPY library ("rdpy").
log.get_logger().setLevel(logging.INFO)

class RssPlayerWidget(QRemoteDesktop):
    """
    @summary: special rss player widget
    """
    def __init__(self, width, height):
        class RssAdaptor(object):
            def sendMouseEvent(self, e, isPressed):
                """ Not Handle """
            def sendKeyEvent(self, e, isPressed):
                """ Not Handle """
            def sendWheelEvent(self, e):
                """ Not Handle """
            def closeEvent(self, e):
                """ Not Handle """
        QRemoteDesktop.__init__(self, width, height, RssAdaptor())
        
class RssPlayerWindow(QtGui.QWidget):
    """
    @summary: main window of rss player
    """
    def __init__(self):
        super(RssPlayerWindow, self).__init__()
        
        self._viewer = RssPlayerWidget(800, 600)
        self._text = QtGui.QTextEdit()
        self._text.setReadOnly(True)
        self._text.setFixedHeight(150)

        scrollViewer = QtGui.QScrollArea()
        scrollViewer.setWidget(self._viewer)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(scrollViewer, 1)
        layout.addWidget(self._text, 2)
        
        self.setLayout(layout)
        self.setGeometry(0, 0, 800, 600)

def start(widget, rssFile):
    loop(widget, rssFile, rssFile.nextEvent())
  
def loop(widget, rssFile, nextEvent):
    """
    @summary: timer function
    @param widget: {QRemoteDesktop}
    @param rssFile: {rss.FileReader}
    """
   
    if nextEvent.type.value == rss.EventType.UPDATE:
        image = RDPBitmapToQtImage(nextEvent.event.width.value, nextEvent.event.height.value, nextEvent.event.bpp.value, nextEvent.event.format.value == rss.UpdateFormat.BMP, nextEvent.event.data.value);
        widget._viewer.notifyImage(nextEvent.event.destLeft.value, nextEvent.event.destTop.value, image, nextEvent.event.destRight.value - nextEvent.event.destLeft.value + 1, nextEvent.event.destBottom.value - nextEvent.event.destTop.value + 1)
        
    elif nextEvent.type.value == rss.EventType.SCREEN:
        widget._viewer.resize(nextEvent.event.width.value, nextEvent.event.height.value)
        
    elif nextEvent.type.value == rss.EventType.INFO:
        widget._text.append("Domain : %s\nUsername : %s\nPassword : %s\nHostname : %s\n" % (
                            nextEvent.event.domain.value, nextEvent.event.username.value, nextEvent.event.password.value, nextEvent.event.hostname.value))
    elif nextEvent.type.value == rss.EventType.KEY_SCANCODE:
        if nextEvent.event.isPressed.value == 0:
            widget._text.moveCursor(QtGui.QTextCursor.End)
            widget._text.insertPlainText(scancodeToChar(nextEvent.event.code.value))
        
    elif nextEvent.type.value == rss.EventType.CLOSE:
        return
    
    e = rssFile.nextEvent()
    QtCore.QTimer.singleShot(e.timestamp.value,lambda:loop(widget, rssFile, e))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("rss_file")
    args = parser.parse_args()
    file_path = args.rss_file

    # Create application
    app = QtGui.QApplication(sys.argv)
    mainWindow = RssPlayerWindow()
    mainWindow.show()
    
    rssFile = rss.createFileReader(file_path)
    start(mainWindow, rssFile)
    sys.exit(app.exec_())