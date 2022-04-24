import csv

from google.colab import files
data_to_load= files.upload()

rows=[]
with open("main2.csv") as file:
  csvreader=csv.reader(file)
  for row in csvreader:
    rows.append(row)

headers=rows[0]
planet_data_rows=rows[1:]
print(headers)
print(planet_data_rows[0])

import plotly.express as px
planet_masses = []
planet_radiuses = []
planet_names = []
for planet_data in planet_data_rows:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  planet_names.append(planet_data[1])
planet_gravity = []

for index, name in enumerate(planet_names):
  gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
  planet_gravity.append(gravity)

fig = px.scatter(x=planet_radiuses, y=planet_masses, size=planet_gravity, hover_data=[planet_names])
fig.show()
print(gravity)

