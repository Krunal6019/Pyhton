import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[5,6,7,8]

plt.title("Scatter")
plt.xlabel('month')
plt.ylabel('number')
plt.scatter(x,y,s=150)
plt.show()