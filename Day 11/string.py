'''print("REVERSE A STRING")
text = input("Enter a string: ")
reverse = text[::-1]
print("Reversed string:", reverse)
print("FIND VOWELS IN A STRING")
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)
print("CHECK PALINDROME")'''
text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
