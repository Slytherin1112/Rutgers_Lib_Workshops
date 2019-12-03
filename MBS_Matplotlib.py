import matplotlib.pyplot as plt
import pandas as pd
import ssl #Secure Sockets Layer

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/Slytherin1112/Rutgers_Lib_Workshops/master/gapminder_gdp_oceania.csv"
data = pd.read_csv(url, index_col='country')

# Extract year from last 4 characters of each column name
years = data.columns.str.strip('gdpPercap_')

data.columns = years.astype(int)

#Get Australia data from dataframe using matplotlib.plot function directly.
years = data.columns
gdp_australia = data.loc['Australia']

plt.plot(years, gdp_australia, 'g-')
plt.show()