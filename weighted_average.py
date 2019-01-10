import pandas
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

#Weighted Average

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

#weighted moving average forecast
#alphas: 1=0.4;2=0.3;3=0.2;4=0.1

#Weighted moving average forecast
wma = np.zeros(55)
for index, value in enumerate(actual_data):
    if index in [0,1,2,3]:
        wma[index] = None
    else:
        wma[index] = (  
                (actual_data[index-1]*0.4) + (actual_data[index-2]*0.3 ) +  
                (actual_data[index-3]*0.2) + (actual_data[index-4]*0.1)  
                )

#plot in graph

#plotting in graph
style.use('seaborn-whitegrid')
fig = plt.figure()
plt.plot(years, actual_data, marker = 'o',label = "actual amount of emission")
plt.plot(years, wma,marker = 'o', label = 'forecasted amount')
plt.xlabel('Year')
plt.ylabel('Carbon emission in kilotonnes(kt)')
plt.title('Forecast of Carbon emisssion of Philippines from 1960 to 2014 using Weighted Moving Average Forecasting Technique')
plt.legend()
plt.show()