#use of random module
import random

value=random.random()
print(value)

value=random.randint(1,10)
print(value)

value=random.uniform(1,10)
print(value)

greetings=['hy','hello','how are you?']
value=random.choice(greetings)
print(value)
print(value+',Krunal')

colors=['Red','White','Black','Purple']
value=random.choices(colors)
print(value)
value=random.choices(colors,k=5)
print(value)
value=random.choices(colors,weights=[5,6,7,2],k=5)
print(value)

deck=list(range(1,53))
print(deck)
print("")
random.shuffle(deck)
print(deck) 
print("")
hand=random.sample(deck,k=5)
print(hand)