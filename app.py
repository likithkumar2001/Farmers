#import Data_query
import streamlit as st
import numpy as np
import pandas as pd
import json
import urllib
import pymongo
import dns
from datetime import datetime

def trans(language,text):
    import googletrans
    translator = googletrans.Translator()
    Text_message = translator.translate(text, dest=language)
    return Text_message.text

uri = 'mongodb+srv://likith:' + urllib.parse.quote(
    "Rp-iA@c6!Nq45c4") + '@cluster0.ms0ap.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = pymongo.MongoClient(uri)
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
st.write(str(trans(lan[lang.index(la)],'Place :')), trans(lan[lang.index(la)],x['title']))
st.write(str(trans(lan[lang.index(la)], 'Message :')), trans(lan[lang.index(la)], x['Message']))
st.write(str(trans(lan[lang.index(la)],'Date of issue:')), x['Date of issue'])
if (x['Time of issue'] < 12):
    st.write(str(trans(lan[lang.index(la)],'Time of issue :')), str(x['Time of issue'])+" AM")
else:
    st.write(str(trans(lan[lang.index(la)],'Time of issue :')), str(round(x['Time of issue']-12,2)) + " PM")
if (x['Valid upto'] < 12):
    st.write(str(trans(lan[lang.index(la)],'Valid upto :')), str(x['Valid upto'])+" AM")
elif(x['Valid upto'] >= 12 and x['Valid upto'] < 13  ):
    st.write(str(trans(lan[lang.index(la)],'Valid upto :')), str(x['Valid upto']) + " PM")
else:
    st.write(str(trans(lan[lang.index(la)],'Valid upto :')), str(round((x['Valid upto']-12),2)) + " PM")
