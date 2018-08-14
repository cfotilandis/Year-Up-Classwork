# count.py
# Prog to ask for name and number, then count by 2's

myName,countNum,endNum = "","",""

minVal, maxVal = 3,100

print('###### Counting through Python ######')
print("Hello.  Lets get ready to count.  We're going to need some info.")

myName=input('Your name?').capitalize()

def numQualify(x):
	if str(x).isdigit() == True:
		x = int(x)
		if x >= minVal:
			return x
		else:
			print('That number was outside of range.')
			return False
	else:
		print("That was not a correct number.")
		return False

while not myName.isalpha():
	print("That was not a name. Try again")
	myName=input('Please enter a correct name: ').capitalize()


endNum=input('Enter a number to count to: ')

while numQualify(endNum) == False:
	endNum = input("Please enter a number between %d and %d: " % (minVal,maxVal))

endNum=int(endNum)
maxVal=int(maxVal)
	
if endNum > maxVal:
	endNum = maxVal
	print("Your number is larger than %s.  Your number has been adjusted to %s." %(maxVal,maxVal))

countNum=input("Please pick an increment to count by: ")


while countNum:
	try:
		int(countNum)
	except ValueError:
		print ("That increment was not correct.")
		countNum=input("Try a different increment: ")
	else:
		countNum=int(countNum)
		break


print("Hello %s.  Your number is %s and you will be counting by %s's." % (myName,endNum,countNum))

input('Prepare to count!  Press Enter to start:')
print()

if(endNum % 2 == 0):
	startNum = 0
else:
	startNum = 1


for x in range(startNum,endNum+1,countNum):
	print(x)

print()
print('Done!  Thank you for counting with us today')






