
import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pymongo import MongoClient
  
client = MongoClient( st.secrets["MONGO_URL"])
# client = MongoClient("localhost", 27017)

#accessing db
db = client["adtProject"]

#fethcing all rules from the collection
apriori_rules = pd.DataFrame(db["rules"].find({}))

#fethcing all rules from the collection
fp_rules = pd.DataFrame(db["fp_rules"].find({}))

#dropdown for the number of suggestions
words = st.sidebar.selectbox("No.of Words", range(10,1000,10))

#setting up title
st.title('Market Basket Analysis')

#deprecating warning
st.set_option('deprecation.showPyplotGlobalUse', False)

#setting header
st.header("Select Item")
temp = []
temp.extend(apriori_rules["Bought Item"])
for i in fp_rules["Bought Item"]:
    for j in i.split(","):
        temp.append(j)

#taking multiple inputs from user
input = st.multiselect(
    'What are your favorite dishes',
    list(set(temp)))

#processing input and getting list of items expected to buy
sample = apriori_rules 
if input:
    sample = apriori_rules[apriori_rules['Bought Item'].isin(input)]
    if len(sample)!=0:
        lis1 = []
        for i in sample["Expected To Be Bought"]:
            lis1.append(i)
        space = " "
        output = space.join(lis1)
        #cleaning data
        output_final = output.replace("nan", "")
        output_final = output.replace("None", "")
        op = set(lis1)
        if "None" in op:
            op.remove("None")
        st.write(op)
        st.header("Word Cloud Plot from Apriori Rules")

        #developing wordcloud from the result
        wordcloud = WordCloud(background_color="white", max_words=words).generate(output_final)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()

sample = fp_rules 
# print(sample["Expected To Be Bought"])
if input:
    sample = fp_rules[fp_rules['Bought Item'].isin(input)]
    if len(sample)!=0:
        lis1 = []
        print(sample["Expected To Be Bought"])
        for i in sample["Expected To Be Bought"]:
            lis1.append(i)
        space = " "
        output = space.join(lis1)
        #cleaning data
        output_final = output.replace("nan", "")
        output_final = output.replace("None", "")
        op = set(lis1)
        if "None" in op:
            op.remove("None")
        st.write(op)
        st.header("Word Cloud Plot from FP Growth Rules")

        #developing wordcloud from the result
        wordcloud = WordCloud(background_color="white", max_words=words).generate(output_final)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()