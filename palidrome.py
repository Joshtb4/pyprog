def is_palindrome(text):
    text = text.lower() 
    text = text.replace(" ", "")  
    return text == text[::-1]  

user_input = input("Enter a word or phrase: ")

if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")