import random
import string
password_length =int(input("enter any length:"))
characters ="!@#$%^&*()_.|~" + string.ascii_letters + string.digits
password=""
for i in range(password_length):
    password = password+random.choice(characters)
print(password)
