from datetime import date
year = int(input('\nYear: '))
print(20 * '=')
if year == 0:
   year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
   print("{} is a leep year!!".format(year))
else:
   print("{} isn't a leap year".format(year))
