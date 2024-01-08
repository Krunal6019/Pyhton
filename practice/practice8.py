#String Formating Advance Operations for Dicts,List,Numbers and Dates

#example1  sentence1
print("example1")   
person={'name':'Krunal','age':20}

sentence1=' 1 My name is '+person['name']+' and I am '+str(person['age'])+ ' years old.'

print(sentence1)

sentence2=' 2 My name is {} and I am {} years old.'.format(person['name'],person['age'])
print(sentence2)

sentence3=' 3 My name is {0} and I am {1} years old.'.format(person['name'],person['age'])
print(sentence3)

sentence4=' 4 My name is {0[name]} and I am {1[age]} years old.'.format(person,person)
print(sentence4)

sentence5=' 5 My name is {name} and I am {age} years old.'.format(name='Tanay',age='10')
print(sentence5)

sentence6=' 6 My name is {name} and I am {age} years old.'.format(**person)
print(sentence6)
print("\n")

#example2 sentence 2
print("example2")
tag='h1'
text='This is header'

example2='<{0}>{1}</0>'.format(tag,text)
print(example2)
print("\n")

#example3
print("example3")
for i in range(1,11):
    example3='The value is {0:02}'.format(i)
    print(example3)
print("\n")
  
#example4
print("example4")
pi=3.14159265
example4='Pi is equal to {:.2f}'.format(pi)
print(example4)
print("\n")

#example5
print("example5")
example5='1 MB is equal to {:,.2f} bytes '.format(1000**2)
print(example5)
print("\n")
#example6
print("example6")

import datetime
my_date=datetime.datetime(2023,12,29,22,45,36)
print(my_date)

my_date='{:%B %d,%Y}'.format(my_date)
print(my_date)

my_date=datetime.datetime(2023,12,29,22,45,36)
my_date="{0:%B %d,%Y} fell on a {0:%A} and was the {0:%j} day of the year".format(my_date)
print(my_date)

