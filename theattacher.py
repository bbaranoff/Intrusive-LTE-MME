from os import wait
import socket
import time
import sctp
sctp_socket = sctp.sctpsocket_tcp(socket.AF_INET);
sctp_socket.connect(("127.0.0.42",36412))
#0011002d000004003b00080000f110000019b0003c400a0380737273656e62303100400007000001c000f1100089400140
#real S1 setup request from srsenb
sctp_socket.sctp_send(bytes.fromhex("0011002d000004003b00080000f110000019b0003c400a0380737273656e62303100400007000001c000f1100089400140"), ppid=socket.htonl(18))
fromaddr, flags, msgret, notif = sctp_socket.sctp_recv(2048)
assert msgret.hex() == "201140170000020069000b000000f11000000100001a00574001ff"
#real S1 setup response
#sctp_socket.sctp_send(bytes.fromhex("20110025000003003d400a03807372736d6d6530310069000b000000f11000000100001a00574001ff"), ppid=socket.htonl(18))
# 20110025000003003d400a03807372736d6d6530310069000b000000f11000000100001a00574001ff
#my own crafted S1 setup response
#201140170000020069000b000000f11000000100001a00574001ff
#sctp_socket.sctp_send(bytes.fromhex("201140170000020069000b000000f11000000100001a00574001ff"), ppid=socket.htonl(18))
#sctp_socket.sctp_send(bytes.fromhex("000c40809f000005000800020001001a00777617c0c8102d0b0741020bf61300148001010000000105e060c0401900240204d011d1271d8080211001000010810600000000830600000000000d00000a000010005213001400015c0a003103e5e03e13130014000111035758a6200b6014046f65230200243c2040080402600000021f005d0103e0c10043000600134001000100644008001340011a2d00100086400130"), ppid=socket.htonl(18))

time.sleep(0.1)
#initialUEMEssage, Attach Request, PDN connectivity request
#fromaddr, flags, msgret, notif = sctp_socket.sctp_recv(2048)
#000c4079000005000800020001001a00515007417208291330002132916305f070c04018002a0241d011d127238080211001000010810600000000830600000000000d00000a000005000010000011005c0a01310365e0349011035758a65d0102c1004300060000f1100007006440080000f1100019b0100086400130
sctp_socket.sctp_send(bytes.fromhex("000c4079000005000800020001001a00515007417208291330002132916305f070c04018002a0241d011d127238080211001000010810600000000830600000000000d00000a000005000010000011005c0a01310365e0349011035758a65d0102c1004300060000f1100007006440080000f1100019b0100086400130"), ppid=socket.htonl(18))
fromaddr, flags, msgret, notif = sctp_socket.sctp_recv(2048)


#identity response
#000d401f000003000000020001000800020001001a000c0b0756082980011032547698
#sctp_socket.sctp_send(bytes.fromhex("000d401f000003000000020001000800020001001a000c0b0756082980011032547698"), ppid=socket.htonl(18))
while (True):
    fromaddr, flags, msgret, notif = sctp_socket.sctp_recv(2048)

#sctp_socket.sctp_send(bytes.fromhex("0017001000000200630004000100010002400120"), ppid=socket.htonl(18))

print("exitus")

#sent original
#07417208291330002132916305f070c04018002a0241d011d127238080211001000010810600000000830600000000000d00000a000005000010000011005c0a01310365e0349011035758a65d0102c1
#sent back
#07417208291330002132916305f070c04018002a0241d011d127238080211001000010810600000000830600000000000d00000a000005000010000011005c0a01310365e0349011035758a65d0102c1
#a message with Cause
#sctp_socket.sctp_send(bytes.fromhex("0017001000000200630004000100010002400120"), ppid=socket.htonl(18))
#0017001000000200630004000100010002400120


