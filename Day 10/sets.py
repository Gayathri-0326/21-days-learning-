print("Remove duplice elements from a list")
n=list(map(int,input("Enter elements to insert in list:").split()))
f=set(n)
print(f)
print("Find common subjects")
subjects1=set(input("Enter subjects of ECE:").split())
subjects2=set(input("Enter subjects of EEE:").split())
common=subjects1&subjects2
print("Common subjects=",common)
