x = input('Digite qualquer coisa: ')
print(' O número digitado é {}. \n São só espaços? {}. \n São só números? {}. \n Há apenas letras? {}. \n É um mix de letras e números? {}. \n Está em letras minúsculas? {}. \n Está em letras maiúsculas? {}.'.format(type(x), x.isspace(), x.isnumeric(), x.isalpha(), x.isalnum(), x.islower(), x.isupper(),))


