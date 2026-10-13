import random as r
import time as t
#TWIH STREAMING (CHOICE 2)
def twih_stream(budget):
  twih_inventory = {}
  twih_inventory['Fartknite'] = 2.5
  twih_inventory['Amongoose'] = 1.3
  twih_inventory['Call of Dude-E'] = 1.5
  twih_inventory['Mimcraft'] = 1.9
  twih_inventory['GTV5'] = 2.2
  twih_inventory['REPOH'] = 1.4
  twih_inventory['Ape-X Legends'] = 1.6
  twih_inventory['Roglox'] = 1.2
  twih_inventory['Phasmo-Boebia'] = 1.8
  twih_inventory['Lethal Business'] = 1.9
  twih_inventory['Fall Dudes'] = 1.3
  twih_inventory["Elder's Ring"] = 2.3
  twih_inventory['Supersonic Acrobatic Rocket-Powered Battle-Cars'] = 2.0
  twih_inventory['Counter-Hit'] = 2.1
  twih_inventory['Only Above'] = 1.4
  twih_games = list(twih_inventory.keys())
  games = r.sample(twih_games, 3)
  print(f'1.{games[0]}: {twih_inventory[games[0]]}')
  print(f'2.{games[1]}: {twih_inventory[games[1]]}')
  print(f'3.{games[2]}: {twih_inventory[games[2]]}')
  sub_tiers = [6, 10, 25]
  stream_cash = 0
  subs = 0
  viewers = 14
  stream = input('What do you choose to stream? ')
  if stream == '1':
    stream_game = games[0]
    game_money = twih_inventory[games[0]]
    print(f'WE STREAMING {stream_game}, current viewers {viewers}!')
  elif stream == '2':
    stream_game = games[1]
    game_money = twih_inventory[games[1]]
    print(f'WE STREAMING {stream_game}, current viewers {viewers}!')
  elif stream == '3':
    stream_game = games[2]
    game_money = twih_inventory[games[2]]
    print(f'WE STREAMING {stream_game}, current viewers {viewers}!')
  event = r.randint(1, 6)
  if event == 1:
    raid_party = r.randint(1, 15)
    viewers += raid_party
    print(f'''
=========================================
    
    YOU GOT RAIDED WITH {raid_party}!
    
    CURRENT VIEWERS {viewers}
    
=========================================
    ''')
  elif event == 2:
    hype_multiplier = r.randint(2, 4)
    print(f'''


=========================================

HYPE TRAIN INCOMING! HYPE TRAIN INCOMING!

=========================================
    
    
    ''')
    t.sleep(3)
    for hype in range(hype_multiplier):
      t.sleep(2.7)
      print(f'''



=========================================

        LEVEL {hype + 1} COMPLETE!!

=========================================



      ''')
  total_subs = r.randint(1, viewers)
  for subs in range(total_subs):
    sub_cash = r.choice(sub_tiers)
    stream_cash += sub_cash
  if event == 2:
    total_made = int(stream_cash * game_money * hype_multiplier)
  else:
    total_made = int(stream_cash * game_money)
  t.sleep(4)
  print(f'\n\nGreat stream! You streamed {stream_game}, you got {total_subs} subs and earned ${total_made}!')
  budget += total_made
  return budget
  
#PRAY 2 GODS (CHOICE 3)
def pray2gods(budget, goal, energy, day, energy_drink):
  zeus = False
  events = ['Nothing',
            'DoubleM',
            'HalfM',
            'Nothing',
            'Sleep',
            'Zeus',
            'Nothing',
            '100 Dollars',
            'Energy Drink',
            'Extra day',
            'Double Rent',
            'Nothing',
            'Half Rent',
            'Energy Refill',
            'Taxes'
           ]
  fate = r.choice(events)
  if fate == 'Nothing':
    print('Nothing happened...')
  elif fate == 'DoubleM':
    print('Your money doubled!')
    budget *= 2
  elif fate == 'HalfM':
    print('You lost half of your money...')
    budget = int(budget / 2)
  elif fate == 'Sleep':
    print('You pass out and lose a day...')
    day += 1
    energy = 3
    has_prayed = False
  elif fate == 'Zeus':
    print("You hear a static noise...\nYour hair starts sticking up...\nYou see a flash...it's over.")
    # MAKE A zeus = FALSE, then if this happens zeus = True
    zeus = True
    #play_game = False
  elif fate == '100 Dollars':
    print('Lucky you! You found 100 dollars!')
    budget += 100
  elif fate == 'Energy Drink':
    print('You found an energy drink')
    energy_drink += 1
  elif fate == 'Extra day':
    print('You gained an extra day!')
    day -= 1
  elif fate == 'Double Rent':
    print('Rent doubled...')
    goal = int(goal * 2)
  elif fate == 'Half Rent':
    print('Rent was cut in half!')
    goal = goal // 2
  elif fate == 'Energy Refill':
    print('You feel energized')
    energy += 2
  elif fate == 'Taxes':
    print('You gotta pay taxes...')
    taxes = abs(int(budget * 0.20))
    budget -= taxes
  return budget, goal, energy, day, energy_drink, zeus


#ASK FOR $$$ FROM PARENTS (CHOICE 4)
def ask_4_money(budget, rounds_won):
  max_money = 300 + (rounds_won * 125)
  money_recieved = r.randint(1, max_money)
  fifty_fifty = r.choice(['yes', 'no'])
  if fifty_fifty == 'yes':
    print(f'Your parents gave you {money_recieved}!')
    budget += money_recieved
  else:
    print('Your parents refused to give you money.')
  return budget

