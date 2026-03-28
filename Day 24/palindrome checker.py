
def is_palindrome(text):
   
    text = text.lower().replace(" ", "")
    rev = text[::-1]
    
    if text == rev:
        return True
    else:
        return False


word = input("Enter a word or number: ")

if is_palindrome(word):
    print("It is a Palindrome")
else:
    print("Not a Palindrome")
