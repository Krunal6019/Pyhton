from collections import namedtuple

# color={'red':55,'green':155,'blue':255}
# print(color['red'])

Color=namedtuple('Color',['red','green','blue'])
color=Color(55,155,255)
print(color[1])
print(color.red)

white=Color(255,255,255)
print(white.green)

dict_color={'red':55,'green':155,'blue':125}
print (dict_color['green'])