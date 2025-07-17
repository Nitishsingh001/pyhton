

# conditional statements

age = int(input("Enter your age: "))

if(age >= 20): 
    print("You are eligible to syndicate")
else:
    print("You are not eligible to syndicate")

# checking num is positive or negative or zero 
num = int(input("Enter a number: "))

if(num==0):
    print("Zero")
elif(num > 0):
    print("Positive")
else:
    print("Negative")

# program for number is even or not 

num1 = int(input("Enter a number: "))

if(num1 >=0): 
    if(num1%2 ==0 ):
        print("Even")
    else:
        print("odd")
else:
    print("Negative number")



#  calculator program using match case 





num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

choice =input("enter your choice ")

match choice:
    case "add":
        print("The sum is :", num1 + num2)
    case "sub":
        print("The difference is :", num1 - num2)
    case "mulF": 
        print("The product is :", num1 * num2)
    case _:
        print("Invalid choice entered")


#   Loop in python  >> while loop 

j =0; 
i =1; 
while(i <= 11):
    j+=i
    i += 1
   
  
    
print("The final sum is ", j)


# for loop 

for i in range(1,11,3):
    print(i)

for ch in "python":
    print(ch)

#  Loop through a string and print only vowels.
