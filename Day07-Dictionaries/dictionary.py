student ={
    "name":"Dnyaneshwar",
    "age": 25,
    "course":"Python"
}

print("Student Name :", student["name"])

student["city"] ="Pune"

print("Updated Dictionary :", student)

for key, value in student.items():
    print(key, ":", value)