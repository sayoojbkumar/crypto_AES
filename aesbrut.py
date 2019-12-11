from Crypto.Cipher import AES
key="YELLOW SUBMARINE"
pt=raw_input("message:")
z=len(pt)
secret="hellowwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"
def encryption(pt):
	global key
	pt=pt+secret
	pt=pt+chr(pad(pt))*pad(pt)
	cipher=AES.new(key,AES.MODE_ECB)
	ct=cipher.encrypt(pt)
        ct=ct.encode("hex")
	return ct
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
def exploitlength():
	length=0
	for i in range (1,17):
		pt="a"*i
		if len(encryption(pt))!=32:
			q=i
			break
	length=16-q
	print"length of secret="
	print length
	return length

def findsecret():
	appending=""
	for j in range(15,0,-1):
		pt="a"*j	
		test=encryption(pt)		
                for k in range(128):
			vt="a"*j+appending+chr(k)
			changingtest=encryption(vt)
			if changingtest[0:16]==test[0:16]:
				appending+=(chr(k))	
	        		print appending
				break
			


			
		

encryption(pt)
ct=raw_input()
decrypt(ct)
exploitlength()
findsecret()

