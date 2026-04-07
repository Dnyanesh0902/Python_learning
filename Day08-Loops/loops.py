# For Loop Example

print("For Loop Example")

for i in range(1,6):
    print(i)


# Loop through list

print("\nLoop through list")

fruits =["Apple","Banana","Mango"]

for fruit in fruits:
    print(fruit)

# While Loop Example

print("\n While Loop Example")

i = 1

while i <= 5:
    print(i)
    i +=1

#Break Example

print("\nBreak Example")

for i in range(10):
    if i == 5 :
        break

    print(i)

# Continue Example

print("\nContinue Example")

for i in range(5):
    if i == 2 :
        continue
    print(i)