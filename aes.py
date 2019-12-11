from Crypto.Cipher import AES
key="YELLOW SUBMARINE"
pt=raw_input("message:")
z=len(pt)
def encryption(pt):
	global key
	print pt
	pt=pt+chr(pad(pt))*pad(pt)
	cipher=AES.new(key,AES.MODE_ECB)
	ct=cipher.encrypt(pt)
        print ct.encode("hex")
def decrypt(ct):
	global key
	ct=ct.decode("hex")
	cipher=AES.new(key,AES.MODE_ECB)
	pt=cipher.decrypt(ct)
	pt=pt[0:z]
	print pt
def pad(pt):
	if len(pt)%16==0:
		padding=16
		return padding
	elif len(pt)%16>0:
		padding=16-(len(pt)%16)
		return padding
	
		

encryption(pt)
ct=raw_input()
decrypt(ct)


