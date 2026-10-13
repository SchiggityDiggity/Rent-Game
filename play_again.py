def again():
  restart = input('Play again: y/n ').lower()
  if restart == 'y':
    print('Let it ride!')
    return True
  else:
    print('Thanks for playing!')
    return False