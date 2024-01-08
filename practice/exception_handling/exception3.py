#Duck Typing and Asking Forgiveness, Not Permission (EAFP)
class Duck:
    
    def quack(self):
        print("Quack!,quack")

    def fly(self):
        print("Flap!,flap")

class Person:
    
    def quack(self):
        print("I'm quacking like a duck")

    def fly(self):
        print("I'm fly like duck")

def quack_and_fly(thing):

    if isinstance(thing,Duck):
        thing.quack()
        thing.fly()
    else:
        print('This has to be duck!')

    print()

d=Duck()
quack_and_fly(d)

p=Person()
quack_and_fly(p)
p.fly()