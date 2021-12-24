from os import link
import streamlit as st
import pandas as pd
import joblib

st.title('Restraunt Rating Prediction App')
@st.cache
def load_data():
    df = pd.read_csv('new_zomato.csv')
    return df

def load_model():
   MODEL = joblib.load('restraunt_rating_pipe.sav')
   return MODEL

def rr(num,x):
    return round(num,x)

def get_prediction(name,online_order,book_table,votes,location,rest_type,cuisines,price,type,city):
    test_case = pd.DataFrame(data=[[name,online_order,book_table,votes,location,rest_type,cuisines,price,type, city]],columns=['name', 'online_order', 'book_table', 'votes', 'location', 'rest_type',
       'cuisines', 'price', 'type', 'city'])
    predictions = model.predict(test_case)
    return predictions[0]


if st.button('Find Me here !!!'):
    st.write('Lets Talk ... :smile:')
    st.markdown('<a href="https://www.linkedin.com/tosifkhan99" target="_blank">LinkedIn :computer:</a>',unsafe_allow_html=True)
    st.markdown('<a href="mailto:Khantosif94@gmail.com">Email me :email:</a>',unsafe_allow_html=True)
    st.markdown('<a href="https://www.kaggle.com/tosifkhan">Kaggle :blue_heart:</a>',unsafe_allow_html=True)
state = st.text('please wait, while we are laoding the app...')
df = load_data()
model = load_model()

state.text('loading complete... Sample of Data')
st.write(df[:10])

name = st.selectbox(
     'Name of Your Restraunt(in Bangalore)',
     (df.name))

online_order = st.selectbox(
    'Does your restraunt accepts online orders',
    ('Yes','No')
)
if online_order == "Yes":
    online_order = 1
else:
    online_order = 0
book_table = st.selectbox(
    'Does your restraunt supports table bookings ?',
    ('Yes','No' )
)
if book_table == "Yes":
    book_table = 1
else:
    book_table = 0

votes = st.slider(
    'How many number of votes your restraunt received (no of ratings)',
     min_value=0, 
     max_value=20000)
location = st.selectbox(
    'Where is your restraunt located ?',
    (df.location.unique())
)
city = st.selectbox(
    'Where is your restraunt located 2?',
    (df.city.unique())
)

restraunt_type =st.selectbox(
    'What is your restraunt type ?',
    (df.rest_type.unique())
) 
type =st.selectbox(
    'What is your restraunt type 2 ?',
    (df.type.unique())
)
cuisines = st.selectbox(
    'What kinds of cuisins your restraunt serves ?',
    (df.cuisines.unique())
)
price = st.slider(
    'What is the average price(2 persons)',
    min_value=100,
    max_value=10000
)
if st.button('Get Your Ratings'):
    msg = st.text('Hold Your customers, we are genrating ratings for you for you')
    ratings = get_prediction(name,online_order,book_table,votes,location,restraunt_type,cuisines,price,type,city)
    msg.text('')
    
    st.write('Your Restraunt is rated with: {:.3} :star2: out of 5'.format(ratings))
