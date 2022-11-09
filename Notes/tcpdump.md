```bash
sudo tcpdump -i eth0 -w - -U host 192.168.1.136 and host 192.168.1.137 and not arp | tee rdp_$(hostname)_$(date +%Y%m%d-%H%M%S).pcapng | tcpdump -r -
```
