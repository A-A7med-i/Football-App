import streamlit as st
import pandas as pd



class DataFrame:
    def __init__(self):
        '''
        init method 
        call the uploaddata
        call apear
        '''
        self.data = 'F:\Football_App\Data\World Cup 2018.CSV'
        self.df = self.uploadData(self.data)
        self.df.drop(columns='Unnamed: 0',inplace=True)
        self.apear()
        st.write(self.df[:self.rows][self.col])

    @st.cache_data
    def uploadData(_self , file):
        '''
        This method is return the data for increase the performance
        '''
        _self.file = file
        return pd.read_csv(_self.file)

    def apear(self):
        '''
        This method makes you have freedom to show any column ant any number of row 
        '''
        self.rows = st.slider('Choose the number of rows' , min_value = 5 ,max_value = len(self.df))

        self.col = st.multiselect('Choose the columns' , self.df.columns.to_list(),default = ['Day','Team','Opponent'])


DataFrame()