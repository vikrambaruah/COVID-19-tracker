from urllib.request import urlopen as request
import requests
import  json
import streamlit as st 
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import pandas as pd 
def autolabel(rects):
    
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2., int(height),
                '%d' %int(height),
        ha='center', va='bottom')

def getdata():
    #get the data
    url='https://coronavirus-tracker-api.herokuapp.com/v2/locations'
    data=request(url)
   
    #convert data from bytes to json
    final_data=json.loads(data.read())
    final_data=final_data['locations']

    #sort the data ,using number of cases as the key
    sorted_data=sorted(final_data,key=lambda k: k['latest']['confirmed'],reverse=True)

    #convert data to dataframe
    df=json_normalize(sorted_data)
    df=df.drop(['coordinates.longitude','coordinates.latitude','last_updated','latest.recovered','id','country_code'],axis=1)
    df.rename(columns = {'province':'Province','latest.deaths':'Deaths','latest.confirmed':'Confirmed Cases','country':'Country'}, inplace = True)
    return df
    

def worldwides():
    ogstatsurl='https://coronavirus-tracker-api.herokuapp.com/v2/latest'
    #making get request to the API
    client=request(ogstatsurl)
    data=client.read()
    client.close()
    #bytes to json
    final=json.loads(data)
        
    #number of confirmed cases all around the world ---------variable name - confnum
    confnum=final['latest']['confirmed']
    confirmed='''## Confirmed Cases ```  %d``` '''%(confnum)
    st.markdown(confirmed)

    #number of deaths around the world ---------variable name -deathnum
    deathnum=final['latest']['deaths']
    deaths='''## Deaths ``` %d ``` '''%(deathnum)
    st.markdown(deaths)

        
    objects = ('Deaths', 'Total Cases')#labels for the bar chart
    y_pos = np.arange(len(objects))
    #active=int(confnum)-(int(recoverednum)+int(deathnum))#finding number of active cases
    values = [int(deathnum),int(confnum)]#values for the bar chart
    ax=plt.bar(y_pos, values, align='center', alpha=0.7)#bar chart ----plotted using matplotlib
    plt.xticks(y_pos, objects)
        
        # Additional data for the graph
    plt.title('COVID-19')
    autolabel(ax)
    st.write(mpl_fig=ax)
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)
        
    df=getdata()

    #getting the list of countries 
    country_list=df['Country'].tolist()
    country_list=sorted(list(set(country_list)))
        
    choice=st.selectbox('Choose Country',country_list)
    #finding data related to specific country and displaying
    value=df.loc[df['Country']==choice]
    st.table(value)

    #dsplaying all data
    st.table(df)
       
    return
        

        
