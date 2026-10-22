import pandas as pd 
# load original data 
df = pd.read_csv(r"C:\Users\acer\Videos\Retail sales analytics and businesss intelligence\Sample - Superstore.csv", encoding= 'latin1')

# check the size of an data
print("Original size :", df.shape)

#inspect missing values
print("Missing values before cleaning")
print(df.isnull().sum())

# Remove exact duplicate rows
df = df.drop_duplicates()

#convert order date if it present like text to date format
if "Order Date" in df.columns:
    df["Order Date"] = pd.to_datetime(df["Order Date"]
,errors= "coerce")

# inspect Numerical columns 
print("Numerical summary")
print(df.select_dtypes(include="number").describe())

#saved a cleaned data set
df.to_csv(r"C:\Users\acer\Videos\Retail sales analytics and businesss intelligence\Sample - Superstore.csv", encoding= 'latin1', index=False)

print("\nCleaned Shape:", df.shape)
print("Cleaned dataset saved ")



