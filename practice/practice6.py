#Comprehensions

nums=[1,2,3,4,5,6,7,8,9,10]

#1 
my_list=[]
for n in nums:
    my_list.append(n)
# print( my_list)

my_list=[n for n in nums]   #Comprehensions
# print(my_list)

#2
# my_list=filter(n%2==0,nums)
# print(my_list)

#3
my_list=[]
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))

# print(my_list)


my_list=[(letter,num) for letter in 'abcd' for num in range(4)]
# print(my_list)

#4
names=['Bruces','Clark','Peter','Logan','Wade']
heros=['Batman','Superman','Spiderman','Wolverine','Deadpole']
x = zip(names,heros)
print(tuple(x))

#5 dictonary comprehencive
# my_dict={}
# for name,hero in zip(names,heros):
#     my_dict[name]=hero

# print(my_dict)

# my_dict={name:hero for name,hero in zip (names,heros) if name !='Peter'}
# print(my_dict)

#6 set comprehencive
nums=[1,1,1,2,2,3,3,3,4,5,6,6,7]
# print(nums)
my_set=set()
for n in nums:
    my_set.add(n)   
print(my_set)

my_set={n for n in my_set}
print(my_set)
