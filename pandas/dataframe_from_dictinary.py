import pandas as pd
#dictinary
d={
    "key1":[1,2,3,4,5],
    "key2":[6,7,8,9,10],
    "key3":[11,12,13,14,15]
}
print(d)
#dataframe
x=pd.DataFrame(d)
print(x)

df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df1=df.dropna() #not permentalyy,delete that rows who has nan values
print(df1,'\n')
#in column
print(df)
# df2=df.dropna(axis=0) also for rows
df2=df.dropna(axis=1)
print(df2)
#fill na with some value
df3=df.fillna('K9')
print(df3)