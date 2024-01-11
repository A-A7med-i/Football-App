import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np



class Visualization :

    def __init__(self):
        '''
        init method have 
        call the uploade method to return the data
        2 tabs
        call sactter and hist method
        '''
        self.color = '#BB8FCE'
        self.data = 'F:\Football_App\Data\World Cup 2018.CSV'
        self.df = self.uploadData(self.data)
        self.df.drop(columns='Unnamed: 0',inplace=True)
        self.numerical = self.df.select_dtypes(include = np.number ).columns.to_list()
        self.tab_1,self.tab_2 = st.tabs(['Scatter' , 'Histograph'])
        self.scatter()
        self.hist()

    
    @st.cache_data
    def uploadData(_self , file):
        '''
        This method is return the data for increase the performance
        '''
        _self.file = file
        return pd.read_csv(_self.file)
    

    def scatter(self):
        '''
        This method is about scatter plot 
        You have the freedom to choose the row and the column
        and can comparing with each column
        '''
        with self.tab_1 :
            self.col_1 , self.col_2 , self.col_3 = st.columns(3)

            with self.col_1:
                self.x_axis = st.selectbox("Select the x axis : " , self.numerical , index = 5)

            with self.col_2:
                self.y_axis = st.selectbox("Select the y axis : " , self.numerical ,index = 2)

            with self.col_3:
                self.color = st.selectbox("Select color : " , self.df.columns , index = 2)

            self.graph_scat = px.scatter(self.df , x = self.x_axis , y = self.y_axis , color = self.color)
            st.plotly_chart(self.graph_scat , theme = 'streamlit')



    def hist(self):
        '''
        This method is about histogram plot 
        You have the freedom to choose the row
        '''
        with self.tab_2:
            self.color = '#0d3b66'
            self.x_axis = st.selectbox('Select the x axis', self.numerical, placeholder='Select the x axis' , index = 2)
            self.graph_hist = px.histogram(self.df, x = self.x_axis , color_discrete_sequence = [self.color])
            st.plotly_chart(self.graph_hist, theme='streamlit')


Visualization()
