import random
MAX_TRIES = 6
name = input("Enter your name: ")
right = random.randint(1,100)
print(f'Hi {name}!' """ I quessed the number between 1 and 100.
Try to guess it. You have six tries\n""")

tries = 0

while tries < 6:
    tries+=1
    num = int(input("Enter your number: "))
    if  num > right:
        print("my number is smaller")
    elif num < right:
        print("my number is bigger")
    else: 
        print("Yes! my number is ", right, "You have used only",tries, "tries") 
        
        break

if tries == 6:
    print("Sorry, You lose")





    
    
    



