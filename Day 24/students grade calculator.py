
def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"


name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

total = 0


for i in range(n):
    mark = int(input(f"Enter mark for subject {i+1}: "))
    total += mark

average = total / n


grade = calculate_grade(average)


print("\n--- Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)
