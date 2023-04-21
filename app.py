import os
import numpy as np
import pandas as pd
import plotly.io as pio
import dash  # !pip install dash
from dash import Dash, dcc
from dash import html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
from jupyter_dash import JupyterDash

df = pd.read_excel(r"data\Ecoshoe results raw new.xlsx")
materials_df = pd.read_excel(r"data\Materials.xlsx")

color_map = {
    'Traditional':'rgb(102,102,102)',
    'Design for use of Recycled Material ':'rgb(55,126,184)',
    'Design for use of Healthy Material ':'rgb(47,178,139)'
}

Materials_color_map={
#                      Traditional materials: Grey
    'Conventional cotton':'rgb(32,32,32)',
    'Wool':'rgb(52,52,52)',
    'Nylon':'rgb(72,72,72)',
    'Polyester':'rgb(102,102,102)',
    'EVA':'rgb(132,132,132)',
    'Rubber':'rgb(162,162,162)',
    'Chrome tanned leather':'rgb(192,192,192)',
#    Healthy materials: Green
    'Cork':'rgb(7,138,99)',
    'Vegetable tanned leather':'rgb(17,148,109)',
    'Organic cotton':'rgb(27,158,119)',
    'Certified leather':'rgb(37,168,129)',
    'Kenaf':'rgb(47,178,139)',
    'Lyocell':'rgb(57,188,149)',
    'Jute':'rgb(77,208,169)',
    'Viscose':'rgb(97,228,189)',
    'Hemp':'rgb(117,248,209)',
#    Recycled materials: blue
    'Econyl':'rgb(15,86,144)',
    'Recycled cotton':'rgb(35,106,164)',
    'Recycled rubber':'rgb(55,126,184)',
    'Recycled wool':'rgb(75,146,204)',
    'Recycled polyester':'rgb(95,166,224)'
}

app = Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])  # , external_stylesheets=external_stylesheets)
server = app.server

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('ECOSHOE Dashboard', style={'textAlign': 'center'}),
        ], width=12)
    ]),

    dbc.Row([
        dbc.Col([
            html.Label('Impact category'),
            dcc.Dropdown(id='imp_cat',
                         options=[{'label': x, 'value': x} for x in
                                  df['Impact category'].unique()],
                         # assegna al menù gli impact category riportate nella tabella, value è quello che voglio vedere nel menù a tendina
                         placeholder="Select the impact category to visualize",
                         # multi=False, # per avere un solo valore selezionabile
                         clearable=False  # in modo da non avere valore vuoto
                         # style={'width':"50%"} # larghezza del menù
                         ),
        ], width=6)
    ], justify="center"),

    # UPPER
    dbc.Row([
        dbc.Col([
            html.Label('Traditional material use for the upper'),
            dcc.Dropdown(id='upp1',
                         options=[{'label': x, 'value': x} for x in
                                  materials_df['Upper_t'].dropna().unique()],
                         # assegna al menù gli impact category riportate nella tabella, value è quello che voglio vedere nel menù a tendina
                         placeholder="Select material for the UPPER",
                         # multi=False, # per avere un solo valore selezionabile
                         clearable=False
                         ),
        ], width=4),

        dbc.Col([
            html.Label('Weight [kg]:'),
            dcc.Input(id='wupp1',
                      type='number',
                      min=0,
                      max=1,
                      # step=0.1
                      ),
        ], width=2),

        dbc.Col([
            html.Label('Alternative material for the upper'),
            dcc.Dropdown(id='upp2',
                         options=[{'label': x, 'value': x} for x in
                                  materials_df['Upper_a'].dropna().unique()],
                         # assegna al menù gli impact category riportate nella tabella, value è quello che voglio vedere nel menù a tendina
                         placeholder="Select material for the UPPER",
                         # multi=False, # per avere un solo valore selezionabile
                         clearable=False
                         ),
        ], width=4),

        dbc.Col([
            html.Label('Weight [kg]:'),
            dcc.Input(id='wupp2',
                      type='number',
                      min=0,
                      max=1,
                      # step=0.1
                      ),
        ], width=2)

    ], justify="center"),

    # LINER
    dbc.Row([
        dbc.Col([
            html.Label('Traditional material use for the liner'),
            dcc.Dropdown(id='lin1',
                         options=[{'label': x, 'value': x} for x in
                                  materials_df['Liner_t'].dropna().unique()],
                         # assegna al menù gli impact category riportate nella tabella, value è quello che voglio vedere nel menù a tendina
                         placeholder="Select material for the LINER",
                         # multi=False, # per avere un solo valore selezionabile
                         clearable=False
                         ),
        ], width=4),

        dbc.Col([
            html.Label('Weight [kg]:'),
            dcc.Input(id='wlin1',
                      type='number',
                      min=0,
                      max=1,
                      # step=0.1
                      ),
        ], width=2),

        dbc.Col([
            html.Label('Alternative material for the liner'),
            dcc.Dropdown(id='lin2',
                         options=[{'label': x, 'value': x} for x in
                                  materials_df['Liner_a'].dropna().unique()],
                         # assegna al menù gli impact category riportate nella tabella, value è quello che voglio vedere nel menù a tendina
                         placeholder="Select material for the LINER",
                         # multi=False, # per avere un solo valore selezionabile
                         clearable=False
                         ),
        ], width=4),

        dbc.Col([
            html.Label('Weight [kg]:'),
            dcc.Input(id='wlin2',
                      type='number',
                      min=0,
                      max=1,
                      # step=0.1
                      ),
        ], width=2)

    ], justify="center"),

    # LACES
    dbc.Row([
        dbc.Col([
            html.Label('Traditional material use for the laces'),
            dcc.Dropdown(id='lac1',
                         options=[{'label': x, 'value': x} for x in
                                  materials_df['Laces_t'].dropna().unique()],
                         # assegna al menù gli impact category riportate nella tabella, value è quello che voglio vedere nel menù a tendina
                         placeholder="Select material for the LACES",
                         # multi=False, # per avere un solo valore selezionabile
                         clearable=False
                         ),
        ], width=4),

        dbc.Col([
            html.Label('Weight [kg]:'),
            dcc.Input(id='wlac1',
                      type='number',
                      min=0,
                      max=1,
                      # step=0.1
                      ),
        ], width=2),

        dbc.Col([
            html.Label('Alternative material for the laces'),
            dcc.Dropdown(id='lac2',
                         options=[{'label': x, 'value': x} for x in
                                  materials_df['Laces_a'].dropna().unique()],
                         # assegna al menù gli impact category riportate nella tabella, value è quello che voglio vedere nel menù a tendina
                         placeholder="Select material for the LACES",
                         # multi=False, # per avere un solo valore selezionabile
                         clearable=False
                         ),
        ], width=4),

        dbc.Col([
            html.Label('Weight [kg]:'),
            dcc.Input(id='wlac2',
                      type='number',
                      min=0,
                      max=1,
                      # step=0.1
                      ),
        ], width=2)

    ], justify="center"),

    # INSOLE
    dbc.Row([
        dbc.Col([
            html.Label('Traditional material use for the insole'),
            dcc.Dropdown(id='ins1',
                         options=[{'label': x, 'value': x} for x in
                                  materials_df['Insole_t'].dropna().unique()],
                         # assegna al menù gli impact category riportate nella tabella, value è quello che voglio vedere nel menù a tendina
                         placeholder="Select material for the INSOLE",
                         # multi=False, # per avere un solo valore selezionabile
                         clearable=False
                         ),
        ], width=4),

        dbc.Col([
            html.Label('Weight [kg]:'),
            dcc.Input(id='wins1',
                      type='number',
                      min=0,
                      max=1,
                      # step=0.1
                      ),
        ], width=2),

        dbc.Col([
            html.Label('Alternative material for the insole'),
            dcc.Dropdown(id='ins2',
                         options=[{'label': x, 'value': x} for x in
                                  materials_df['Insole_a'].dropna().unique()],
                         # assegna al menù gli impact category riportate nella tabella, value è quello che voglio vedere nel menù a tendina
                         placeholder="Select material for the INSOLE",
                         # multi=False, # per avere un solo valore selezionabile
                         clearable=False
                         ),
        ], width=4),

        dbc.Col([
            html.Label('Weight [kg]:'),
            dcc.Input(id='wins2',
                      type='number',
                      min=0,
                      max=1,
                      # step=0.1
                      ),
        ], width=2)

    ], justify="center"),

    # OUTSOLE
    dbc.Row([
        dbc.Col([
            html.Label('Traditional material use for the outsole'),
            dcc.Dropdown(id='out1',
                         options=[{'label': x, 'value': x} for x in
                                  materials_df['Outsole_t'].dropna().unique()],
                         # assegna al menù gli impact category riportate nella tabella, value è quello che voglio vedere nel menù a tendina
                         placeholder="Select material for the OUTSOLE",
                         # multi=False, # per avere un solo valore selezionabile
                         clearable=False
                         ),
        ], width=4),

        dbc.Col([
            html.Label('Weight [kg]:'),
            dcc.Input(id='wout1',
                      type='number',
                      min=0,
                      max=1,
                      # step=0.1
                      ),
        ], width=2),

        dbc.Col([
            html.Label('Alternative material for the insole'),
            dcc.Dropdown(id='out2',
                         options=[{'label': x, 'value': x} for x in
                                  materials_df['Outsole_a'].dropna().unique()],
                         # assegna al menù gli impact category riportate nella tabella, value è quello che voglio vedere nel menù a tendina
                         placeholder="Select material for the OUTSOLE",
                         # multi=False, # per avere un solo valore selezionabile
                         clearable=False
                         ),
        ], width=4),

        dbc.Col([
            html.Label('Weight [kg]:'),
            dcc.Input(id='wout2',
                      type='number',
                      min=0,
                      max=1,
                      # step=0.1
                      ),
        ], width=2)

    ], justify="center"),

    # grafico totale
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='my-graph'),
        ], width=8)
    ], justify="center"),

    #     # Grafico Upper
    #     dbc.Row([
    #         dbc.Col([
    #             # html.Label('Upper'),
    #             dcc.Graph(id='graph-upp'),
    #         ], width=6),
    #     #grafico liner
    #         dbc.Col([
    #             html.Label('Liner'),
    #             dcc.Graph(id='graph-lin'),
    #         ], width=6),

    #     ], justify="center"),

])


