import random

# a function to select random cards
def deal_cards():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10]
  choice = random.choice(cards)
  cards.remove(choice)

  return choice

# a function to calculate the sum of cards drawn
def calculate_score(cards):
  score = sum(cards)
  blackjack = 0

  # check for blackjack when the game starts
  if len(cards) == 2 and score == 21:
    return blackjack
  elif score == 21:
    return blackjack
  
  # replace value of ace from 11 to 1 if score>21
  for card in cards:
    if card == 11 and score > 21:
      cards.remove(card)
      card = 1
      cards.append(card)
      score = sum(cards)
  
  return score

# a function to check user's status in the game
def check_user_status(score):
  if score == 0:
    print("User Wins")
    return True
  elif score > 21:
    print("User lost")
    return True
  else:
    return False

def check_cpu_status(score):
  if score == 0:
    print("CPU wins")
    return True
  elif score>21:
    print("User wins")
    return True
  else: 
    return False

def compare(userScore, cpuScore):
  if userScore == cpuScore:
    print(f"User: {userScore} v CPU: {cpuScore}")
    print("Draw")
    return False
  elif (cpuScore == 0 or userScore > 21):
    print(f"User: {userScore} v CPU: {cpuScore}")
    print("CPU Wins")
    return False
  elif cpuScore > userScore or cpuScore == 0:
    print(f"User: {userScore} v CPU: {cpuScore}")
    print("CPU Wins")
    return False
  elif userScore > cpuScore or userScore == 0:
    print(f"User: {userScore} v CPU: {cpuScore}")
    print("User Wins")
    return False    
  elif (userScore == 0 or cpuScore > 21):
    print(f"User: {userScore} v CPU: {cpuScore}")
    print("User Wins")
    return False
  else:
    return True
 

restart = True

while restart:
    user_cards = [deal_cards(),deal_cards()]
    cpu_cards = [deal_cards(),deal_cards()]

    # assign user and cpu scores to variables
    cpu_score = calculate_score(cpu_cards)
    user_score = calculate_score(user_cards)

    # assign game ending conditions to variables
    user_conditions = check_user_status(user_score)
    cpu_conditions = check_cpu_status(cpu_score)

    print(f"CPU's first card is {cpu_cards[0]}")
    print(f"Your cards are {user_cards[0]} and {user_cards[1]} = {user_score}")


    # check for game ending conditions
    flag = True
    while flag:
        if user_conditions or cpu_conditions:
            flag = False
        else:
            user_input = input("Do you want to draw another card?\n").lower()

            if user_input == "yes":
                new_user_card = deal_cards()
                print(f"User selected {new_user_card}")
                user_cards.append(new_user_card)
                user_score = calculate_score(user_cards)
                print(f"Your current score is: {user_score}")
                user_conditions = check_user_status(user_score)
            else: 
                print(f"CPU's current score is {cpu_score}")
                break


    while flag: 
    # need to refactor this 

        if cpu_conditions:
            print("Game Ends")
            flag = False
        elif cpu_score < 17:
            new_cpu_card = deal_cards()
            print(f"CPU selected {new_cpu_card}")
            cpu_cards.append(new_cpu_card)
            cpu_score = calculate_score(cpu_cards)
            print(f"CPU's current score is: {cpu_score}")
            cpu_conditions = check_user_status(user_score)
            
            if cpu_score < user_score and cpu_score >21:
                new_cpu_card = deal_cards()
                print(f"CPU selected {new_cpu_card}")
                cpu_cards.append(new_cpu_card)
                cpu_score = calculate_score(cpu_cards)
                print(f"CPU's current score is: {cpu_score}")
                cpu_conditions = check_user_status(user_score)
                flag = compare(user_score,cpu_score)
                print(flag)
        else:
            flag = compare(user_score,cpu_score)
    
    to_restart = input("Do you want to restart the game? \n").lower()
    
    if to_restart == "yes":
        restart
    else:
        print("Game Over")
        restart = False
    
