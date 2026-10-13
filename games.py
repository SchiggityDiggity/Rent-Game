def calculate_total(hand):
      total = 0
      ace_count = 0
      for card in hand:
        rank = card.split()[0]
        try:
          int(rank)
          total += int(rank)
        except ValueError:
          if rank == 'jack' or rank == 'queen' or rank == 'king':
            total += 10
          elif rank == 'ace':
            total += 11
            ace_count += 1
      while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
      return total

import random as r

d_total = 0
total = 0
dealer_hand = []
player_hand = []
def black_jack(bet):
  double_down = False
  num = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
  suites = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
  #play_again = True
  #dealer_hand = []
  #player_hand = []
  #while play_again:
    #dealer_hand.clear()
    #player_hand.clear()
  
  cards = []
  dealer_hand = []
  player_hand = []
  for n in num:
    for suit in suites:
      cards.append(f'{n} of {suit}')
  r.shuffle(cards)
  for i in range(2):
    drawn_card = cards.pop()
    player_hand.append(drawn_card.lower())
    drawn_card = cards.pop()
    dealer_hand.append(drawn_card.lower())
  ace_count = 0
  total = calculate_total(player_hand)
  d_total = calculate_total(dealer_hand)
  game = True
  while game:
    print(f'Your cards: {player_hand}\n')
    print(f"Dealer's card: {dealer_hand[0]}\n")
    choice = input('Hit, Stand, or Double Down?').lower()
    if choice == 'hit':
      drawn_card = cards.pop()
      player_hand.append(drawn_card.lower())
      total = calculate_total(player_hand)
      if total > 21:
        print('You busted')
        print(f'''
============================================
  Dealer won with {d_total}!
============================================
      ''')
        return 0
    elif choice == 'stand':
      print(f'You stand with a total of {total}')
      break
    elif choice == 'double down':
      drawn_card = cards.pop()
      player_hand.append(drawn_card.lower())
      total = calculate_total(player_hand)
      if total > 21:
        print(f'You busted with a total of {total}.')
        print(f'''
============================================
  Dealer won with {d_total}!
============================================
        ''')
        return - bet
      else:
        double_down = True
        break
    else:
      print("That's not a choice, try again")
  # DEALER'S TURN    
  d_total = calculate_total(dealer_hand)
  print(f"\nDealer's hand: {dealer_hand}")
  while d_total < 17:
    #print(f"Dealer's hand: {dealer_hand}")
    drawn_card = cards.pop()
    dealer_hand.append(drawn_card.lower())
    d_total = calculate_total(dealer_hand)
    print(f"\nDealer's hand: {dealer_hand}")

  if d_total > 21 and double_down:
    print(f''''
============================================
  Dealer busted with {d_total}!
  
  You won with {total}!
============================================
  ''')
    return bet * 4
  elif total > 21:
    print(f'''
============================================
  Dealer won with {d_total}!
============================================
  ''')
    return 0

  elif d_total > 21:
    print(f''''
============================================
  Dealer busted with {d_total}!
  
  You won with {total}!
============================================
  ''')
    return bet * 2

  elif total > d_total:
    print(f'''
============================================
  You won with {total}
  
  Dealer had {d_total}!
============================================
  ''')
    return bet * 2

  elif total < d_total:
    print(f''''
============================================
  Dealer won with {d_total}!
  
  You had {total}!
============================================
  ''')
    return 0

  elif total == d_total:
    print(f'''
============================================
  Push, you both tied with {total} and {d_total}!
============================================
  ''')
    return bet

def dice_game(bet):
  dice = []
  num = [1, 2, 3, 4, 5, 6]
  for n in num:
    for d in num:
      dice.append(f'{n} and {d}: {n + d}')
  r.shuffle(dice)
  winner = r.choice(dice)
  dice_roll = r.choice(dice)
  total = dice_roll.split()[3]
  if int(total) == 2:
    print('You got rolled snake eyes (2)')
  else:
    print(f'You rolled a {dice_roll}')
  if dice_roll == winner:
    print(f'''
====================================
              You won!
====================================
    ''')
    return bet * 2
  else:
    print(f'''
=====================================
  You lost, roll needed {winner}
=====================================
    ''')
    return 0

def rps(bet):
  choices = ['rock', 'paper', 'scissors']
  player_win = 0
  cpu_win = 0
  print('''
=====================================
  Welcome to Rock, Paper, Scissors!

      Classic game, best 2/3
=====================================
''')

  while player_win < 2 and cpu_win < 2:
    cpu_choice = r.choice(choices)
    choice = input('rock, paper, scissors, SHOOT!')
    if choice == cpu_choice:
      print('tie')
    elif choice == 'rock' and cpu_choice == 'scissors':
      print('Player wins!')
      player_win += 1
    elif choice == 'paper' and cpu_choice == 'rock':
      print('Player wins!')
      player_win += 1
    elif choice == 'scissors' and cpu_choice == 'paper':
      print('Player wins!')
      player_win += 1
    else:
      print('CPU wins!')
      cpu_win += 1
  if player_win == 2:
    print(f'Player won! Score {player_win}/{cpu_win}')
    return bet * 2
  elif cpu_win == 2:
    print(f'CPU won! Score {player_win}/{cpu_win}')
    return 0