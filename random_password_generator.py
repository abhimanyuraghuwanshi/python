import random
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x',"y","z"]
digit= ['1','2','3','4','5','6','7','8','9','0']
symbol= ['`','!','@','$','%','*',')',':','<']

print("program for generating strong password\n")
def show(display):
    password=""
    for char in display:
        password+= char
    print(password)

alp= int(input("specify how many alpharbet you want"))
num= int(input("specify how many numerical you want"))
sym= int(input("specify how many symbols you want"))

display = []
for n in range(alp):
    display += random.choice(alpha)

for n in range(num):
    display += random.choice(digit)

for n in range(sym):
    display += random.choice(symbol)

random.shuffle(display)
show(display)   