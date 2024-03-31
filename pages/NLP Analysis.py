import streamlit as st
import pandas as pd
import spacy
import eng_spacysentiment
from bertopic import BERTopic

st.set_page_config(
    page_title="NLP Analysis",
    page_icon="⚙️",
    layout="wide"
)

st.title(':rainbow[NLP Analysis]')
st.header(':red[Multiple Analyses using different methods]')
st.text('From sematic similarity and word vectors to topic modeling')

nlp = spacy.load("en_core_web_md")
df = pd.read_csv('data.csv')

st.subheader("Content Similarity Calculator")
st.write('First of all, we are going to continue with similarity between two news articles.')
st.write('The set used to analyze and compare two news articles is done via spacy & en_core_web_md.')
st.write('Since its a medium-sized model, some inaccuracies might occur.')
st.write('Medium-sized model was used due to the computational and CPU power of PC.')
st.text('Choose two numbers between 0 and 199705, and type them in these boxes.')
row_num1 = st.number_input("Enter the first row number:", min_value=0, max_value=len(df)-1, value=0)
row_num2 = st.number_input("Enter the second row number:", min_value=0, max_value=len(df)-1, value=0)

def content_similarity(row_num1, row_num2):
    content1 = df.iloc[row_num1]['Content']
    content2 = df.iloc[row_num2]['Content']
    doc1 = nlp(content1)
    doc2 = nlp(content2)
    return content1, content2, doc1.similarity(doc2)

if st.button("Compare"):
    content1, content2, similarity_score = content_similarity(row_num1, row_num2)
    st.write(":blue[Article 1 Content]")
    st.write(content1)
    st.write(":blue[Article 2 Content]")
    st.write(content2)
    st.write(f"##### Similarity Score: {similarity_score:.4f}")

st.subheader("Sentiment Analysis")
st.write('Now, you can perform a sentiment analysis for a random news article.')
st.write('The model used for this analysis is called eng_spacysentiment.')
st.write('You can do it for both the headline and the news article itself.')
st.write('It will give you "positive", "negative", and "neutral", and its corresponding % of confidence.')
st.text('Choose a number between 0 and 199705, and type it in this box.')

nlp = spacy.load("eng_spacysentiment")
df = pd.read_csv('data.csv')

def sentiment(row_num):
    headline = df.iloc[row_num]['Headline']
    content = df.iloc[row_num]['Content']
    doc_headline = nlp(headline)
    doc_content = nlp(content)
    return headline, doc_headline.cats, content, doc_content.cats

row_num = st.number_input("Enter the row number:", min_value=0, max_value=len(df)-1, value=0)

if st.button("Analyze"):
    headline, headline_cats, content, content_cats = sentiment(row_num)
    st.write(":blue[Headline Sentiment]")
    st.write(headline)
    st.text(headline_cats)
    st.write(":blue[Content Sentiment]")
    st.write(content)
    st.text(content_cats)

st.write(':blue[For the Topic Modeling and its visuals, please click on the "NLP Visuals" page.]')