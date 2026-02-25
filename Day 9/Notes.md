Dictionaries in Python:
A dictionary is a collection of key-value pairs.
Each value is accessed using its key.
Dictionaries are unordered, changeable, and do not allow duplicate keys.

Syntax:
dict_name = {
    "key1": value1,
    "key2": value2
}
eg:
student = {
    "name": "Gayathri",
    "age": 20,
    "dept": "ECE"
}
print(student)
Output:
{'name': 'Gayathri', 'age': 20, 'dept': 'ECE'}
Access values:
print(student["name"])
print(student["age"])
Output:
Gayathri
20
Add new key:
student["city"] = "Chennai"
print(student)
Update value:
student["age"] = 21
Remove key:
student.pop("dept")
Loop through dictionary:
for key, value in student.items():
    print(key, value)

