def coffee_bot():
  print('Welcome to the cafe!')
  size = get_size()
  drink_type = get_drink_type()
  print('Alright, that\'s a ' + size + ' ' + drink_type)  
  name = input('can I get your name please? \n')
  print('Thanks, ' + name + '! Your drink will be ready shortly.')

def get_size():
  print()
  print("type the letters a/b/c instead of small/medium/large")
  print()
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else: 
    print_message()
    return get_size() #this is a recursive function call, calling a function in itself

def print_message():
  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

def get_drink_type():
  res = input("what type of drink would you like?\n[a] brewed coffee\n[b] mocha\n[c] latte \n")
  if res =='a':
    return order_brewed_coffee()
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type() # another recursive function call

def order_latte():
  res = input('and what kind of milk for your latte? \n [a] 2% milk \n [b] non-fat milk \n [c] soy milk \n [d] almond milk \n')    
  if res == 'a':
    return 'regular latte'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  elif res == 'd':
    return 'almond latte'
  else:
    print_message()
    return order_latte() # another recursive function call

def order_brewed_coffee():
  res = input('and what kind brewed coffee? \n [a] Machine Espresso \n [b] Stovetop espresso \n [c] Aeropress \n [d] French Press \n')    
  if res == 'a':
    return 'machine espresso'
  elif res == 'b':
    return 'Stovetop espresso'
  elif res == 'c':
    return 'Aeropress'
  elif res == 'd':
    return 'French Press'
  else:
    print_message()
    return order_brewed_coffee() # another recursive function call

def order_mocha():
  res = input('and what kind of chocolate for your mocha? \n [a] white chocolate \n [b] milk and/or dark chocolate \n')    
  if res == 'a':
    return 'white caffè mocha'
  elif res == 'b':
    return 'Caffè mocha'
  else:
    print_message()
    return order_mocha() # another recursive function call

coffee_bot()