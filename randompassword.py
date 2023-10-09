import string
import random
#Getting password length
len=int(input("Enter password length:"))
print('''Choose character set for password from these:
      1. Digits
      2. Letters
      3. Special characters
      4. Exit''')
charlist=" "
#Getting character set for password
while(True):
    choice=int(input("Pick a number:"))
    if choice==1:
        #Adding letters to possible characters
        charlist+=string.ascii_letters
    elif choice==2:
        #Adding letters to possible characters
        charlist+=string.digits
    elif choice==3:
        #Adding letters to possible characters
        charlist+=string.punctuation
    elif choice==4:
        break
    else:
        print("please pick a valid option!")
password=[]
for i in range(len):
    #picking a random character from our char list
    randomchar=random.choice(charlist)
    #appending a random char to password
    password.append(randomchar)
#printing password as a string
print("The random password is "+" ".join(password))
        




