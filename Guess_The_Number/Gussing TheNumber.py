

#Gussing The Number From 1 to 100 
import difflib
import random 
print("""
   ___                       _____ _                __                 _                
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __  
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__| 
/ /_\\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |    
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|    
                                                                                        
""")

The_Correct_number= random.randint(1,100)

print("Welcome to The Number Gussing name ")
print("I am Thinking in a number between 1 and 100 .")
difficulity=input("Choose The difficulity . 'easy' or 'hard' ")

if difficulity == 'easy' :
    lives= 10
    lives_sy = ['❤','❤','❤','❤','❤','❤','❤','❤','❤','❤']
    print(f"\nYou have ({lives}) attempts to guess the number . ")
    print(lives_sy)

elif difficulity == 'hard' :
    lives = 5 
    lives_sy = ['❤','❤','❤','❤','❤']
    print(f"\nYou have ({lives}) attempts to guess the number . ")
    print(lives_sy)


playing = True

while playing:

    gussing=int(input("what is your guess:  "))
#Kill One of His Life If False
    if gussing != The_Correct_number :
        lives -=1 
        lives_sy.pop()
        print(f"\nYou Still Have Only ({lives}) attempts")
        print(lives_sy)
#     print(live,sep="\n",end="" )
# print('\n')
#Checking For The Number
    if gussing == The_Correct_number :
        playing = False 
        print(f"\nYou Got It The Correct Number is :{gussing}")

    elif gussing > The_Correct_number :
        print("Try lower number .\n")

    elif gussing < The_Correct_number :
        print("Try higher number .\n")

#End The Game if his life is done . 
    if lives == 0 :
        playing = False 
        print(f"Game Over The Correct Number Was :{The_Correct_number}")
    









































