# Define File Here
inFile = 'file.txt'

# Exception try
try:
    # Open File
    with open(inFile,'r') as f:
        # Read File
        words = list(f.read().split())
        
        # Declare Dictionary
        dict = {}

        # Add each word count in dictionary
        for i in words:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        
        # Print 
        print("\nCount Of Words :")
        for i in dict.items():
            print(i[0],"-",i[1])
            
        print("\nTotal number of words in file -",sum(dict.values())) # Instead Of sum(dict.values()) len(words) also give the same output
        f.close()

        

except:
# Exception handeled
    print("Can't Open The File")