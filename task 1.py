print("Welcome to the Random Password Generator")
import string
import random

string1=string.ascii_lowercase
string2=string.ascii_uppercase
string3=string.digits
string4=string.punctuation

password_length=int(input("Enter the length of your password:"))

s=[]
s.extend(list(string1))
s.extend(list(string2))
s.extend(list(string3))
s.extend(list(string4))
random.shuffle(s)

print("Your password is:")
print("".join(s[0:password_length]))
