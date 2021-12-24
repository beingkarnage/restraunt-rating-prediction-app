# restraunt-rating-prediction-app

## About the Project :
This app is based on zomato's dataset of various restraunts, for detailed documentation of this dataset refer to the link below
https://www.kaggle.com/himanshupoddar/zomato-bangalore-restaurants

## Installation :
for running the app only
pip install requirements.txt

## Use this app
create a local copy of this repository in your system and run with command

streamlit run app.py

## Files
new_zomato.csv : this dataset is present which is just a cleaned copy of original dataset for presentation purpose in app
restraunt_rating_pipe.zip : XGBoost regressor model zipped, is stored with pipelines, refer to the python notebook for code, unzip into the root directory
restraunt-rating-prediction.ipynb : notebook of app, analysis, preprocessing, modeling, etc
