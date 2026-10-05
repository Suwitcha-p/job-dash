import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Mock Dataframes for Supply & Demand
df_supply = pd.DataFrame({
    'academic_year': [2021, 2022, 2023, 2024] * 2,
    'program_name': ['Data Science'] * 4 + ['AI Engineering'] * 4,
    'graduates_count': [45, 55, 70, 90, 30, 40, 60, 85],
    'tuition_fee_total': [160000] * 8
})

df_demand = pd.DataFrame({
    'job_level': ['Entry', 'Mid', 'Senior', 'Executive'],
    'avg_salary': [67500, 115000, 185000, 260000]
})

app = dash.Dash(__name__, external_stylesheets=['https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css'])
app.title = "AI & DS Market Dashboard Engine"

app.layout = html.Div([
    html.H2("AI & Data Science Dashboard (Backend Engine)", className="p-3 text-primary"),
    dcc.Tabs([
        dcc.Tab(label='1. Academic Supply Side', children=[
            dcc.Graph(id='graph-graduates', figure=px.bar(df_supply, x='academic_year', y='graduates_count', color='program_name', barmode='group', title="Graduates Count by Program"))
        ]),
        dcc.Tab(label='2. Market Demand Side', children=[
            dcc.Graph(id='graph-salary', figure=px.bar(df_demand, x='job_level', y='avg_salary', title="Salary by Experience Level (USD)"))
        ]),
        dcc.Tab(label='3. Skill Mismatch Analysis', children=[
            html.Div([html.P("Skill Mismatch Radar Chart Placeholder")], className="p-4")
        ])
    ])
], className="container my-4")

if __name__ == '__main__':
    app.run_server(debug=True)
