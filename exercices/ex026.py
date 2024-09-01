sentence = str(input('\nWrite your sentence: ')).upper()
na = sentence.strip().count('A')
print(20*'-')
print('1.This sentene has {} letter(s) "a". '.format(na))
print('2.The first letter "a" shows in {}º position.'.format(sentence.find('A')))
print('3.The last letter "a" shows in {}º position.'.format(sentence.rfind('A')))


