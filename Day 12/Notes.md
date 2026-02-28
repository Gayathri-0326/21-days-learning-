File Handling in Python:
  File handling is used to create, read, write, and modify files in Python.
  It allows programs to store data permanently
  
Opening a File:
file = open("filename.txt", "mode")
Mode
Meaning
r - Read (default)
w - Write (overwrites file)
a - Append (adds to file)
x - Create new file
rb - Read binary
wb - Write binary

Writing to a File:
file = open("sample.txt", "w")
file.write("Hello Python")
file.close()
If file doesn’t exist → created
If exists → content overwritten

Appending to a File:
file = open("sample.txt", "a")
file.write("\nWelcome")
file.close()

Reading from a File:
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

Reading Line by Line:
file = open("sample.txt", "r")
for line in file:
    print(line)
file.close()

Important File method:
Method
Description
read() - Reads entire file
readline() - Reads one line
readlines() - Reads all lines into list
write() - Writes data
close() - Closes file
