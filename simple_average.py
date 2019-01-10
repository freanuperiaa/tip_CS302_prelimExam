import pandas
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

#Simple Average Forecasting

#take values from the CSV
df = pandas.read_csv("ph_peso_dollar.csv")
print(df)
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
#manipulation of data frames
actual_data = list(df.iloc[1:13,2])

print(actual_data)
actual_data.reverse()
#implementation of "simple average"
sum = 0
for x in actual_data:
    sum += x
average = sum/len(actual_data)
print(average)

#plotting in graph
style.use('seaborn-whitegrid')
fig = plt.figure()
plt.plot(months, actual_data, label = "actual rate")
plt.axhline(y = average, color = 'r', linestyle='-')
plt.xlabel('Month')
plt.ylabel('Dollar to Peso rate')
plt.title('prediction of dollar-to-peso rate using "Simple Average" Forecasting')
plt.legend()
plt.show()