@app.callback(  # dove vengono inseriti gli elementi interattivi della dashboard
    Output(component_id='my-graph', component_property='figure'),  #
    [Input(component_id='imp_cat', component_property='value'),
     Input(component_id='upp1', component_property='value'),
     Input(component_id='upp2', component_property='value'),
     Input(component_id='wupp1', component_property='value'),
     Input(component_id='wupp2', component_property='value'),
     Input(component_id='lin1', component_property='value'),
     Input(component_id='lin2', component_property='value'),
     Input(component_id='wlin1', component_property='value'),
     Input(component_id='wlin2', component_property='value'),
     Input(component_id='lac1', component_property='value'),
     Input(component_id='lac2', component_property='value'),
     Input(component_id='wlac1', component_property='value'),
     Input(component_id='wlac2', component_property='value'),
     Input(component_id='ins1', component_property='value'),
     Input(component_id='ins2', component_property='value'),
     Input(component_id='wins1', component_property='value'),
     Input(component_id='wins2', component_property='value'),
     Input(component_id='out1', component_property='value'),
     Input(component_id='out2', component_property='value'),
     Input(component_id='wout1', component_property='value'),
     Input(component_id='wout2', component_property='value')
     ]  # l'utente sceglie il value del menù che andrà a modificare l'output, ovvero my-graph
)
def update_graph(impact_category,
                 upp1, upp2, wupp1, wupp2,
                 lin1, lin2, wlin1, wlin2,
                 lac1, lac2, wlac1, wlac2,
                 ins1, ins2, wins1, wins2,
                 out1, out2, wout1, wout2
                 ):
    df['Component'] = ''
    df['Scenario'] = ''
    dff = df[df['Impact category'] == impact_category]

    # UPPER
    df_upp1 = dff.copy().loc[dff['Materials'] == upp1]
    df_upp1['Impact'] = df_upp1['value'] * wupp1
    df_upp1['Component'] = 'Upper'
    df_upp1['Scenario'] = 'Actual'

    df_upp2 = dff.copy().loc[dff['Materials'] == upp2]
    df_upp2['Impact'] = df_upp2['value'] * wupp2
    df_upp2['Component'] = 'Upper'
    df_upp2['Scenario'] = 'Substitute'

    # LINER
    df_lin1 = dff.copy().loc[dff['Materials'] == lin1]
    df_lin1['Impact'] = df_lin1['value'] * wlin1
    df_lin1['Component'] = 'Liner'
    df_lin1['Scenario'] = 'Actual'

    df_lin2 = dff.copy().loc[dff['Materials'] == lin2]
    df_lin2['Impact'] = df_lin2['value'] * wlin2
    df_lin2['Component'] = 'Liner'
    df_lin2['Scenario'] = 'Substitute'

    # LACES
    df_lac1 = dff.copy().loc[dff['Materials'] == lac1]
    df_lac1['Impact'] = df_lac1['value'] * wlac1
    df_lac1['Component'] = 'Laces'
    df_lac1['Scenario'] = 'Actual'

    df_lac2 = dff.copy().loc[dff['Materials'] == lac2]
    df_lac2['Impact'] = df_lac2['value'] * wlac2
    df_lac2['Component'] = 'Laces'
    df_lac2['Scenario'] = 'Substitute'

    # INSOLE
    df_ins1 = dff.copy().loc[dff['Materials'] == ins1]
    df_ins1['Impact'] = df_ins1['value'] * wins1
    df_ins1['Component'] = 'Insole'
    df_ins1['Scenario'] = 'Actual'

    df_ins2 = dff.copy().loc[dff['Materials'] == ins2]
    df_ins2['Impact'] = df_ins2['value'] * wins2
    df_ins2['Component'] = 'Insole'
    df_ins2['Scenario'] = 'Substitute'

    # OUTSOLE
    df_out1 = dff.copy().loc[dff['Materials'] == out1]
    df_out1['Impact'] = df_out1['value'] * wout1
    df_out1['Component'] = 'Outsole'
    df_out1['Scenario'] = 'Actual'

    df_out2 = dff.copy().loc[dff['Materials'] == out2]
    df_out2['Impact'] = df_out2['value'] * wout2
    df_out2['Component'] = 'Outsole'
    df_out2['Scenario'] = 'Substitute'

    dfff = pd.concat([df_upp1, df_upp2,
                      df_lin1, df_lin2,
                      df_lac1, df_lac2,
                      df_ins1, df_ins2,
                      df_out1, df_out2
                      ])

    fig = px.histogram(data_frame=dfff, x='Scenario', y='Impact', color='Materials',
                       color_discrete_map=Materials_color_map,
                       pattern_shape="Component",
                       template="seaborn",
                       )
    # unit = '[' + dfff['Unit'][0] + ']'
    fig.update_yaxes(matches=None, showticklabels=True, tickformat='.1e', title="", tickfont={'size': 14})
    fig.update_xaxes(matches=None, showticklabels=True, title="", tickfont={'size': 18})
    fig.update_layout(showlegend=False)

    # fig.update_layout(legend=dict(title={'text': '<b>'+'Ecodesign','font' : dict(size=24)}, # armonizzare con indicazioni Eli # br is for line break
    #                           font={'size':22},
    #                           yanchor="top",
    #                           y=-0.05,
    #                           xanchor="center",
    #                           x=0.15,
    #                           # bordercolor="Black",
    #                           # borderwidth=1
    #                          ),
    #               legend_orientation='h',
    #                          )

    return fig


if __name__ == '__main__':
    app.run_server(port=8050)