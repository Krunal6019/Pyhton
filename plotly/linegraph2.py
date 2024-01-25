import plotly.graph_objects as go

x=[5,8,2,1,3,6]
y=[4,5,1,3,6,8]

fig=go.Figure(go.Scatter(x=x,y=y))
fig.update_layout(title="Line graph",xaxis_title="x-axis",yaxis_title="y-axis")
fig.show()