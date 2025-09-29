

#Gussing The Number From 1 to 100 
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
#Validating The Input  
while True:
    difficulty = input("Choose The difficulty . 'easy' or 'hard' ").lower().strip()
    if difficulty not in ['easy', 'hard']:
         print("Invalid input. Please enter 'easy' or 'hard'.")
    else:
        break 

if difficulty == 'easy' :
    lives= 10
    lives_sy = ['❤','❤','❤','❤','❤','❤','❤','❤','❤','❤']
    print(f"\nYou have ({lives}) attempts to guess the number . ")
    print(lives_sy)

elif difficulty == 'hard' :
    lives = 5 
    lives_sy = ['❤','❤','❤','❤','❤']
    print(f"\nYou have ({lives}) attempts to guess the number . ")
    print(lives_sy)


playing = True

while playing:

    #Validating The Input If It Is A Number  
    while True:
            guess_input = input("what is your guess:  ")
            if guess_input.strip().isdigit():
                gussing = int(guess_input)
                break
            else:
                print("Invalid input. Please enter a number.")



    if gussing != The_Correct_number :
        lives -=1 
        lives_sy.pop()
        print(f"\nYou Still Have Only ({lives}) attempts")
        print(lives_sy)

    #Checking For The Number If It Is Correct or Not 
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
    








































