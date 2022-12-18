list= [ {'item':'coffee','price':15 ,'milk':150,'bean':10,'water':150},
         {'item':'cappuccino','price':25 ,'milk':180,'bean':15,'water':120}]
std={'milk':1000,'bean':500,'water':1200}

amount=0
run=1
while run:
#print(std['milk'])
    print(f"Quantity of raw material inside the machine\n1.Milk= {std['milk']}\n2.Beans= {std['bean']}\n3.Water=  {std['water']}\nAvaliable balance= {amount}")

    select=input("select your refreshment\n1.coffee\n2.cappuccino\nEnter your selection here = ")

    for n in range(0,2):
        if list[n]['item']==select:
            if std['milk']>=list[n]['milk'] and std['bean']>=list[n]['bean'] and std['water']>=list[n]['water']:
                print(f"Your order is {list[n]['item']},and the price is Rs {list[n]['price']}")
                payment=int(input("please pay the amount to proceed =  Rs "))
                amount+=payment
                if list[n]['price']==payment:
                    print("\nOrder succesfull\nPlease collect your item from despenser\n")
                    std['milk']-=list[n]['milk']
                    std['bean']-=list[n]['bean']
                    std['water']-=list[n]['water']
             
                
    run=int(input("press 1 to continue & press 0 to exit."))