from emoji import emojize
name = str(input('Type your name: ')).strip().upper()

if name == 'VICTOR':
   print('Xii! {}{}{} is a common name!!!'.format('\033[1;35m', name.capitalize(), '\033[m'))
elif name == 'JONAS':
   print(emojize('I hate the name {}{}{} :angry::angry:!!!'.format('\033[7;33;41m', name.capitalize(), '\033[m'), use_aliases=True))
else:
   print("Ok, I don't problem with the name {}{}{}".format('\033[0;30;45m', name.capitalize(), '\033[m'))
