#Let's start by importing the pandas library.
import pandas as pd
#We can read the CSV file "outbreaks.csv" in as a DataFrame for easier manipulation.
df = pd.read_csv('outbreaks.csv')

#For convenience, pandas DataFrames have methods called head() and tail()
## which display the first few or last few rows, respectively (default # of rows = 5).
'''
df.head()
# Showing the last 10 rows
df.tail(10)
#What are all the column names in this table?
print(df.columns)
#How many rows/columns are in this table?
print(df.shape)

#You can get this information along with information about the data types present using the info() method.
df.info()



#We can get summary statistics of the columns with numerical data using the describe() method.
df.describe()


#What "species" were responsible for outbreaks over the course of the years covered in this dataset?
print(df['Year'].unique())
#No result 

'''
'''
#What if we want to only deal with outbreaks that happened in New Jersey?
print(df[df['State'] == 'New Jersey'])

#Subsets of DataFrames can be assigned to variables,
#just as DataFrames can be assigned to variables:
nj = df[df['Location'] == 'Restaurant']
print(nj.head(9))

#We can choose to only look at certain columns in the DataFrame:
df[['Year', 'Illnesses']].head(10)

#What if we only want to focus on certain rows?
print(df[10:20])
'''
#We can also sort the rows by a chosen column.
#What were the top 5 outbreaks in terms of fatalities?
#print(df.sort_values(by='Illnesses', ascending=True).head(200))

#How many outbreaks occurred each year?
print(df.groupby('Year').size())
