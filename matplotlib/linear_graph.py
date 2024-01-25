import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[5,6,7,8]
# c='r' to gives color
plt.plot(x,y,marker='.')
plt.plot(y,marker='>')
plt.plot(x,marker='o')
plt.show()