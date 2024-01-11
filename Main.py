import streamlit as st


class Main:
    def __init__(self):
        '''
        init method have the title and icon of the main page 
        sidebar to access the another page
        '''
        self.title = 'Foot Ball App'
        self.message = 'Welcome To World Cup 2018'
        self.choose = 'Choose The Page'
        st.set_page_config(page_title=self.title )
        st.title(self.message)
        st.sidebar.success(self.choose)


if __name__ == '__main__':
    Main()
