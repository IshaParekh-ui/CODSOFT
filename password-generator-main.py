import random
import string

num = int(input("Enter the desired length of password: "))
character_set = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(num):
    password += random.choice(character_set)
print(f"\nYour generated password: {password}")
