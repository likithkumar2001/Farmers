#import Data_query
import streamlit as st
import numpy as np
import pandas as pd
import json
import urllib
import pymongo
import dns
from datetime import datetime
st.title("**HERE YOU GET UPTO DATE INFORMATION ABOUT WEATHER All OVER INDIA.....**")
uri = 'mongodb+srv://likith:' + urllib.parse.quote(
    "Rp-iA@c6!Nq45c4") + '@cluster0.ms0ap.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = pymongo.MongoClient(uri)
db = client.weather
data = db.data
result = st.selectbox('Type your place here.....',data.distinct( "title"))
x = {'title': result}
mydoc = data.find(x)
x = "."
for y in mydoc:
    x=y
st.write(" Title : ", x['title'])
st.write(" Message : ", x['Message'])
st.write(" Date of issue : ", x['Date of issue'])
if (x['Time of issue'] < 12):
    st.write(" Time of issue : ", str(x['Time of issue'])+" AM")
elif(x['Time of issue '] >= 12 and x['Time of issue '] < 13  ):
    st.write(" Time of issue  : ", str(x['Time of issue']) + " PM")
else:
    st.write(" Time of issue : ", str(round(x['Time of issue']-12,2)) + " PM")
if (x['Valid upto'] < 12):
    st.write(" Valid upto : ", str(x['Valid upto'])+" AM")

elif(x['Valid upto'] >= 12 and x['Valid upto'] < 13  ):
    st.write(" Valid upto : ", str(x['Valid upto']) + " PM")

else:
    st.write(" Valid upto : ", str(round((x['Valid upto']-12),2)) + " PM")
