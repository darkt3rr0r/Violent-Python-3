import socket,time,sys
s = socket.socket()
s.connect(("ad.samsclass.info", 10204))


try:
	
	for i in range (5):

		x=s.recv(1024).decode()
		print(x)
		res = [int(i) for i in x.split() if i.isdigit()]
		print (res)


		if  "Add" in x :

			print("Adding....")
			add_res = str(res[0] + res[1])+"\n"
			print (str(add_res))
			print("Sending....")
			s.send(add_res.encode())
			print(s.recv(1024).decode())
			time.sleep(0.5)
		

		else:

			print("Subtracting....")
			sub_res = str(res[0] - res[1])+"\n"
			print (str(sub_res))
			print("Sending....")
			s.send(sub_res.encode())
			print(s.recv(1024).decode())
			time.sleep(0.5)

except:
	print("Finished")
	sys.exit(1)
s.close()
