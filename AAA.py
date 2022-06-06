import streamlit as st
import numpy as np
import numpy_financial as npf
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import requests
import json
import altair as alt
import yfinance as yf
import fredapi
from fredapi import Fred
import datetime as dt
import pydeck as pdk
import statsmodels.api as sm
import nasdaqdatalink
#KtkauE_-pic1EFrCBFb4

# Home Page

# Sidebar dropdown 
option = st.sidebar.selectbox("Dashboard", ('Home', 'Valuation Models', 'Performance', 'Digital Assets', 'Comparison Analysis', 'Framework')) 

#Title & Header
if option == 'Home':
    st.title("Collin Jones")
    st.header("Data Analytics In Finance")
    st.text("Final Project")
    st.text("  Navigation With Left Dashboard | Framework & Source Code On 'Framework' Page")
    st.text(" ")
    st.markdown("""---""")
    st.text(" ")
    st.text(" Index | Valuations Models, Performance Visualization Models, Digital Asset Tracker, Comparison Analysis, Framework")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    
    #weather
    api_key = "54c08ecafc87e0166d56037c1fdaa23a"
    lat = "41.8786"
    lon = "-87.6251"
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=imperial" % (lat, lon, api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    current = data["current"]["temp"]
    w = data["current"]["wind_speed"]
    h = data["current"]["humidity"]
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", current, "1.2 °F")
    col2.metric("Wind", w, "3mph")
    col3.metric("Humidity", h, "4%")
   
 
    #map
    st.pydeck_chart(pdk.Deck(
         map_style='mapbox://styles/mapbox/dark-v8',
         initial_view_state=pdk.ViewState(
         latitude=41.87,
         longitude=-87.62,
         zoom=11,
         pitch=50)))
