from random import * 

logo = \
"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   


cards= [1,2,3,4,5,6,7,8,9,10,10,10]
print(logo)

your_card = []
computer_card = []

your_card.append(choice(cards))
your_card.append(choice(cards))

computer_card.append(choice(cards))
computer_card.append(choice(cards))

your_sum=0
for card1 in your_card :
    your_sum +=card1

computer_sum=0
for card2 in computer_card :
    computer_sum +=card2
    
yours = f'your card is {your_card}  Total is :{your_sum}'
computer=  f'Computer card is {computer_card[0] } '

print(yours)
print(computer)


def Check_for_winner(x=your_sum,y=computer_sum) :
    """Game Instructions """

    if x > 31 and y > 31:
        return "No Winner ."

    if x == y:
        return "Draw 🙃"
    
    elif y == 31:
        return "Lose, opponent has Blackjack 😱"
    
    elif x == 31:
        return "Win with a Blackjack 😎"
    
    elif x > 31:
        return "You went over. You lose 😭"
    
    elif y > 31:
        return "Opponent went over. You win 😁"
    
    elif x > y:
        return "You win 😃"
    else:
        return "You lose 😤"



another_card = True
while another_card :
    
    while True: 
        y = input("Type 'yes' to get another card or 'no' to pass: ").strip().lower()

        if y == 'yes' or y == 'no':
            break  # valid input, exit the loop
        else:
            print("Invalid input. Please type 'yes' or 'no' only.") 

    if y== 'yes' :
        #User
        your_card.append(choice(cards))
        your_sum +=your_card[-1]
        yours = f'your card is {your_card}  Total is :{your_sum}'

        #Computer
        computer_card.append(choice(cards))
        computer_sum+=computer_card[-1]
        computer=  f'Computer card is {computer_card[0]},{computer_card[1]}'
        print(yours)
        print(computer)

    else :
        another_card= False
        print(f'Your score is :{your_sum}')
        print(f'computer score is :{computer_sum}   {computer_card}')
        print(Check_for_winner(your_sum,computer_sum))



















