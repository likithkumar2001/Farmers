import lang
import streamlit as st
import numpy as np
import pandas as pd
import json
import urllib
from pymongo import MongoClient
import dns
from datetime import datetime
import data_accumulation
from googletrans import Translator, constants
import pytz
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
            st.write(" Time of issue : ", str(round((x['Time of issue']-12),3)) + " PM")
        if (x['Valid upto'] < 12):
            st.write(" Valid upto : ", str(x['Valid upto'])+" AM")
        elif(x['Valid upto'] >= 12 and x['Valid upto'] < 13  ):
            st.write(" Valid upto : ", str(x['Valid upto']) + " PM")
        else:
            st.write(" Valid upto : ", Time of issue + " PM")
st.title('**HERE YOU GET UPTO DATE INFORMATION ABOUT WEATHER All OVER INDIA.....**')
i = data();
result = st.selectbox('Type your place here.....',i.distinct( "title"))
x = {'title': result}
mydoc = i.find(x)
x = "."
for y in mydoc:
    x=y
IST = pytz.timezone('Asia/Kolkata')
now = datetime.now(IST)
current_time = now.strftime("%H.%M")
if  x['Valid upto'] <= float(current_time):
    u = data_accumulation.web_scrapping();
    info = data_accumulation.data_cleaning(u);
    data_accumulation.store_data(info);
    data = data();
    x = {'title': result}
    mydoc = data.find(x)
    x = "."
    for y in mydoc:
        x=y
    web(x)
else:
    web(x)
