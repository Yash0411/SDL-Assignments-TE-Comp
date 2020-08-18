#input string and split it 
s = list(input("Enter a string : ").split())

# Initialize empty dictionary
dict = {}

for i in s:
	if i in dict:
		dict[i]+=1
	else:
		dict[i]=1

print("Count Of Words :")
for i in dict.items():
	print(i[0],"-",i[1])
	
print("Total number of words in string -",len(s))