import random
import string

print("Welcome to my Project 'PASSWORD GENERATOR'")
length = int(input("Enter length of password:"))

if length>5:
 letters = string.ascii_letters
 digits = string.digits
 symbols = string.punctuation

 all_chars = letters + symbols + digits 

 password = ''.join(random.sample(all_chars,length))

 print(f"Your secure password is:\n", password)

else:
 print("Too Short....! ,Password must be atleast 8 characters") 
