import pandas as pd

data = pd.read_csv("hosptial_location.csv")
data = data.dropna(subset=['location'])
print(data)

data = data['location'].str.split(', ', 1).tolist()

update_data = []

for loc in data:
    [float(i) for i in loc[::-1]]
    update_data.append([float(i) for i in loc[::-1]])

print(update_data)