# Protocol analysis
## Connection Sequence
https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rdpbcgr/023f1e69-cfe8-4ee6-9ee0-7e759fb4e4ee?redirectedfrom=MSDN
![[Pasted image 20221028185822.png]]

## Client X.224 Connection Request PDU
- [Documentation](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rdpbcgr/18a27ef9-6f9a-4501-b000-94b1fe3c2c10) / [Annotated dump](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rdpbcgr/e78db616-689f-4b8a-8a99-525f7a433ee2?redirectedfrom=MSDN)
- [RDP Negotiation Request (RDP_NEG_REQ)](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rdpbcgr/902b090b-9cb3-4efc-92bf-ee13373371e3)
```
Listening for new connection
Connection received from 192.168.1.137:50188
From client:
00000000: 03 00 00 2F 2A E0 00 00  00 00 00 43 6F 6F 6B 69  .../*......Cooki
00000010: 65 3A 20 6D 73 74 73 68  61 73 68 3D 50 59 52 44  e: mstshash=PYRD
00000020: 50 2D 43 4C 49 0D 0A 01  00 08 00 0B 00 00 00     P-CLI..........

tpktHeader: 4 bytes
  03: version 3
  00: reserved
  00 2f: packet length (high low): 47
x.224Crq: 7 bytes
  2a: length (42)
  e0: 
  00 00: dst ref
  00 00: src ref
  00: class and options
routingToken:
  43 6F 6F 6B 69 65 3A 20 6D 73 74 73 68 61 73 68 3D 50 59 52 44 50 2D 43 4C 49: Cookie: PYRDP-CLI
  0d 0a: termination
rdpNegReq (8 bytes):
  01: type always 01
  00: flags (RESTRICTED_ADMIN_MODE_REQUIRED, REDIRECTED_AUTHENTICATION_MODE_REQUIRED, CORRELATION_INFO_PRESENT are possible)
  08 00: length always 08 00
  0B 00 00 00: requestedProtocols
```