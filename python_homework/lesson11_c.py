from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load gapminder data
gapminder = px.data.gapminder()
countries = sorted(gapminder['country'].unique())

# Initialize Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in countries],
        value="Canada",
        clearable=False
    ),
    dcc.Graph(id="gdp-growth")
])

# Callback for dynamic updates
@app.callback(
    Output("gdp-growth", "figure"),
    Input("country-dropdown", "value")
)
def update_graph(selected_country):
    filtered_df = gapminder[gapminder['country'] == selected_country]
    fig = px.line(
        filtered_df,
        x='year',
        y='gdpPercap',
        title=f"GDP Per Capita Over Time for {selected_country}"
    )
    fig.update_layout(xaxis_title="Year", yaxis_title="GDP Per Capita")
    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)