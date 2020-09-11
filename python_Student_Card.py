import numpy as np  # import numpy

# Declare a Class Student
class Student:
    
    # Pass name, class, PRN from constructor
    def __init__(self, name, clas, PRN):
        self.name = name    # Name as name
        self.clas = clas    # cls as class
        self.PRN = PRN      # PRN as PRN
        self.marks = []     # Maeks as marks array
        self.avg = 0        # Declare average to 0 initially
        self.status = "Pass"    


    # Accept marks for each semester
    def accept_marks(self):
        
        for i in range(5,0,-1):
            print("\nEnter The marks of semester",i)
            
            # Declare Sem array for storing marks of each sem
            sem = []
            j = 0

            while j<5 :

                # Exception Handling inplemented here
                try:
                    m = int(input("Enter marks for subject "+ str(j+1)+" : ")) # Get marks
                    if m<40 or m>100 :
                        if m<40 and m>=0:
                            self.status = "Fail"
                        else:
                            raise 
                    sem.append(m)
                    j+=1
                except:
                    print("Enter a number between 40 to 100 as marks")

            # append sem to marks
            self.marks.append(sem)
    
    # get avg for each student
    def average(self):

        np_marks = np.asarray(self.marks)   # convert list array into numpy array 
        self.avg = np.average(np_marks)     # calculate average using numpy
        print("\nAverage of the student ",self.name, " for all semesters is : ",self.avg,"\n Student is",self.status) # Print average and status

# k for getting option
k = 1
# array to store students
students = []

while(k!=0):
    k = int(input("\nEnter YOur Choice : \n 1. Add Student \n 2. Display Aggregate of added students \n 0. To Terminate \n => "))
    
    if k==1:
        # Get student
        name = input("\nEnter the name of student : ")
        clas = input("Enter the class of student : ")
        PRN = input("Enter the PRN of student : ")
        student = Student(name,clas,PRN)    # New object creation
        student.accept_marks()              # accept marks
        student.average()                   # calcualte average
        students.append(student)            # append to students array
    
    elif k==2 :
        # Print all students
        print("\nAverage For all students entered")        
        for i in students:
            i.average()
    
    elif k==0:
        # Terminate
        break
    
    else :
        print("Enter Proper value")



