#horizontal bbar graph
import matplotlib.pyplot as plt
import numpy as np

x=np.array(['A','B','C','D'])
y=np.array([3,8,1,10])

plt.barh(x,y) #width,height params
plt.show()