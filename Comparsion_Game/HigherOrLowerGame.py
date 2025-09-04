from re import A
from game_logo import vs
from game_logo import logo

from game_data import data
from random import randint

import os
print(logo)

score=0



def first_person () :

    first_person =data[randint(0,49)] 
    name = first_person['name']
    follower= first_person['follower_count']
    carrer = first_person["description"]
    country = first_person['country'] 
    print(f'Compare A : {name},a {carrer},From {country}')

    return follower

def second_person ():

    second_person =data[randint(0,49)] 
    name = second_person['name']
    follower= second_person['follower_count']
    carrer = second_person["description"]
    country = second_person['country'] 
    print(f'Compare B : {name},a {carrer},From {country}\n')
    
    return follower



playing = True
while playing:

    

    first=first_person()
    print(vs)
    second=second_person()
    the_winner =''

    if first > second :
        the_winner = "A"
    elif first < second :
        the_winner = "B"

    gussing =input("who Has More Followers? Type 'A' or 'B' :").capitalize()

    if gussing == the_winner :
        os.system('cls')
        score +=1 
        print(f'You Got IT.\nYour Score Now Is ({score}) \n')
    else :
            
            print(f'Not True \nYour Score Now Is ({score}) \n')
            break





















