#  Program 1 - Check Positive Or Negative

num = int(input("Enter Number : "))

if num > 0 :
    print("Positive Number")
else :
    print("Negative Number")


# Program 2 - Check Even or Odd

num = int(input("Enter Number : "))

if num % 2 == 0 :
    print("Even")
else:
    print("Odd")


# Program 3 - Salary Bonus

Salary = int(input("Enter Salary: "))
if Salary > 50000 :
    print("Bonus granted")
else:
    print("No Bonus")

# Program 4 - Student Grade

marks = int(input("Enter Marks : "))

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50 :
    print("Grade C")
else:
    print("Fail")