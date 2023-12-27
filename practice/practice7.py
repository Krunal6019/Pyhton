# Sorting Lists, Tuples, and Objects

#lists
li=[9,1,8,2,6,3,4]

s_li=sorted(li)
# li.sort() ///////////////sort function is suitable to list only
print('Orignal Variable:\t',li)
print('Sorted Variable:\t',s_li)
#in decending order
s_li=sorted(li,reverse=True)
print('Sorted decending :\t',s_li)


#tuples
tup=(9,1,8,2,6,3,4)
s_tup=sorted(tup)
print('Tuple\t',s_tup)

#dictnory

di={'name':'Corey','job':'programing','age':None,'os':'Windows'}
s_di=sorted(di)
print('Dict \t',s_di) #do sortings according to keyssss
#////

li=[-6,-5,-4,1,2,3] 
s_li=sorted(li)
print(s_li)

s_li=sorted(li,key=abs)
print(s_li)


#objects of class

class Employee():
    def __init__(self,name,age,salary):
        self.name=name 
        self.age=age
        self.salary=salary
        
    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)

e1=Employee('Carl',37,70000)
e2=Employee('Sarah',29,85000)
e3=Employee('John',42,90000)

employees=[e1,e2,e3]

def e_sort(emp):
    return emp.age

s_employees=sorted(employees,key=e_sort)

print(s_employees)
        
        