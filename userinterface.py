
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from apyori import apriori
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from pymongo import MongoClient

  
client = MongoClient("localhost", 27017)
db = client["adtProject"]
new_df = pd.DataFrame(db["rules"].find({}))
words = st.sidebar.selectbox("No.of Words", range(10,1000,10))
st.title('Market Basket Analysis')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.sidebar.header("Select Item")
Input = st.sidebar.selectbox('Object Variables', new_df["Bought Item"])
print(Input)
sample = new_df[new_df['Bought Item'] == Input]
lis1 = []
for i in sample["Expected To Be Bought"]:
    lis1.append(i)
space = " "
output = space.join(lis1)
output_final = output.replace("nan", "")
new_title = '<p style="font-family:sans-serif; color:Green; font-size: 32px;">Recommended Items for above selected Item</p>'
st.markdown(new_title, unsafe_allow_html=True)

#st.markdown("Recommended Items for above selected Item")
st.write(output_final)
st.write("Word Cloud Plot")
wordcloud = WordCloud(background_color="white", max_words=words).generate(output_final)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()