import plotly.express as px

x=[1,2,3,4,5,6,7,8,9]
y=[9,8,7,6,5,4,3,2,1]

fig=px.line(x=x,y=y,title="line graph")
fig.show()
