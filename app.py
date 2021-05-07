#import Data_query
import streamlit as st
import numpy as np
import pandas as pd
import json
import urllib
import pymongo
import dns
from datetime import datetime
import data_accumulation
data = data_accumulation.web_scrapping()
info = data_accumulation.data_cleaning(data)
data_accumulation.store_data(info)
info
