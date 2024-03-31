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

st.subheader("Topic Modeling")
st.write('Finally, we will perform topic modeling using BerTopic on news articles')
st.write('We will also remove the stopwords, they are defined via en.Defaults.stop_words')
st.text('We had to limit the amount of rows to 15000 due to computational capacities')
st.text('In other words, it would take a long time to calculate for all the rows')
st.text('Yes, at first nothing happens, but just wait, let it load :)')

df1 = pd.read_csv('data.csv')
df = df1.head(15000)

en = spacy.load('en_core_web_md')
stopwords = en.Defaults.stop_words

def clean(Content):
    text_clean = ''
    for token in Content.split():
        if token.lower() not in stopwords:
            text_clean += token + ' '
    return text_clean

df['text_clean'] = df['Content'].apply(clean)
docs = df['text_clean'].to_list()
nlp = spacy.load('en_core_web_md', 
                 exclude=['tagger', 'parser', 'ner', 'attribute_ruler', 'lemmatizer'])

model = BERTopic(embedding_model=nlp,verbose=True)
topics, probabilities = model.fit_transform(docs)
topic_vis = model.visualize_barchart(n_words=10,height=300)
st.plotly_chart(topic_vis)
topic_vis2 = model.visualize_topics()
st.plotly_chart(topic_vis2)

st.write('Wow ! There are a lot of topics ! Let us reduce them and visualize once again.')

model.reduce_topics(docs)
new_topics = model.topics_
new_probs = model.probabilities_

st.text('We have reduced the amount of topics from over 500 to just 20 ! What a great job !')

new_vis = model.visualize_barchart(n_words=10,height=300)
st.plotly_chart(new_vis)
new_vis2 = model.visualize_topics()
st.plotly_chart(new_vis2)

st.subheader(':blue[This concludes our NLP Analysis, thank you :)]')