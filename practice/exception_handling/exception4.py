#Duck Typing and Asking Forgiveness, Not Permission (EAFP)

person1={'name':'Jack','age':103,'job':'artist'}
person2={'name':'Jack','age':103}


try:
    print("I'm {name}. My age{age}.I am {job}".format(**person1))
    print("I'm {name}. My age{age}.I am {job}".format(**person2))

except KeyError as e:
    print("Missing {} key".format(e))

