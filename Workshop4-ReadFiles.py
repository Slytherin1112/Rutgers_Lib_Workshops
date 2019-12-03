#Read file in the same folder with pandas
#Users/apple/Desktop/Work&Legal/RutgersLibrary/Python

import pandas as pd
import ssl #Secure Sockets Layer

ssl._create_default_https_context = ssl._create_unverified_context
'''
df = pd.read_csv('Credit.csv')

#Read file from a different directory
#Users/apple/Desktop/Notes/RealGDP.csv
GDP = pd.read_csv("../../../Notes/RealGDP.csv")
print(GDP,df)
'''

#Get file from URL
url="https://raw.githubusercontent.com/Slytherin1112/Rutgers_Lib_Workshops/master/gapminder_gdp_americas.csv"
c=pd.read_csv(url)
print (c)