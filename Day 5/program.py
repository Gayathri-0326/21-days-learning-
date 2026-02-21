print("Multiplication table")
num=int(input("Enter a number:"))
for i in range(1,11):
    print(num,"X",i,"=",num*i)
print("Factorial of a number")
num=int(input("Enter a number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial=",fact)
print("Sum of numbers(1 to n)")
num=int(input("Enter a number:"))
total=0
for i in range(1,num+1):
    total+=i
    print("Sum=",total)
print("pattern printing")
rows=int(input("Enter number of rows:"))
for i in range(1,rows+1):
    print("*"*i)
    
