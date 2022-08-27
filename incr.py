import socket
s = socket.socket()
s.connect(("ad.samsclass.info", 10203))
print(s.recv(1024).decode())
num = input("What to send the server ?")
print (num)
s.send(num.encode())
print(s.recv(1024).decode())
s.close()