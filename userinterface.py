
import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pymongo import MongoClient
import os
  
client = MongoClient(os.environ['MONGO_URL'])
db = client["adtProject"]
new_df = pd.DataFrame(db["rules"].find({}))
words = st.sidebar.selectbox("No.of Words", range(10,1000,10))
st.title('Market Basket Analysis')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.header("Select Item")
input = st.multiselect(
    'What are your favorite dishes',
    list(set(new_df["Bought Item"])))
sample = new_df 
if input:
    sample = new_df[new_df['Bought Item'].isin(input)]
lis1 = []
for i in sample["Expected To Be Bought"]:
    lis1.append(i)
space = " "
output = space.join(lis1)
output_final = output.replace("nan", "")
st.header("Word Cloud Plot")
wordcloud = WordCloud(background_color="white", max_words=words).generate(output_final)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()