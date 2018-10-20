import csv
import urllib.request

url = "https://raw.github.com/datasets/gdp/master/data/gdp.csv"
webpage = urllib.request.urlopen(url)
datareader = csv.reader(webpage.read().decode('utf-8').splitlines())
data = []
for row in datareader:
    data.append(row)

for row in data:
    print(row[2],row[3])
