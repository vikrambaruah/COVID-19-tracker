import streamlit as st
from urllib.request import urlopen as request
from urllib.request import Request,urlopen
import json
from bs4 import BeautifulSoup as soup
from languages import *
from helpline import helpline
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt 
from pandas.io.json import json_normalize
from PIL import Image
from symptoms import symptoms
import requests
from news import news
from hospitals import hospitals
from india import indianStats
from boutme import boutme
from worldwide import worldwides

def list_cities():
    cities=["Delhi","Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","Puducherry"]
    return  cities




def main():
    st.title('COVID - 19')
    menuItems=['Guidelines','India Statistics','Worldwide Statistics','Hospital Stats India','Symptoms','Helpline','About me']
    st.sidebar.title('Menu')
    
    
    itemSelected=st.sidebar.selectbox('',menuItems)
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    

    if(itemSelected=='Helpline'):
        st.markdown(helpline())
   
    if(itemSelected=='About me'):
        st.markdown(boutme())
    if(itemSelected=='Hospital Stats India'):
        hospitals()
    if(itemSelected=='India Statistics'):
        indianStats()
    if(itemSelected=='Guidelines'):
        
        langugaes=['English','हिंदी','ગુજરાતી','தமிழ்','తెలుగు','ਪੰਜਾਬੀ','മലയാളം','ಕನ್ನಡ']
        lang=st.selectbox('Choose Language',langugaes)
        st.subheader('WHO Guidelines')
        
        if(lang=='English'):
           st.markdown(english())
        elif(lang=='தமிழ்'):
            st.markdown(tamil())
        elif(lang=='हिंदी'):
            st.markdown(hindi())
        elif(lang=='ગુજરાતી'):
            st.markdown(gujarati())
        elif(lang=='తెలుగు'):
            st.markdown(telugu())
        elif(lang=='ਪੰਜਾਬੀ'):
            st.markdown(punjabi())
        elif(lang=='മലയാളം'):
            st.markdown(malayalam())
        elif(lang=='ಕನ್ನಡ'):
            st.markdown(kannada())
        

    if(itemSelected=='Worldwide Statistics'):
        worldwides()
        
    if(itemSelected=='Symptoms'):
        st.markdown(symptoms())
        st.write('Source : WHO')


if __name__ == '__main__':
    st.set_option('deprecation.showPyplotGlobalUse', False)
    main()

