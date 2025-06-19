import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')


#Print first 10 lines
print ("First 10 rows:\n", df.head(10))

#Print last 10 lines
print ("Last 10 rows:\n", df.tail(10))

#Clean the data. You need to convert the 'strength' column to a float. Use of str.replace() with regex is one way to do this, followed by type conversion.
df['strength'] = df['strength'].str.replace(r'[^\d.]', '', regex=True).astype(float)



#Create an interactive scatter plot of strength vs. frequency, with colors based on the direction.
fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title='Wind Strength vs Frequency by Direction',
    labels={"strength": "Wind Strength", "frequency":"Frequency"}   
)


#Save and load the HTML file, as wind.html. Verify that the plot works correctly
fig.write_html("wind.html", auto_open=True)