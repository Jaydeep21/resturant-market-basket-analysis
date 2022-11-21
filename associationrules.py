import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from apyori import apriori
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from pymongo import MongoClient

  
client = MongoClient("mongodb+srv://brogrammers:f43op3GduCWsG3OQ@cluster0.naknivb.mongodb.net/?retryWrites=true&w=majority")
db = client["adtProject"]
dataset = pd.DataFrame(db["resturant"].find({}))
dim = dataset.shape
rows = dim[0]
cols = dim[1]
print(rows, cols)
transactions = []
for i in range(0, rows):
    transactions.append([str(dataset.values[i,j]) for j in range(0, cols)])
rule_list = apriori(transactions, min_support = 0.003, min_confidence = 0.1, min_lift = 3, min_length = 2)
results = list(rule_list)
bought_item = [tuple(result[2][0][0])[0] for result in results]
will_buy_item = [tuple(result[2][0][1])[0] for result in results]
support_values = [result[1] for result in results]
confidences = [result[2][0][2] for result in results]
lift_values = [result[2][0][3] for result in results]
db['rules'].delete_many({})
for i in range(len(bought_item)):
    db['rules'].insert_one({
        "_id": i,
        "Bought Item":bought_item[i],
        "Expected To Be Bought":will_buy_item[i],
        "Support":support_values[i],
        "Confidence":confidences[i],
        "Lift":lift_values[i],
     })
