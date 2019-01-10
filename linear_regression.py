import pandas
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
#      Linear Regression Line
#   this type of forecasting uses the previous data (n-1)
#   to predict the next outcome (n-1)


#take values from the CSV
df = pandas.read_csv("ph_peso_dollar.csv")
print(df)
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
#manipulation of data frames
actual_data = list(df.iloc[1:13,2])
predicted = np.zeros(12)
actual_data.reverse()
mnths = [1,2,3,4,5,6,7,8,9,10,11,12]
#making the regression line
sum_xtimesy = 0
for index, value in enumerate(mnths):
    sum_xtimesy += mnths[index] * actual_data[index]
#
sum_x = 0
for x in mnths:
    sum_x += x
#
sum_y = 0
for x in actual_data:
    sum_y += x
#
sum_x_squared = 0
for x in mnths:
    sum_x_squared += x*x 
#
print(sum_xtimesy,sum_x,sum_y,sum_x_squared)

numerator = (12* sum_xtimesy) - sum_x*sum_y
denominator =  (12* sum_x_squared) - (sum_x*sum_x)
b = numerator/ denominator
print(b)

a = (sum_y - (b*(sum_x)))/12
print(a)
predicted = []
for x in mnths:
    predicted.append(x*b + a)

#plotting in graph
style.use('seaborn-whitegrid')
fig = plt.figure()
plt.plot(months, actual_data, marker = 'o',label = "peso-dollar rate")
plt.plot(months, predicted ,marker = 'o', label = 'forecasted amount')
plt.xlabel('Year')
plt.ylabel('Carbon emission in kilotonnes(kt)')
plt.title('Peso-Dollar Exchange Rate in 2014 using Regression Line ')
plt.legend()
plt.show()