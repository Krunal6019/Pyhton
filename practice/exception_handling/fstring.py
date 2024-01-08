first_name="Krunal"
last_name="rathod"

sentence='My name is {} {}.'.format(first_name,last_name)
print(sentence)

sentence=f"I'm {last_name.title()} {first_name} "
print(sentence)

person={'name':'jeff','age':19}
sentence="My name is {},I'm {}".format(person['name'],person['age'])
print(sentence)

sentence=f"Heyy!, {person['name']} here and i'm {person['age']}"
print(sentence)

calculation=f'4 times 11 is eqaula to {4*11}'
print(calculation)

for n in range(1,11):
    x=f'{n}'
    print(x)

pi=3.14159265
sentence=f"value of pi is {pi}"
print(sentence)

from datetime import datetime
birthdate=datetime(1990,1,1)
sentence=f'Jehnn has bday on {birthdate:%B %d,%Y}'
print(sentence)