import random
from os import system
from dol import stage

def show(life):
    dis="-"
    dis= ' '.join(display)
    print(dis)

wordlist = ["england","london" , "america", "india"]

word = random.choice(wordlist)
print("Guess the name of the city and win the game (you have 6 lifes before you lose)")
#print(word)
display=[]
for _ in range(len(word)):
   display+="_"

life= 6
end= False
while not end:
    
    guess= input("Guess the letter = ").lower()

    system('cls')
    
    if guess in display:
        print("you have already guessed it") 

    for position in range(len(word)):
        letter= word[position]
        if guess == letter:
            display[position] = letter

    if guess not in word:
        life-=1
        print(life,"= You lose a life")
        if life==0:
            end = True
            print("Game over")

    print(stage[life])
    show(life)

    if "_" not in display:
        end = True
        print("You win")

print("THE END")
t=input("hope you enjoyed it.")
    

