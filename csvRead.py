import pandas as pd
import matplotlib.pyplot as plt
url = "https://data.cityofnewyork.us/api/views/kku6-nxdu/rows.csv"
data=pd.read_csv(url)
total_rows = data['JURISDICTION NAME'].count
data.plot.scatter(x='PERCENT PUBLIC ASSISTANCE TOTAL',y='JURISDICTION NAME')
plt.show()
#print(data)