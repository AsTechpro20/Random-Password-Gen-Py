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
print ("Your Password is:" + password)