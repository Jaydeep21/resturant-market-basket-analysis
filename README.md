# Market Basket Analysis on Resturant Dataset using Apriori and FP-Growth Algorithm

Market Basket Analysis(MBA) is one of the key techniques used by large retailers to uncover associations between items. In this project we are trying to perform market basket analysis on a resturant dataset.

## Dataset Source

We've downloaded the dataset from https://kaggle.com/ .

##  Project Flow

* We are using ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=plastic&logo=mongodb&logoColor=white) to fetch resturant dataset and to store association rules generated from both the algorithms. 

* We are performing Data analysis, generation of association rules using Apriori Algorithm and FP-Growth Algorithm using ![Python](https://img.shields.io/badge/python-3670A0?style=plastice&logo=python&logoColor=ffdd54) (this section of code exists in associationrules.ipynb file).

* UI is developed and hosted using strealit and its implementation can be seen in userinterface.py file. 

## 💻 Final Project

https://brogrammers.streamlit.app/

## To run the project

* Make a config.py file(as per example.config.py) and add mongodb source url.

* Download all the libraries as per requirements.txt using command

``` 
pip install -r requirements. txt
```

* Execute associationrules.ipynb file to generate rules.

* To start the streamlit server on localhost execute:
``` 
streamlit run userinterface.py 
```

## Our Team

- [Jaydeep Dharamsey](https://linkedin.com/in/jaydeepdharamsey/)
- [Henish Patel](https://www.linkedin.com/in/henishpatel)
- [Yash Somaiya](https://www.linkedin.com/in/yash-somaiya1)
- [Bharat Kumar Vayitla](https://www.linkedin.com/in/bharat-kumar-vayitla)