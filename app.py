#import Data_query
import streamlit as st
import numpy as np
import pandas as pd
import json
import urllib
from pymongo import MongoClient
import dns
from datetime import datetime
import data_accumulation
from pytz import timezone 
def data():
    uri = 'mongodb+srv://likith:' + urllib.parse.quote("Rp-iA@c6!Nq45c4") + '@cluster0.ms0ap.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = MongoClient(uri)
    db = client.weather
    data = db.data
    client.close()
    return data
def web(x):
    st.write('Place :', x['title'])
    st.write('Message :', x['Message'])
    if x['Message'] != 'No data Available' :
        st.write(" Date of issue : ", x['Date of issue'])
        if (x['Time of issue'] < 12):
            st.write(" Time of issue : ", str(x['Time of issue'])+" AM")
        else:
            st.write(" Time of issue : ", str(round(x['Time of issue']-12,2)) + " PM")
        if (x['Valid upto'] < 12):
            st.write(" Valid upto : ", str(x['Valid upto'])+" AM")
        elif(x['Valid upto'] >= 12 and x['Valid upto'] < 13  ):
            st.write(" Valid upto : ", str(x['Valid upto']) + " PM")
        else:
            st.write(" Valid upto : ", str(round((x['Valid upto']-12),2)) + " PM")
st.title('**HERE YOU GET UPTO DATE INFORMATION ABOUT WEATHER All OVER INDIA.....**')
data = data();
result = st.selectbox('Type your place here.....',data.distinct( "title"))
x = {'title': result}
mydoc = data.find(x)
x = "."
for y in mydoc:
    x=y
ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%H.%M')
st.write(x['Valid upto'])
st.write(float(ind_time))
if  x['Valid upto'] <= float(ind_time):
    d = data_accumulation.web_scrapping();
    info = data_accumulation.data_cleaning(d);
    data_accumulation.store_data(info);
    st.write("1")
x = {'title': result}
mydoc = data.find(x)
x = "."
for y in mydoc:
    x=y
web(x);
