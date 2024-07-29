#from PubmedArticle_s import article_spider as sp
import streamlit as st
from streamlit_option_menu import option_menu
import os
import time
from langchain.llms import openai

st.set_page_config(page_title='chatbot test', layout='wide')
st.title("My first chatbot")
with st.sidebar:
    choose = option_menu('website', ['chatbot', 'statistics', 'visuals'], 
                         icons=['house', 'book-half','book-half'])


openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.into(llm(input_text))





################# Example from another page ####################
if choose == 'intro':
    st.title('welcome to the page')
    st.write('this web is for PubMed articles')
    st.write('this belongs to xxx')

elif choose =='web scraping':
    term1 = st.text_input('please input key word:',)
    sp = sp()
    if len(term1) != 0:
        term = sp.input_term(term1)
    year = st.radio(
        "please select the year",
        ('empty', '1 year', '5 years', '10 years'), horizontal=True
    )