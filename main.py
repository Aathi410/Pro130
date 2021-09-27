import pandas as pd
import csv

df = pd.read_csv("final.csv")

del df["Luminosity"]
del df["Name.1"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]
del df["Unnamed: 0"]
del df["Unnamed: 6"]

print(df.shape)
print(list(df))

df.to_csv('main.csv') 