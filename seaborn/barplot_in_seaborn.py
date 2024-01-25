import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# df=sns.get_dataset_names()
df=sns.load_dataset('penguins')
# sns.barplot(x=df.island,y=df.bill_length_mm)
# sns.barplot(x="island",y="bill_length_mm",data=df,hue="sex") #categorical data
order1=["Dream","Torgersen","Biscoe"]
# sns.barplot(x="island",y="bill_length_mm",data=df,hue="sex",order=order1,hue_order=['Female','Male']) #orders
# sns.barplot(x="island",y="bill_length_mm",data=df,hue="sex",order=order1,hue_order=['Female','Male'],color="black") #colors for bars
sns.barplot(x="island",y="bill_length_mm",data=df,hue="sex",order=order1,hue_order=['Female','Male'],palette="prism",saturation=0.08) #colors according to hue
plt.show()
