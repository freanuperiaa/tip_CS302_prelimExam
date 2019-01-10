import pandas
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

#Forecasting seasonality

#take values from the CSV (note that the CSV is comma-delimited)
df = pandas.read_fwf("worldbank_co2emission/API_EN.ATM.CO2E.KT_DS2_en_csv_v2_10224872.csv")
data =df.iloc[187]              #take the data in the 187th row
s = data[0]                     #put to string the 0th element in data list
s = s.replace('"','')           #remove the double quotes in every element
actual_data = s.split(',')      #make a list, 'actual data', by splitting the string s by the commas

for x in range(4):
    actual_data.pop(0)          #remove the first four elements, which is just some useless labels
for x in range(4):
    actual_data.pop(55)         #remove the trailing empty strings
actual_data = list(map(float, actual_data))     #convert the strings to numbers (the numbers in the list are enclosed by '')
print(actual_data)
print(len(actual_data))
#make a list for the years 
years = [ i for i in range(1960, 2015) ]


yrs = np.zeros(len(years))
num = 1
for index, value in enumerate(yrs):
    yrs[index] = num
    num += 1
#taking the slope (y = a + bt)
#taking the summation values...
sum_xtimesy = 0
for index, value in enumerate(yrs):
    sum_xtimesy += yrs[index] * actual_data[index]
#
sum_x = 0
for x in yrs:
    sum_x += x
#
sum_y = 0
for x in actual_data:
    sum_y += x
#
sum_x_squared = 0
for x in yrs:
    sum_x_squared += x*x 
#
numerator = (55* sum_xtimesy) - sum_x*sum_y
denominator =  (55* sum_x_squared) - (sum_x*sum_x)
b = numerator/ denominator
print(b)
#taking the y - intercept (y= a + bt)
a = (sum_y - (b*(sum_x)))/55
print(a)
#taking the seasonal relatives (every decade, for half a century)
cycle1 =[]
cycle2 =[]
cycle3 =[]
cycle4 =[]
cycle5 =[]
for index,value in enumerate(actual_data):
    if 0<=index<=9:
        cycle1.append(value)
    elif 10<=index<=19:
        cycle2.append(value)
    elif 20<=index<=29:
        cycle3.append(value)
    elif 30<=index<=39:
        cycle4.append(value)
    elif 40<=index<=49:
        cycle5.append(value)
    else:
        pass
averages = {
    1:0, 2:0, 3:0, 4:0, 5:0,
    6:0, 7:0,8:0, 9:0, 10:0
}
for x in [cycle1,cycle2,cycle3,cycle4,cycle5]:
    for index, value in enumerate(x):
        averages[index+1] += value

wantuten = [1,2,3,4,5,6,7,8,9,10]
for x in wantuten:
    averages[x] = averages[x]/5
grand_average = 0
for x in wantuten:
    grand_average += averages[x]
grand_average = grand_average/10
for x in wantuten:
    averages[x] = averages[x]/grand_average
print(averages)

#combining the linear trend line and seasonality
forecasting_seasonality = np.zeros(55)
for index, value in enumerate(forecasting_seasonality):
    forecasting_seasonality[index] = a + b * yrs[index]

for index, value in enumerate(forecasting_seasonality):
    forecasting_seasonality[index] = forecasting_seasonality[index] * averages[wantuten[index%10]]


#plotting in graph
style.use('seaborn-whitegrid')
fig = plt.figure()
plt.plot(years, actual_data, marker = 'o',label = "actual amount of emission")
plt.plot(years, forecasting_seasonality, marker = 'o', label = "forecasted amount")
plt.xlabel('Year')
plt.ylabel('Carbon emission in kilotonnes(kt)')
plt.title('Forecast of Carbon emisssion of Philippines from 1960 to 2014 using Forecasting Seasonality ')
plt.legend()
plt.show()