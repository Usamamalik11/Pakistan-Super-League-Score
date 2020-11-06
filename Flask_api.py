from flask import Flask,request
import pandas as pd
import numpy as np
import dill as pickle
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn import preprocessing

app=Flask(__name__)

with open('model' ,'rb') as f1:
    loaded_model = pickle.load(f1)
with open('sc','rb') as f2:
    stand = pickle.load(f2)
with open('important','rb') as f3:
    encoder = pickle.load(f3)


@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict')
def predict_score():
    Over_Ball=request.args.get("Over_Ball")
    Batting_Team=request.args.get("Batting_Team")
    Bowling_Team=request.args.get("Bowling_Team")
    Stadium=request.args.get("Stadium")
    Runs_Scored=request.args.get("Runs_Scored")
    Extras=request.args.get("Extras")
    Fallen_Wickets=request.args.get("Fallen_Wickets")
    Cumulative_Runs_Scored=request.args.get("Cumulative_Runs_Scored")
    
    data={'Over_Ball':[Over_Ball],
          'Batting_Team':[Batting_Team],
          'Bowling_Team':[Bowling_Team],
          'Stadium':[Stadium],
          'Runs_Scored':[Runs_Scored],
          'Extras':[Extras],
          'Fallen_Wickets':[Fallen_Wickets],
          'Cumulative_Runs_Scored':[Cumulative_Runs_Scored]
        }
    
    df = pd.DataFrame (data, columns =['Over_Ball','Batting_Team', 'Bowling_Team','Stadium','Runs_Scored', 'Extras', 'Fallen_Wickets','Cumulative_Runs_Scored'])
    df=encoder.fit_transform(df)
    prediction=loaded_model.predict(df)
    return "Hello The answer is"+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_score_test():
    df_test=pd.read_csv(request.files.get("file"))
    df_test=encoder.fit_transform(df_test)
    df_test=stand.fit_transform(df_test)
    predictions=loaded_model.predict(df_test)
    
    return str(list(predictions))



    













if __name__=='__main__':
    app.run(host = '127.0.0.1')