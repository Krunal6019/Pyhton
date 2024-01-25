#Pandas is python library used for working with data sets.
import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(df,'\n')

print(df.columns,'\n')#print columns

print(df.head(),'\n') #top five

print(df.head(10),'\n') 

print(df.tail(),'\n')#bottom five

print(df.dtypes,'\n')#datatypes

print(df.describe(),'\n')#mean,count,min,max,std,25%,50%,75%

print(df[['Name','Sex','Ticket','Cabin','Embarked']],'\n') #selecs perticular columns

print(df.dtypes=='object','\n')#check colums datatype and result are true or false

print(df.dtypes=='float64','\n')#check colums datatype and result are true or false

print(df[df.dtypes[df.dtypes=='float64'].index],'\n') #select perticular types of  data with index

print(df[df.dtypes[df.dtypes=='int64'].index],'\n') #select perticular types of     data with index

print(df[['Ticket']],'\n') #selects single column

print(df[['Ticket']][4:16],'\n')#slicing

print(df[['Ticket']][4:16:2],'\n')#slicing with jump

print(df[['Ticket','Cabin']],'\n')#slicing

df['new_col']=0 # addnew column with zero value
print(df,'\n')

df.insert(loc=3,column='food',value='samosa')#insert column with dezired index
print(df,'\n')


