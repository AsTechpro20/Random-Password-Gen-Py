import random

# Main
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "Abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbol = "!@#$%^&*()_+<>?:{}"

# adding
string =  upper + lower + numbers + symbol
length = 8

#joining
password = "".join(random.sample(string,length))

#printing
ready = input ("Are You Ready to See your Password:")
if ready.lower() == 'no':
    print ("ok")

elif ready.lower() == 'yes':
    print ("Here is your password" + password)

else:
    yesorno = input ("Yes or No:")

if yesorno.lower() == 'no':
    print("Ok")
elif yesorno.lower() == 'yes':
    print("Here is your Password" + password)