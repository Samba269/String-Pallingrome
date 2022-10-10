def ispallindrome(str):
    return str==str[::-1]

str=input("enter a string:")

if ispallindrome(str):
    print("the string is pallindrome")
else:
    print("the string is not pallindrome")