#encryption.py
#To encrypt and decrypt files.
import re


index,key,keyLow,keyHigh=0,0,3,26
userName,cryptVar,userInput,enOrDe="",[],"","",
options = ['E', 'D', 'X']
#Function to make sure the input for 'key' is a number, greater than 3, and less than 26.
def keySetup(x):
	try:
		int(x)
	except ValueError:
		print("Please enter a number for the key")
		return False
	else:
		x=int(x)
		if x < keyLow:
			print("That key number is too low")
			return False
		else:
			if x > keyHigh:
				print("That key is too high")
				return False
			else:
				return True

#Makes sure the text is within the designed parameters of that box and actually has text/ no blanks.
def textVerify(x,y):
	while not y:
		print("No text received")
		return False
	else:
		while not re.match(x,y):
			print("Unauthorized symbols for this text box")
			return False

#This function checks to see if the user wants to either encrypt or decrypt their text.  It will not allow numbers, blanks, or any letters besides "e" or "d"		
print("###########Lets get to coding!###########")

#Asks for user's name
userName=input("What is your name?: ").capitalize()

#Determines if the input for the person's name has any symbols/numbers in it. Only symbols allowed are alpha, aprostrophe, spaces, and hyphens.
while textVerify("^[a-zA-Z '-]*$",userName) == False:
	userName = input("Write a message that contains text without numbers: ").capitalize()


print("Hello %s. " %(userName))
#Checks if the user wants to encrypt or decrypt.  Only allows "E, D, and X."
cryptVar=input("Please choose to encrypting or decrypting by writing either 'E' or 'D'.  If you want to quit, type X: ").upper()
while cryptVar not in options:
	print("\nYou entered something besides 'E' or 'D'")
	cryptVar = input('Enter "E" to Encrypt, "D" to Decrypt, or "X" to Exit: ').upper()#Error if anything other than e, d, or x
if cryptVar == "E":
	print("\n You have chosen encryption \n")
	enOrDe = "encrypted"
if cryptVar == "D":
	print("\n You have chosen decryption \n")
	enOrDe ="decrypted"
if cryptVar == "X":
	print("\nGood bye!")
	exit()
#Asks for user's text to be encrypted or decrypted.
userInput = input("Please write what you want to be %s: " % (enOrDe)).lower() 

#Determines that the user's text to be changed does not have numbers in it.
while textVerify("^[^\d]*$",userInput) == False:
	userInput = input("Write a message that contains text without numbers: ").lower()

print ("\n You have entered '%s' to be %s.\n" % (userInput,enOrDe))

#Asks the user for how much the letters will be shifted.
key = input("Please enter the 'key' that is greater than %d and less than %d :" % (keyLow,keyHigh))

#Checks to see if the key is a number
while keySetup(key)==False:
	key=input("Please enter a numeric key:")	
else:
	key=int(key)

#if they are decrypting, the key is swapped from positive to negative.
if cryptVar == "D":
	key = -key

print(userInput)
print("Translating...")
print("\n")

#Loop to convert letters into  the new letters.
for char in userInput:
	#If letters are outside the lowercase range or are a space, leave as they are.
	if ord(char) < 97 or ord(char) > 122 or char == " ":
		print (char, end="")
	else:
		#If the letter is looping
		if (ord(char)+key) > 122:
			char=(ord(char)+key)-26
		elif (ord(char)+key) < 97:
			char=(ord(char)+key)+26
		else:
			char=ord(char)+key
		print (chr(char), end="")



print("\n")



print("Done!  Your word has been %s! Do not forget that your key is %d." % (enOrDe,key))


print("\nGood bye!")
# https://www.pythonlearn.com/html-008/cfbook007.html
# https://docs.python.org/2/library/functions.html#ord
# https://docs.python.org/3/tutorial/datastructures.html
# http://www.practicalcryptography.com/cryptanalysis/cipher-implementations/caesar-cipher-implementation/
# https://inventwithpython.com/hacking/
