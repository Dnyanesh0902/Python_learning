#program 1 - Addition
a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

print("Sum: ", a+b)

#program 2 -Even or Odd
num = int(input("Enter Number : "))

if num %2 == 0 :
    print("Even Number")
else:
    print("Odd Number")

# Program 3 -Login System

username =input("Enter Username : ") 
password = input("Enter Password : ")
if username =="Admin" and password == "1234" :
    print("Login Successful")
else :
    print("Login Failed")
    