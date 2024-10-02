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
#years = np.arange(1980, 2024)
#years = list(map(str, range(1980, 2014)))
#create data for plotting
df_rec = df[df['Recession']==1]
df_Mline = df_rec.groupby(['Year','Vehicle_Type'], as_index=False)['Automobile_Sales'].sum().reset_index()
df_Mline.set_index('Year', inplace=True)
df_Mline = df_Mline.groupby(['Vehicle_Type'])['Automobile_Sales']

#create figure
plt.figure(figsize=(10, 6))
df_Mline.plot(kind='line')

#plt.annotate('1991 Recession', xy=(1990.8, 787), xytext=(1987, 1311), arrowprops=dict(facecolor='red', shrink=0.05))
#plt.annotate('end 2007-mid 2009 Recession', xy=(2007, 1388), xytext=(1998, 530), arrowprops=dict(facecolor='red', shrink=0.05))
#plt.text(1990.8, 787, '1991 Recession')
#plt.text(2007, 1388, 'end 2007-mid 2009 Recession')

plt.xlabel('Year')
#plt.xticks(years, rotation=90)
plt.ylabel('Sum of Automobile Sales per Year')
plt.title('Sales Trend Vehicle-wise during Recession')
plt.legend(title = 'Vehicle Type');
plt.savefig('Line_Plot_2.png')
plt.show()

