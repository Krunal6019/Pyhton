import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df=sns.load_dataset('penguins')
# sns.displot(df["flipper_length_mm"])
# sns.displot(df["flipper_length_mm"],bins=[170,180,190,200,210,220,230]) #bins is gaps between bars
sns.displot(df["flipper_length_mm"],bins=[170,180,190,200,210,220,230],kde=True) #A kernel density estimate (KDE) plot is a method for visualizing the distribution of observations in a dataset, analogous to a histogram.
plt.show()