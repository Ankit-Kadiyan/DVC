import pandas as pd

Data=[
    {'name':'Sunny','age':28,'city':'Bhopal'},
    {'name':'Sudhasnshu','age':33,'city':'Delhi'},
    {'name':'Krish','age':35,'city':'Benglore'},
    {'name':'Vikas','age':29,'city':'Pune'},
]

data=pd.DataFrame(Data)

data.to_csv("data/data.csv",index=False)
