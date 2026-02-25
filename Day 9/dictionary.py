'''print("Employee salary record")
name=input("Enter employee name:")
emp_id=input("Enter employee id:")
salary=float(input("Enter employee salary:"))
details={"name":name,
         "emp_id":emp_id,
         "salary":salary}
print("Employee details")
print(details)
yearly_salary=12*salary
print(yearly_salary)'''
print("Bank account summary")
name = input("Enter account holder name: ")
acc_no = input("Enter account number: ")
balance = float(input("Enter account balance: "))

account = {
    "name": name,
    "account_number": acc_no,
    "balance": balance
}

print("\nAccount Details:")
print(account)

if balance < 1000:
    print("Warning: Low balance")
else:
    print("Balance is sufficient")
