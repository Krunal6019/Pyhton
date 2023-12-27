# num1='100'
# num2='200'

# print(num1+num2)

# num1=int(num1)
# num2=int(num2)

# print(num1+num2)

# # array or list

course=['history','math','physics','compsci']

for i in range(1,3):
        print(course[i])

# for index,course in enumerate(course):
#         print(index,course)
        
        
        
# #Sets

# cs_course={'history','math','physics','compisci','math'}

# print(cs_course )

k='py'

if k=='y':
    print("ok")
else:
    print(k)        
    
    #there is no switch case in python

#false values:
#false
#none
#zero
#any empty sequence ,' ',(),[]
#any empty mapping,{}.

condition={}

if condition:
    print('trueee')

else:
    print('falsee')


nums=[1,2,3,4]

for num in nums:
    for letter in 'abc':
        print(num,letter)


# for i in range(1,11):
#     print(i)


x=0

while x<10:
    print(x)
    x+=1