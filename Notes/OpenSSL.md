# OpenSSL
## Compliation
```bash
$ ./config enable-weak-ssl-ciphers
$ make
$ sudo make install
```

## Run
```
$ LD_LIBRARY_PATH=/usr/local/lib64 /usr/local/bin/openssl version -a
OpenSSL 3.0.5 5 Jul 2022 (Library: OpenSSL 3.0.5 5 Jul 2022)
built on: Fri Oct 28 14:59:28 2022 UTC
platform: linux-x86_64
options:  bn(64,64)
compiler: gcc -fPIC -pthread -m64 -Wa,--noexecstack -Wall -O3 -enable-weak-ssl-ciphers -DOPENSSL_USE_NODELETE -DL_ENDIAN -DOPENSSL_PIC -DOPENSSL_BUILDING_OPENSSL -DNDEBUG
OPENSSLDIR: "/usr/local/ssl"
ENGINESDIR: "/usr/local/lib64/engines-3"
MODULESDIR: "/usr/local/lib64/ossl-modules"
Seeding source: os-specific
CPUINFO: OPENSSL_ia32cap=0xfffab2234f8bffff:0x4009c47ab
$ LD_LIBRARY_PATH=/usr/local/lib64 /usr/local/bin/openssl ciphers | grep -Eo '[^:]*RC4[^:]*' | sort
ADH-RC4-MD5
AECDH-RC4-SHA
DHE-PSK-RC4-SHA
ECDHE-ECDSA-RC4-SHA
ECDHE-PSK-RC4-SHA
ECDHE-RSA-RC4-SHA
PSK-RC4-SHA
RC4-MD5
RC4-SHA
RSA-PSK-RC4-SHA
```