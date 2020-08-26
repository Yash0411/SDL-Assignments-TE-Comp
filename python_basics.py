# Function Task 1
def task1():
    print("\nTask 1")
    # input numbers
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    # Check product > 1000 (if-else condition statements)
    if num1 * num2 > 1000 :
        print(num1 + num2)
        return num1 + num2
    print(num1 * num2)
    return num1 * num2


# Function Task 2
def task2():
    print("\nTask 2")
    l = []
    sumarray = []
    # Get the list of numbers
    for i in range(10):
        n = int(input("Enter the number "+str(i+1)+" : "))
        # Add in list
        l.append(n)
        # Add number in sum list
        if i!=0:
            sumarray.append(l[i]+l[i-1])
    
    print("The list of sum of the current number and previous number : " + ' '.join(map(str,sumarray)))    
    return 


# Function Task 3
def task3():
    print("\nTask 3")
    s = input("Enter the string : ")

    print("Required string is : ",end='')
    # Print Characters at even places
    for i in range(len(s)):
        if i%2==1:
            print(s[i],end='')
    print('')
    return


# Function Task 4
def task4():
    print("\nTask 4")
    s = input("Enter a string : ")
    num1 = int(input("Enter a number : "))

    if num1 < len(s):
        k = s[num1:]
        print(k)
    else:
        print("Number is greater than length of string")
    return


# Function Task 5
def task5():
    print("\nTask 5")
    # Get the list of numbers
    l = list(map(float, input("Enter the list of numbers : ").split()))
    
    # Check
    if l[0]==l[-1]:
        print("True")
        return True
    else:
        print("False")
        return False


# Function Task 6
def task6():
    print("\nTask 6")
    # Get the list of numbers
    l = list(map(int, input("Enter the list of numbers : ").split()))

    # Fliter and print
    print("List of numbers divisible by 5 :",list(filter(lambda x: (x % 5 == 0), l)))
    return


# Function Task 7
def task7():
    print("\nTask 7")

    substr = "Emma"
    string = "ABC is good developer. ABC is a writer"

    print("Count of substring in given string is :",string.count(substr))
    return


# Function Task 8
def task8():
    print("\nTask 8")
    # Print Task 8
    for i in range(1,6):
        print(' '.join(map(str,[i]*i)))
    return


# Function Task 9
def task9():
    print("\nTask 9")
    # input number
    num1 = int(input("Enter the number : "))

    s = str(num1)
    s="".join(reversed(s))
    num2 = int(s)

    if num1 == num2:
        print("True")
        return True
    else:
        print("False")
        return False
    

# Function Task 10
def task10():
    print("\nTask 10")
    # Get the list of numbers
    l1 = list(map(int, input("Enter the first list of numbers : ").split()))
    l2 = list(map(int, input("Enter the second list of numbers : ").split()))

    finallist = list(filter(lambda x: (x % 2 == 1), l1)) + list(filter(lambda x: (x % 2 == 0), l2))
    print("Final List is : ",finallist)
    return


# Function Task 11
def task11():
    print("\nTask 11")

    # input number
    num1 = int(input("Enter a number : "))

    l = reversed(list(str(num1)))
    
    print("Integers in reversed order :",end=" ")
    for i in l:
        print(i,end=' ') 

    print('')
    return


# Function Task 12
def task12():
    print("\nTask 12")  
    
    # input number
    income = int(input("Enter income : ")) 

    if income < 10000 :
        tax = 0
    elif income < 20000:
        tax = 0.1 * income
    else:
        tax = 0.2 * income
    
    print("Tax is :",tax)
    return


# Function Task 13
def task13():
    print("\nTask 13")  

    for i in range(1,11):
        l = [i*j for j in range(1,11)]
        print("Table of",i,":",' '.join(map(str,l)))
    return


# Function Task 14
def task14():
    print("\nTask 14") 
    # Print
    for i in range(5,0,-1):
        print(' '.join(['*']*i))

    return


# Function exponent
def exponent(base, exp):
    return base**exp


# Function Task 15
def task15():
    print("\nTask 15") 
    # input numbers
    base = int(input("Enter base : "))
    exp = int(input("Enter exponent : "))

    print("Base raised to exponent :",exponent(base, exp))
    return


task1()
task2()
task3()
task4()
task5()
task6()
task7()
task8()
task9()
task10()
task11()
task12()
task13()
task14()
task15()