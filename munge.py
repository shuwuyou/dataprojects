# place your code to clean up the data file below.
import pandas as pd
import numpy as np

df =  pd.read_csv("data/nyc_hotspot.csv")

#delete unnecessary columns
df = df.drop(df.columns[[1, 8, 9, 12, 13, 14, 15, 18, 20, 22, 23, 24, 25, 26, 27, 28]], axis=1)

#replace missing value with nan
df.fillna("NaN", inplace=True)

#output to a new clean csv file
df.to_csv("data/clean_data.csv", index=False)

