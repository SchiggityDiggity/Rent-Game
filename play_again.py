import random as r

def again():
  restart = input('Play again: y/n ').lower()
  if restart == 'y':
    print('Let it ride!')
    return True
  else:
    print('Thanks for playing!')
    return False

def odds():
  list_of_chances = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.99]
  final_chance = r.choice(list_of_chances)
  player_chance = round(r.uniform(0, 1.0), 1)
  if player_chance <= final_chance:
    print(f"""You managed to convinced your landlord
to wait until next month! Odds to beat: {final_chance}.  
    """)
    pay_rent = False
  else:
    print(f"""You failed to convince your landlord,
you must pay rent! Odds to beat: {final_chance}.  
    """)
    pay_rent = True
  return pay_rent