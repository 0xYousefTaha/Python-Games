from re import A
from game_data import data
from random import randint
import game_logo
import os





def first_person():
    person = data[randint(0, 49)]
    name = person['name']
    follower = person['follower_count']
    carrer = person["description"]
    country = person['country']
    print(f'Compare A : {name}, a {carrer}, From {country}')
    return person


def second_person():
    person = data[randint(0, 49)]
    name = person['name']
    follower = person['follower_count']
    carrer = person["description"]
    country = person['country']
    print(f'Compare B : {name}, a {carrer}, From {country}\n')
    return person



score = 0
playing = True
while playing:
    print(game_logo.logo)
    first = first_person()
    # Ensure second person is not the same as first
    print(game_logo.vs)

    while True:
        second = second_person()
        if second['name'] != first['name']:
            break

    the_winner = ''
    if first['follower_count'] > second['follower_count']:
        the_winner = "A"
    elif first['follower_count'] < second['follower_count']:
        the_winner = "B"
    else:
        the_winner = None  # In case of a tie

    while True:
        gussing = input("Who Has More Followers? Type 'A' or 'B': ").strip().capitalize()
        if gussing not in ['A', 'B']:
            print("Invalid input! Please type 'A' or 'B'.")
            continue
        break

    if gussing == the_winner:
        os.system('cls' if os.name == 'nt' else 'clear')
        score += 1
        print(f'You Got IT.\nYour Score Now Is ({score}) ')
    else:
        print(f'Not True \nYour Score Now Is ({score}) ')
        break





















