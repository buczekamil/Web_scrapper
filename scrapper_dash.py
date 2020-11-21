import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt


df = pd.read_csv('main_output.csv')
# df.describe()
#                                             # CRUDE WTI to differ
# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(x=df['Date'], y=df['Words differ'], name="Words differ"),
    secondary_y=False,)
fig.add_trace(
    go.Scatter(x=df['Date'], y=df['CRUDE WTI'], name="Crude WTI"),
    secondary_y=True,)
#
# Add figure title
fig.update_layout(
    title_text="Words differ to CRUDE WTI price"
)

# Set x-axis title
fig.update_xaxes(title_text="Date")

# Set y-axes titles
fig.update_yaxes(title_text="Words differ", secondary_y=False)
fig.update_yaxes(title_text="CRUDE WTI", secondary_y=True)

fig.show()

#
#                                 # BRENT CRUDE to differ

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(x=df['Date'], y=df['Words differ'], name="Words differ"),
    secondary_y=False,)
fig.add_trace(
    go.Scatter(x=df['Date'], y=df['BRENT CRUDE'], name="Brent Crude"),
    secondary_y=True,)

# Add figure title
fig.update_layout(
    title_text="Words differ to Brent CRUDE price"
)

# Set x-axis title
fig.update_xaxes(title_text="Date")

# Set y-axes titles
fig.update_yaxes(title_text="Words differ", secondary_y=False)
fig.update_yaxes(title_text="BRENT CRUDE", secondary_y=True)

fig.show()
#
#
#                                 # Positive words to BRENT CRUDE
#
# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(x=df['Date'], y=df['Positive words'], name="Positive words"),
    secondary_y=False,)
fig.add_trace(
    go.Scatter(x=df['Date'], y=df['BRENT CRUDE'], name="Brent Crude"),
    secondary_y=True,)

# Add figure title
fig.update_layout(
    title_text="Positive words to Brent CRUDE price"
)

# Set x-axis title
fig.update_xaxes(title_text="Date")

# Set y-axes titles
fig.update_yaxes(title_text="Positive words count", secondary_y=False)
fig.update_yaxes(title_text="BRENT CRUDE", secondary_y=True)

fig.show()
#
#                                 # Negative words to BRENT CRUDE

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(x=df['Date'], y=df['Negative words'], name="Negative words"),
    secondary_y=False,)
fig.add_trace(
    go.Scatter(x=df['Date'], y=df['BRENT CRUDE'], name="Brent Crude"),
    secondary_y=True,)

# Add figure title
fig.update_layout(
    title_text="Positive words to Brent CRUDE price"
)

# Set x-axis title
fig.update_xaxes(title_text="Date")

# Set y-axes titles
fig.update_yaxes(title_text="Negative words count", secondary_y=False)
fig.update_yaxes(title_text="BRENT CRUDE", secondary_y=True)

fig.show()


plt.plot(df['Date'], df['Words differ'], label='Words differ')
plt.plot(df['Date'], df['CRUDE WTI'], label='Crude WTI')
plt.plot(df['Date'], df['BRENT CRUDE'], label='Brent Crude')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('random')
plt.grid(True)
plt.legend()
plt.show()

fig, axes = plt.subplots(6,1)
axes[0].hist(df['Words differ'])
axes[1].plot(df['Date'], df['Positive words'])
axes[2].plot(df['Date'], df['Negative words'])
axes[3].plot(df['Date'], df['CRUDE WTI'])
axes[4].plot(df['Date'], df['BRENT CRUDE'])
axes[5].plot(df['Date'], df['NATURAL OIL'])
fig.show()