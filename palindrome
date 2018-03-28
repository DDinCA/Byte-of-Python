import string
def reverse(text):
    return text[::-1]#第85页 用切片功能翻转

def is_palindrome(text):
   forbidden = (',',' ','.', '?')
   for item in forbidden:
       text = text.replace(item, "")
   text = text.lower()
   return text == reverse(text)

something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
