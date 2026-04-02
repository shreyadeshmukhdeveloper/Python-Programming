import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*']
print("welcome to the password generator")
en_letter=int(input("enter numbers of letter do you want?\n"))
en_symbol=int(input("enter numbers of symbol do you want?\n"))
en_number=int(input("enter numbers of number do you want?\n"))

password=[]
for pass1 in range(0,en_number):
    password.append(random.choice(numbers))

for pass1 in range(0, en_symbol ):
    password.append(random.choice(symbols))

for pass1 in range(0,en_letter ):
    password.append(random.choice(letters))

random.shuffle(password)
password_list=""

for pass1 in password:
    password_list+=pass1
print(f"your password is :{password_list}")
