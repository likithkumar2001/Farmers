#import Data_query
import streamlit as st
import numpy as np
import pandas as pd
import json
import urllib
from pymongo import MongoClient
import dns
from datetime import datetime
def trans(language,text):
    from googletrans import Translator, constants
    translator = Translator()
    Text_message = translator.translate(text, dest=language).text
    return Text_message

uri = 'mongodb+srv://likith:' + urllib.parse.quote(
    "Rp-iA@c6!Nq45c4") + '@cluster0.ms0ap.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = MongoClient(uri)
db = client.weather
data = db.data
lang=['English','Telugu','Hindi']
la=st.sidebar.selectbox('select language',lang)
lan = ['en','te','hi']
st.title(trans(lan[lang.index(la)], 'HERE YOU GET UPTO DATE INFORMATION ABOUT WEATHER All OVER INDIA.....'))
result = st.selectbox('Type your place here.....',data.distinct( "title"))
x = {'title': result}
mydoc = data.find(x)
x = "."
for y in mydoc:
    x=y
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
