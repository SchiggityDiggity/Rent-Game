# Made with AI as a tutor/guide
import random as r
import time as t
from games import calculate_total, black_jack, dice_game, rps
from play_again import again
from choices import pray2gods, ask_4_money, twih_stream

# MONEY MAKING VARIABLES
budget = 50
#word_choice = ['Pablo', 'Guilt', 'September', '1998', 'Shield', 'Change'] This is used to new  feature
#options = r.sample(word_choice, 3)
#correct_choice = r.choice(options)
pay_rent = True
goal = 250
play_game = True
zeus = False
energy_drink = 0
rounds_won = 0
energy_drink_counter = 0
#multiplying goal each 3 days -> goal = int(goal * 1.5)
name = input('What is your name? ')
print(f'''
=========================================
  Welcome {name}, you have to make rent
  for this month!

  You need to make $250!
  
  You got 3 days to make rent!
  
  Pay it by any means necessary...
=========================================
''')
while play_game:
  day = 1
  while day <= 3:
    if zeus == True:
      break
    energy = 3
    has_pray = False
    has_searched = False
    asked = False
    if energy_drink_counter >= 5:
      doctors_cost = r.randint(50, 250)
      print("You don't feel well...\nAll those energy drinks are finally taking a toll on your body...")
      print(f'You visited the doctor...it costed you ${doctors_cost}')
      budget -= doctors_cost
    print(f'Day: {day} Energy: {energy} Budget: ${budget}')
    while energy > 0:
      print(f'You have {energy} energy.')
      print(f'Your budget is ${budget}')
      print("You can: \n1.GAMBLE!\n2.Stream on Twih\n3.Pray to the gods\n4.Ask parents for money\n5.Accept you're done for\n6.Energy drink?")
      choice = input('What do you choose? ')
      if choice == '1':
        if budget > 0:
          print('Your choices are:\n1.Roll dice for $$$\n2.Black Jack\n3.Rock, Paper, Scissors!\n4.Hidden option!')
          choice_2 = input('What is your choice? ')
          if choice_2 == '1':
            while True:
              try:
                bet = int(input(f'How much will you bet on this?\nYour budget is ${budget}'))
                if bet > budget:
                  print(f'Bet within your budget of {budget}.')
                elif bet <= 0:
                  print('You gotta bet over 0 pal.')
                else:
                  break
              except ValueError:
                print('Enter a number bet')
            budget -= bet
            budget += dice_game(bet)
            energy -= 1
          elif choice_2 == '2':
            while True:
              try:
                bet = int(input(f'How much will you bet on this?\nYour budget is ${budget}'))
                if bet > budget:
                  print(f'Bet within your budget of {budget}.')
                elif bet <= 0:
                  print('You gotta bet over 0 pal.')
                else:
                  break
              except ValueError:
                print('Enter a number bet')
            budget -= bet
            double_down = False
            d_total = 0
            total = 0
            dealer_hand = []
            player_hand = []
            budget += black_jack(bet)
            energy -= 1
          elif choice_2 == '3':
            while True:
              try:
                bet = int(input(f'How much will you bet on this?\nYour budget is ${budget}'))
                if bet > budget:
                  print(f'Bet within your budget of {budget}.')
                elif bet <= 0:
                  print('You gotta bet over 0 pal.')
                else:
                  break
              except ValueError:
                print('Enter a number bet')
            budget -= bet
            choices = ['rock', 'paper', 'scissors']
            budget += rps(bet)
            energy -= 1
          elif choice_2 == '4':
            print('You lost a day :)')
            energy -= 4
        else:
          print("You're broke pal, get your money up.")
      elif choice == '2':
        if energy < 2:
          print("You don't have enough energy to stream.\nStreaming requires 2 energy!")
        else:
          print('You start your stream...')
          budget = twih_stream(budget)
          energy -= 2
      elif choice == '3':
        if has_pray == False:
          energy -= 1
          budget, goal, energy, day, energy_drink, zeus = pray2gods(budget, goal, energy, day, energy_drink)
          if zeus == True:
            play_game = False
            break
          has_pray = True
        else:
          print('You have already prayed...')
      elif choice == '4':
        if asked == False:
          print('You ask your parents for money...')
          budget = ask_4_money(budget, rounds_won)
          energy -= 1
          asked = True
        else:
          print("You already asked...don't want to annoy them.")
      elif choice == '5':
        print('You give up...')
        day += 3
        energy -= 10
      elif choice == '6':
        print('You open your fridge.')
        if energy_drink > 0:
          print(f'You have {energy_drink} drink(s)')
          print('Would you like to drink an energy drink?')
          drink = input('Drink energy drink? (y/n)').lower()
          if drink == 'y':
            energy += 2
            energy_drink -= 1
            energy_drink_counter += 1
            print('You feel energized!')
          else:
            print('Okay, you can drink it later')
        else:
          print('You have no energy drinks...')
          if has_searched == False:
            search = input('Search house for energy drinks? (y/n)').lower()
            search_list = ['Found Drink', 'No Drink found']
            if search == 'y':
              energy -= 1
              has_searched = True
              found_drink = r.choice(search_list)
              if found_drink == 'Found Drink':
                num_drink = r.randint(1, 3)
                energy_drink += num_drink
                print(f'You found {num_drink} energy drink(s)!')
              else:
                print('You found no energy drinks...')
            else:
              print("I guess you don't wanna check")
          else:
            print("\nYou've already searched for energy drinks")
      else:
        print('I guess you just gonna do nothing for the day.')
        energy -= 10
    if energy <= 0:
      print("You're tired, the day's over pal.")
    day += 1
  if zeus == True:
    print('You were struck down by Zeus, you lost')
    zeus = False
    play_again = again()
    if play_again == True:
      play_game = True
      budget = 0
      goal = 0
      energy_drink = 0
      rounds_won = 0
    else:
      play_game = False
  else: 
    print(f'''
=====================================
          RENT IS DUE PAL!
          
          RENT IS ${goal}!
=====================================
 ''')
    #phrase = input(f"Any final words? {options}")
    #if phrase == correct_choice:
      #print("The landlord's eyes widen, he runs in away in what seems to be fear...")
      #print("You manage to avoid paying rent this month...")
      #pay_rent = False
    #else:
      #print("The landlord looks at you with confusion, wondering what you meant by that.")
      #pay_rent = True
    if budget >= goal:
      print(f'You succeeded in paying your rent!')
      rounds_won += 1
      budget -= goal
      goal = int(goal * 1.5)
      print(f'Your new rent is {goal}, your budget is {budget}')
    else:
      print(f'You failed to pay your rent!\nGame Over, {name}!')
      print(f'You survived {rounds_won} rounds!')
      play_again = again()
      if play_again == True:
        play_game = True
        budget = 50
        goal = 250
        energy_drink = 0
        rounds_won = 0
      else:
        play_game = False
