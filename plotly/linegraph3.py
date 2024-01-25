import plotly.graph_objects as go

x1,y1=[1,2,3,4,5],[6,4,0,3,1]
x2,y2=[8,2,4,6,3],[5,8,1,6,9]
x3,y3=[8,2,1,5,4],[4,6,8,2,1]

fig=go.Figure()

fig.add_trace(go.Scatter(x=x1,y=y1,name="line1",mode="lines"))
fig.add_trace(go.Scatter(x=x2,y=y2,name="line2",mode="markers"))
fig.add_trace(go.Scatter(x=x3,y=y3,name="line3",mode="lines+markers"))

fig.show()