![PSL](https://github.com/Usamamalik11/Pakistan-Super-League-Score/blob/main/PSL-2020-banner.jpeg)


Google Cloud App Link: https://cricket231.el.r.appspot.com
# PSL Score Prediction
Have you ever thought while watching a cricket match that what is going to be final score. Your answer is usually provided by the TV channel which is broadcasting the match. But sometimes you wonder whether it's the right prediction. That finl prediction is usually provided by artificial intelligence working in the backend. Can we ourselve develop such kind of models from scratch?
This gave me an idea to work on a similar project for my country's cricket league i.e. Pakistan Super league. Using streamlit and flask, I developed a basic web app that predicts the final score upon providing certain stats during the match. Lets see how the backend machine learning moel works in this case and what was the whole procedure.

## Data Collection
The relevant dataset was collected from https://cricsheet.org/ . But it was a long and tiresome process to manually clean the data and do feature engineering on it so that it could be transformed into a useful data.
Feature engineering was performed on it as well as data for above hundred matches was cleaned and combined into a single dataset. It was a long and tiresome process but was worth it.

## Data Wrangling
The null values were replaced with suitable values in the dataset.
For data visualization, I used a library known as dtale. I came to know about this library a few days ago while scrolling hrough youtube and I have to say I loved it. You can see relationship between different variables in an interactive way. Not only this, it also provides you the code for the visualizations. It is a must try library and everyone interested in trying new things must give it a try. 
The next step was selecting some columns and dropping others. The total number of features were 11 which were as follow:
#### Over Ball
The current ball of the over going on.
#### Batting Team
The team which is on the pitch i.e which is batting. Remember that we have only considered the 1st innings.
#### Bowling Team
The team whic is fielding.
#### Striking Batsman
The batsman who is on the striking end of the pitch.
#### Non Striking Batsman
The batsman who is on the non striking end of the pitch.
#### Bowler
The bowler bowling the current ball.
#### Extras
The extras given on that ball.
#### Runs Scored
Runs which were scored on that specific ball.
#### Fallen Wickets
Number of wickets that have already fallen.
#### Cumulative Runs Scored
The runs scored uptill the current ball.
#### Stadium
The stadium hosting the match.
#### Final Score
This is the dependent and target variable. It is the final score(the actual final score).

A custom label encoder was made and applied on batting team, bowling team and stadium columns.This custom encodel was also saved as ml.pkl file for further use in the app.
At first I did normalize the data but upon receiving results, I noticed that it is not necessary as model is performing better without it. But you can normalize and it's up to you.
The striking batsman, non striking batsman and bowler were droped as they weren't having a major impact on the final results.

## Model Development
The algorithm I used is random forest regressor. I tried some other algos as well but random forest was giving the best results with an accuracy of above ninety percent. The model was then saved as pkl file for further use.

## Web App
The first web app was developed with the help of flask. You can understand and run the code and run the app on your machine. The code is simple python and I hope you'll we able to understand it.
The second web app was develped with the help of stramlit and I was amazed to know how easy it was to develop a web app using streamlit. Its file is also there in the repository.
I'll also deploy the model in AWS and Azure in few days so that it can be accessed easily.

There is also a docker file in the repo but I was unable to dockerize the whole model due to certain problems in my laptop. However you can download and do it yourself. You are welcome to make any improvements to the model. Thank You.

