import sys
import random
import hashlib
import os

choice = 5

def hash(inp):
	a = hashlib.md5()
	a.update(inp.encode('utf-8'))
	hazh = a.hexdigest()
	
	cache = []
	for i in range(26**4):
		if i % 1000 == 0:
			if os.system('cls'):
				os.system('clear')
			sys.stdout.write("#>")
			for asdf in range(int(round(i/26**4,2)*10)):
				sys.stdout.write('*')
			print('<#')
			print("Working.. :")
		
		b = hashlib.md5()
		rand = ''
		for co in range(20):
			rand = rand + chr(random.randint(0,127))
		b.update(str(rand).encode('utf-8'))
		e = b.hexdigest()
		cache.append(e)
	l = len(cache)
	place = random.randint(0,l-1)
	cache[place] = hazh
	print("Writing to new user passwd-file...")
	return cache

def passfi(user, cache):
	finame = "passwd-" + user
	fi = open(finame, "w")
	fi.close()
	
	stri = ''
	for t in cache:
		stri = stri + t + ":"
		if len(stri) == 676*33:
			fi = open(finame, "a")
			fi.write(stri)
			fi.close()
			stri = ''

def auth():
	user = input("Username: ")
	guess = input("Password: ")
	h = hashlib.md5()
	h.update(guess.encode('utf-8'))
	hazh = h.hexdigest()
	
	passwdfi = open("passwd-" + user, 'r')
	passwdl = passwdfi.read()
	passwd = passwdl.split(':')
	print(len(passwd))
	
	for h in passwd:
		if h == hazh:
			return True
	
	return False

if os.system("cls"):
	os.system("clear")

print("Welcome To Chaff POC")
print("********************")
print()
print("1) Create New User")
print("2) Attempt To Login")
print()

while choice != '2' and choice != '1':
	choice = input("Choose[1,2]: ")
	
if choice == "1":
	passfi(input("Enter new username: "),hash(input("Enter new password: ")))
else:
	if auth():
		print("Congrats!")
