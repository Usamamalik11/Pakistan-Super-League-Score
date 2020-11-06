# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:33:33 2020

@author: HP
"""
#from flask import Flask,request
import pandas as pd
import numpy as np
import dill as pickle
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn import preprocessing
#import flasgger
#from flasgger import Swagger
import streamlit as st

#app=Flask(__name__)
#Swagger(app)
from PIL import Image

with open('model' ,'rb') as f1:
    loaded_model = pickle.load(f1)
with open('sc','rb') as f2:
    stand = pickle.load(f2)
with open('important','rb') as f3:
    encoder = pickle.load(f3)


#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict')
def predict_score(Over_Ball,Batting_Team,Bowling_Team,Stadium,Runs_Scored,Extras,Fallen_Wickets,Cumulative_Runs_Scored):
    
    """Let's Predict the Score 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: Over_Ball
        in: query
        type: number
        required: true
      - name: Batting_Team
        in: query
        type: string
        required: true
      - name: Bowling_Team
        in: query
        type: string
        required: true
      - name: Stadium
        in: query
        type: string
        required: true
      - name: Runs_Scored
        in: query
        type: number
        required: true
      - name: Extras
        in: query
        type: number
        required: true
      - name: Fallen_Wickets
        in: query
        type: number
        required: true
      - name: Cumulative_Runs_Scored
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """

    #Over_Ball=request.args.get("Over_Ball")
    #Batting_Team=request.args.get("Batting_Team")
    #Bowling_Team=request.args.get("Bowling_Team")
    #Stadium=request.args.get("Stadium")
    #Runs_Scored=request.args.get("Runs_Scored")
    #Extras=request.args.get("Extras")
    #Fallen_Wickets=request.args.get("Fallen_Wickets")
    #Cumulative_Runs_Scored=request.args.get("Cumulative_Runs_Scored")
    
    data={'Over_Ball':[Over_Ball],
          'Batting_Team':[Batting_Team],
          'Bowling_Team':[Bowling_Team],
          'Stadium':[Stadium],
          'Runs_Scored':[Runs_Scored],
          'Extras':[Extras],
          'Fallen_Wickets':[Fallen_Wickets],
          'Cumulative_Runs_Scored':[Cumulative_Runs_Scored]
        }
    
    check = pd.DataFrame (data, columns =['Over_Ball','Batting_Team', 'Bowling_Team','Stadium','Runs_Scored', 'Extras', 'Fallen_Wickets','Cumulative_Runs_Scored'])
    Bat=pd.Series(check['Batting_Team'].values)
    check[['Batting_Team']]=Bat.map({'Islamabad United':0,'Peshawar Zalmi':4,'Quetta Gladiators':5,'Lahore Qalandars':2,'Multan Sultans':3,'Karachi Kings':1})
    Bowl=pd.Series(check['Bowling_Team'].values)
    check[['Bowling_Team']]=Bowl.map({'Islamabad United':0,'Peshawar Zalmi':4,'Quetta Gladiators':5,'Lahore Qalandars':2,'Multan Sultans':3,'Karachi Kings':1})
    Stad=pd.Series(check['Stadium'].values)
    check[['Stadium']]=Stad.map({'Sharjah Cricket Stadium':5,'Rawalpindi Cricket Stadium':4,'Gaddafi Stadium Lahore':1,'Dubai International Cricket Stadium':0,'National Stadium Karachi':3,'Sheikh Zayed Stadium Abu Dhabi':6,'Multan Cricket Stadium':2})
    prediction=loaded_model.predict(check)
    return "Hello The answer is"+str(prediction)

#@app.route('/predict_file',methods=["POST"])
def predict_score_test():
    
    """Let's predict the scores 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))
    df_test=encoder.fit_transform(df_test)
    predictions=loaded_model.predict(df_test)
    
    return str(list(predictions))


def main():
    st.title("PSL Score Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Score Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Over_Ball = st.text_input("Over_Ball","Type Here")
    Batting_Team = st.text_input("Batting_Team","Type Here")
    Bowling_Team = st.text_input("Bowling_Team","Type Here")
    Stadium = st.text_input("Stadium","Type Here")
    Runs_Scored = st.text_input("Runs_Scored","Type Here")
    Extras = st.text_input("Extras","Type Here")
    Fallen_Wickets = st.text_input("Fallen_Wickets","Type Here")
    Cumulative_Runs_Scored = st.text_input("Cumulative_Runs_Scored","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_score(Over_Ball,Batting_Team,Bowling_Team,Stadium,Runs_Scored,Extras,Fallen_Wickets,Cumulative_Runs_Scored)
    st.success('The output is {}'.format(result))


    













if __name__=='__main__':
    main()