#part2
import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(df,'\n')

a=df['Name'][0:10] #a=df['Name'].head(10) another way
print(a,'\n') #slicicng in purticular column
print(type(a),'\n')

#set dezired index
l=['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10']
print(pd.Series(a,index=l),'\n')
print(pd.Series(list(a),index=l),'\n')

m1=pd.Series([100,200,300,400,500],index=[1,2,3,4,5])
print(m1,'\n')
m2=pd.Series([600,700,800,900,1000],index=[1,2,3,4,5])
print(m2,'\n')
m3=pd.concat([m1,m2])
print(m3,'\n')
print(m3[1],'\n')
print(m1+m2,'\n')
print(m1*m2,'\n')
print(df,'\n')

#delete column
print(df.drop('PassengerId',axis=1),'\n')
print(df,'\n') #not permenent deleted
print(df.drop('PassengerId',axis=1,inplace=True),'\n')
print(df,'\n') # permenent deleted

#delete row
print(df.drop(3),'\n')#not permenent deleted
print(df.drop(3,inplace=True),'\n')#not permenent deleted
print(df,'\n')  

#set column to index
i=df.set_index('Name') #not permenantalyyyyyyy
print(i,'\n')
# df.set_index('Name',inplace=True) # permenantalyyyyyyy
print(df)
print(df.reset_index())

