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
non_rec_data = df[df['Recession'] == 0]
    
#Figure
fig=plt.figure(figsize=(12, 6))
    
#Create different axes for subploting
ax0 = fig.add_subplot(1, 2, 1) # add subplot 1 (1 row, 2 columns, first plot)
ax1 = fig.add_subplot(1, 2 ,2 ) # add subplot 2 (1 row, 2 columns, second plot). 
    
#plt.subplot(1, 2, 1)
sns.lineplot(x='Year', y='GDP', color='red', data=rec_data, label='Recession', ax=ax0)
ax0.set_xlabel('Year')
ax0.set_ylabel('GDP')
ax0.set_title('GDP Variation during Recession Period')
    
#plt.subplot(1, 2, 2)
sns.lineplot(x='Year', y='GDP', color='green', data=non_rec_data , label='non-Recession',ax=ax1)
ax1.set_xlabel('Year')
ax1.set_ylabel('GDP')
ax1.set_title('GDP Variation during non-Recession Period')
plt.tight_layout()    
plt.show()



plt.savefig('Subplot1.png')

