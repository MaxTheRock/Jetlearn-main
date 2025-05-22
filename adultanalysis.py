import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt 
import plotly
import plotly.express as px  
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv("adult.csv")

data.columns = ["age","work-class","fnlwgt","education","educational-num","martial-status","occupation","relationship","race","gender","capital-gain","capital-loss","hours-per-week","native-country","income"]

print(data.info())
print(data.describe())
print(data.isnull().sum())
print()
print(data.isin(['?']).sum(axis=0))
data["native-country"] = data["native-country"].replace("?",np.nan)
data.dropna(how="any", inplace=True) # any= means it drops the row if any single column in the row is na  all= Drops the row if every column in the row is na
print("------------------------")
print(data.columns)
print("------------------------")
for i in data.columns:
    print('---%s---'%i)
    print(data[i].value_counts())
    # educational-num, age, hours-per-week, fnlwgt, capital-gain, capital-loss, native-country

# mapping and plotting
    