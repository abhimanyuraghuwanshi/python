import random
p=''' 
       ____             _____   _____    _____
      |        |    |  |       |        |
      | ____   |    |  |_____  |_____   |_____    
      |     |  |    |  |             |        |
      |_____|  |____|  |_____   _____|   _____|
      '''
print(p)
num= random.randint(0,100)
#print(num)

run=True

print("HELLO I m your computer and i have memorised a number between 0 to 100 in my mind\nLets see if you can guess.")
level=int(input("choose your gaming level between\n 1.hard = you get 5 guess \n2.easy = you get 7 guess\n"))
if level==1:
    life=5
elif level==2:
    life=7
else:
    print("invalid input")
    
while run:
    guess= int(input("\ntype the number you guessed\t"))
    if guess==num:
        print(f"Congratulation the number {num} is correct and you win")
        run= 0
    if guess<num:
        life-=1
        print(f"your number is smaller than mine, you lose a life = {life}\n try again") 
    if guess > num:
        life-=1
        print(f"your number is greater than mine, you lose a life = {life}\n try again")
    if life ==0:
        run = False
        print("your lifes are ended,YOU LOST")

input()