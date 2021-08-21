def multi(a,b):
	return a*b

print (multi(8,8))

def testGrade(levle):
	if(levle == 'A'):
		return "90~100"
	elif(levle == "B"):
		return "80~90"
	elif(levle == "C"):
		return "70~79"
	elif(levle == "D"):
		return "60~69"
	elif(levle == "F"):
		return "<60"
	else:
		return "give a wrong level!"

print (testGrade('A'))
print (testGrade('B'))
print (testGrade('C'))
print (testGrade('D'))
print (testGrade('F'))

def testPrice(num):
	count25 = int(num / 0.25);
	count10 = int((num - 0.25 * count25) / 0.1)
	count5 = int((num - 0.25 * count25 - 0.1 * count10) / 0.05)
	count1 = int((num - 0.25 * count25 - 0.1 * count10 - 0.05 * count5) / 0.01)
	return count25,count10,count5,count1

print (testPrice(0.88))
