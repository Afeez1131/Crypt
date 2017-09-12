import os
import sys


def banner():
	print('________ ')
	print('\  _____\ _______  __   __  ____    _')
	print('/  \      \_  __ \ \ \ |  ||  _ \ _| |__')
	print('\   \___ __ | | \/  \ \/ / | |__//__  _/')
	print(' \______  / |_|      /  /  | |     | |_ ')
	print('        \/          /__/   |_|     |_|/ ')
	print('          +----==[crypt v1 by Afeez ]==----+ ')
	
	
	print('+----==[  e.g Python3 crypt.py encrypt 200    ]==----+')
	print('       |------- A Warm Welcome to Crypt-------| ')
	print('       |--https://github.com/Afeez1131/Crypt--| ')
	print('       |------- Works only on Linux O.s-------| ')
	print('       |-------  Tested on Kali Linux  -------| ')
	print('python3 crypt.py pathtoatextfile mode[encrypt or decrypt] key[any number]')
	print('Usage: python3 crypt.py /root/Desktop/texttoencrypt.txt encrypt 20')
	print('python3 crypt.py /root/Desktop/texttodecrypt.txt decrypt 20')
	print()
	print('NOTE: you can only decrypt your file with the key you use to encrypt it, there is a folder on your Desktop/Encrypted called keys.txt, it contains your key for different fileName ')
__author__="Afeez (lawalafeez052@gmail.com) "
__date__ ="12- 09 -2017 "	

if len(sys.argv) <= 3:
	banner()
	sys.exit()
		
try:	
	banner()
	print()
	print()
	encrypted = ''
	letters = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
	name = sys.argv[1]
	n = open(name, 'r')
	m = ['encrypt', 'decrypt']
	mode = sys.argv[2]
	key = int(sys.argv[3])
	
	if mode.lower() not in m:
		print('[-] incorrect mode [encrypt or decrypt]')
		sys.exit()
	

	if os.path.isfile(name):	
		n2 = n.read()
		for line in n2:
			line = line.replace('\n', ' ')
			for word in line:
				for letter in word: 
					if letter in letters:
						num = letters.find(letter)
						if mode == 'encrypt':
							num += key
						elif mode == 'decrypt':
							num -= key
						if num >= len(letters):
							num -= len(letters)
						elif num < 0:
							num += len(letters)
						encrypted = encrypted + letters[num]
						
						
					else:
						encrypted += letter
						
	path = ('/root/Desktop/')
	os.chdir(path)
	
	if os.path.isdir('Encrypted'):
		os.chdir('Encrypted')
		fileName = input('Enter the name for the output file: ')
		output = open(fileName, 'w')
		output.write(encrypted)
		keys = open('Keys.txt', 'a')
		keys.write('FileName' + '=' + fileName +  '\t\t'+ 'Key ' + '='+str(key) +'\n')
								
	elif os.path.isdir('Encrypted') == False:
		os.mkdir('Encrypted')
		os.chdir('Encrypted')
		
		fileName = input('Enter the name for the output file: ')
		output = open(fileName, 'w')
		keys = open('Keys.txt', 'w')
		output.write(encrypted)
		keys.write('FileName' + '=' + fileName +  '\t\t'+ 'Key ' + '='+str(key) +'\n')
		output.close()			
			
except FileNotFoundError:
	print('[-] File Not Found')
	
except ValueError:
	print('[-] Make sure you enter the correct parameter')
	
except IsADirectoryError:
 print('[-] Make sure to enter a valid text path ')

else:
	print('[-] File Encrypted Successfully' )
	print('File Path: ')
	print(' 	/root/Desktop/Encrypted/' + fileName )


					


			
	
