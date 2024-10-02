 #Import Primary Modules:
import numpy as np
import pandas as pd
#%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import folium as flm

# # x=np.random.normal(loc=0,scale=1,size=1000)
# plt.hist(x,100)
# # plt.title('Normal distribution with $\mu=0, \sigma=1$')
# # plt.savefig('matplotlib_histogram.png')
# # plt.show()
import requests
import io
# from js import fetch


URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
resp = requests.get(URL)
text = io.StringIO(resp.text)
df = pd.read_csv(text)
print('Data downloaded and read into a dataframe!')

# #df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')
# #print('Data read into a pandas dataframe!')                
# #df_can.head()

print(df.describe())
print(df.columns)
#years = np.arange(1980, 2023)
#years = list(map(str, range(1980, 2014)))
#create data for plotting

    
#Create dataframes for recession and non-recession period
rec_data = df[df['Recession'] == 1]

sizes=rec_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().values
plt.figure(figsize=(10, 6))
plt.pie(sizes, labels=rec_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().index,startangle=90,autopct='%1.1f%%')        



#plt.xlabel('Price')
#plt.ylabel('Automobile Sales')
plt.title('Share of Each Vehicle Type in Total Expenditure during Recessions')

plt.savefig('Pie_2.png')

plt.show()