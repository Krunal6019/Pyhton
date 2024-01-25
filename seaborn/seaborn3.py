import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv").head(100)

sns.lineplot(x="PassengerId",y="Cabin",data=df,hue="Pclass",style="Survived",markers=["o","^"])
plt.grid()
plt.show()

#PassengerId  Survived 
    