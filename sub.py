import sys
import random

if len(sys.argv) != 4:
	print "Usage python sub.py [-e,d] <file> <key>"
	sys.exit(0)

key = int(sys.argv[3])
random.seed(key)

letters = ""
for i in xrange(0,256):
	letters+= chr(i)

#letters = "abcdefghijklmnopqrstuvwxyz "

letters_list 		= list(letters)

substitution_list 	= list(letters)
random.shuffle(substitution_list)

E = dict (zip(letters_list,substitution_list))
D = dict (zip(substitution_list, letters_list))


def encrypt (string):
	e = ""
	for s in string:
		e = e + E[s]

	return e


def decrypt (string):
	d = ""
	for s in string:
		d = d + D[s]

	return d

f = open(sys.argv[2],"rb")
data = f.read()
f.close()


if sys.argv[1] == "-e":
	print encrypt(data)
else:
	print decrypt(data)
