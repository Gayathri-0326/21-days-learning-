print("Storing user data")
name = input("Enter name: ")
age = input("Enter age: ")

with open("users.txt", "a") as file:
    file.write(name + "," + age + "\n")

print("User data saved successfully!")
print("Save mark reports")
name = input("Enter student name: ")
marks = input("Enter marks: ")

with open("report.txt", "w") as file:
    file.write("Student Name: " + name + "\n")
    file.write("Marks: " + marks)

print("Report saved.")

