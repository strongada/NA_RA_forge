from scapy.all import sendp,Ether,IPv6,ICMPv6ND_RA,ICMPv6NDOptPrefixInfo,ICMPv6NDOptSrcLLAddr
print("start")
sendp(Ether(src="5e:6c:c9:a5:6a:4e") \
        /IPv6(src="fe80::5c6c:c9ff:fea5:6a4e",dst="fe80::227c:8fff:fe79:2580") \
        /ICMPv6ND_RA(prf=0,routerlifetime=1800) \
        /ICMPv6NDOptPrefixInfo(prefix="2222:db8:1::",prefixlen=64,preferredlifetime=14400,validlifetime=86400) \
        /ICMPv6NDOptSrcLLAddr(lladdr="5e:6c:c9:a5:6a:4e"),loop=-1, inter=1, iface="br0")

