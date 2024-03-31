import streamlit as st
import pandas as pd
import time
# Title and icon of the app
st.set_page_config(
    page_title="News Dataset",
    page_icon="🌐",
    layout="wide"
)

# Initialize session state variables
# Session state allows you to maintain a state in your app across reruns
if 'my_button' not in st.session_state:
    st.session_state.my_button = False
if 'show_bar_chart' not in st.session_state:
    st.session_state.show_bar_chart = False
if 'load_app' not in st.session_state:
    st.session_state.load_app = False
if 'show_code' not in st.session_state:
    st.session_state.show_code = False
    
# Define a function to change the state of 'my_button' when called
def click_button():
    st.session_state.my_button = True

# Display headers and subheaders in your app
st.title(':rainbow[Project on NLP analysis of News Dataset]')
st.header('Done by Mikhail Belkin')
st.write('Data obtained from Kaggle, entries from January 2023 to February 2024')

st.text('To load the application, please click on the button down below.')
# Add a button to the app (with a key to avoid caching issues)
# When the button is clicked, the 'click_button' function is called, which changes the state of 'my_button' to True
st.button('Start', on_click=click_button)

# Check the state of 'my_button'
# If 'my_button' is True, it means the button has been clicked
if st.session_state.my_button == True:
    # Check the state of 'load_app'
    # If 'load_app' is False, it means the app has not been loaded yet
    if st.session_state.load_app == False:
        # Display a progress bar and fill it to 100% over 1 second
        bar = st.progress(0)
        time.sleep(1)
        bar.progress(100)
        st.success('🚀 The application has loaded successfully! 🚀')
        st.toast('Hip!')
        time.sleep(.5)
        st.toast('Hip!')
        time.sleep(.5)
        st.toast('Hooray!', icon='🎉')
        # Display balloons animation
        st.balloons()
        # Change the state of 'load_app' to True, indicating that the app has been loaded
        st.session_state.load_app = True
    
    
    # Display a message
    st.write('The Dataset we will be working with contains news on different topics and events.')
    st.write('Here are the first 7 lines of it:')
    # Generate a fake dataframe and display it in the app
    df = pd.read_csv('data.csv')
    st.dataframe(df.head(7))
        
    st.write('Let us check our dataset for any missing values:')
    st.write(df.isnull().sum())
    st.write('There are no missing values, we can continue!')
    st.write(':blue[Please, proceed to next page - "Project Members" to continue.]')
    
    
    