#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Yeonji
"""

import dash

import dash_core_components as dcc

import dash_daq as daq

import dash_html_components as html

from dash.dependencies import Input, Output

 

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

 

df = pd.read_csv("clean_data.csv")

X = df[df.columns.difference(['Final Grade'])]
Y = df['Final Grade']

 

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

 

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

 

regressor = LinearRegression() 

regressor.fit(X_train, Y_train)

 


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

 

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server=app.server

 

app.layout = html.Div([

       

    html.H1('Student Performance Predictor'),

       

    html.Div([  

    html.Label('Home to School Travel Time [1: less to 4: high]'),

    dcc.Slider(id='travel-slider',

            min=1, max=4, step=1, value=3,

               marks={
                
        1: {'label': '1'},

        2: {'label': '2'},

        3: {'label': '3'},

        4: {'label': '4'},                        

    }),

 

html.Br(),

html.Label('Weekly Study Time Score [1: less to 4: high]'),

dcc.Slider(id='study-slider',

            min=1, max=4, step=1, value=3,

               marks={
                
        1: {'label': '1'},

        2: {'label': '2'},

        3: {'label': '3'},

        4: {'label': '4'},                        

    }),

 

html.Br(),

html.Label('Past Failure Experiences'),

dcc.Slider(id='fail-slider',

            min=0, max=3, step=1, value=2,

               marks={
                
        0: {'label': '0'},

        1: {'label': '1'},

        2: {'label': '2'},

        3: {'label': '3'},                        

    }),


 

html.Br(),

html.Label('Quality of Family Relationship [1: very bad to 5: excellent]'),

dcc.Slider(id='family-slider',

            min=1, max=5, step=1, value=2,

               marks={
                
        1: {'label': '1'},

        2: {'label': '2'},

        3: {'label': '3'},

        4: {'label': '4'},    

        5: {'label': '5'}                    

    }),


html.Br(),

html.Label('Free Time After School [1: very low to 5: very high]'),

dcc.Slider(id='free-slider',

            min=1, max=5, step=1, value=2,

               marks={
                
        1: {'label': '1'},

        2: {'label': '2'},

        3: {'label': '3'},

        4: {'label': '4'},    

        5: {'label': '5'}                    

    }),


html.Br(),

html.Label('Peer Hangout Extent [1: very low to 5: very high]'),

dcc.Slider(id='peer-slider',

            min=1, max=5, step=1, value=2,

               marks={
                
        1: {'label': '1'},

        2: {'label': '2'},

        3: {'label': '3'},

        4: {'label': '4'},    

        5: {'label': '5'}                    

    }),


html.Br(),

html.Label('Health Status Score [1: very bad to 5: very good]'),

dcc.Slider(id='hth-slider',

            min=1, max=5, step=1, value=2,

               marks={
                
        1: {'label': '1'},

        2: {'label': '2'},

        3: {'label': '3'},

        4: {'label': '4'},    

        5: {'label': '5'}                    

    }),


html.Br(),

html.Label('First Period Grade'),

dcc.Slider(id='firstgrade-slider',

            min=0, max=20, step=1, value=10,

               marks={
                
        0: {'label': '0'},

        5: {'label': '5'},

        10: {'label': '10'},

        15: {'label': '15'},

        20: {'label': '20'}                            

    }),

 

html.Br(),

html.Label('Second Period Grade'),

dcc.Slider(id='secondgrade-slider',

            min=0, max=20, step=1, value=10,

               marks={
                
        0: {'label': '0'},

        5: {'label': '5'},

        10: {'label': '10'},

        15: {'label': '15'},

        20: {'label': '20'}                            

    }),


],className="pretty_container four columns"),

 



  html.Div([

 

    daq.Gauge(

        id='finalgrade-gauge',

        showCurrentValue=True,

        color={"gradient":True,"ranges":{"red":[0,5],"yellow":[5,15],"green":[15,20]}},

        label="Final Grade",

        max=20,

        min=0,

        value=10

    ),

])

    ])

 

 

@app.callback(

    Output('finalgrade-gauge', 'value'),

    [Input('travel-slider', 'value'),

     Input('study-slider', 'value'),

     Input('fail-slider', 'value'),

     Input('family-slider', 'value'),

     Input('free-slider', 'value'),
     
     Input('peer-slider', 'value'),

     Input('hth-slider', 'value'),

     Input('firstgrade-slider', 'value'),

     Input('secondgrade-slider', 'value')

     ])

def update_output_div(travel,
                      study,
                      fail,
                      family,
                      free,
                      peer,
                      hth,
                      firstgrade,
                      secondgrade):

   X_case = pd.DataFrame({'traveltime':[travel],'studytime':[study],
                          'failures':[fail],'famrel':[family],'freetime':[free],
                          'goout':[peer],'health':[hth],
                          'FirstPeriodGrade':[firstgrade],'SecondPeriodGrade':[secondgrade]})

   Y_case = regressor.predict(X_case)


   return Y_case[0]

 

 

if __name__ == '__main__':

    app.run_server()
