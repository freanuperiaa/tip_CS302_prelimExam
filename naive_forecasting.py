import pandas
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
#      Naive Forecasting 
#   this type of forecasting uses the previous data (n-1)
#   to predict the next outcome (n-1)


#take values from the CSV
df = pandas.read_csv("ph_peso_dollar.csv")
print(df)
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
#manipulation of data frames
actual_data = list(df.iloc[1:13,2])
actual_data.reverse()
predicted = np.zeros(12)
#naive forecast
ctr = 1
for x in actual_data:
    try:
        predicted[ctr] = x
        ctr += 1
    except:
        pass

predicted[0] = None

#plotting in graph
style.use('seaborn-whitegrid')
fig = plt.figure()
plt.plot(months, actual_data, label = "actual rate")
plt.plot(months, predicted, label = "predicted rate ")
plt.xlabel('Month')
plt.ylabel('Dollar to Peso rate')
plt.title('prediction of dollar-to-peso rate using Naive Forecasting')
plt.legend()
plt.show()


