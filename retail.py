import pandas as pd 
# load the csv file
df = pd.read_csv(r"C:\Users\acer\Videos\Retail sales analytics and businesss intelligence\Sample - Superstore.csv", encoding='latin1')
#display the 10 rows 
print(df.head(20))
#display and checks the number of rows and coloumns 
print(df.shape)
#display the columns names  they have
print(df.columns)
#check data types and missing values
df.info()
