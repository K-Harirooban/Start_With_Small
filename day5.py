import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv(r"C:\Users\acer\Videos\Retail sales analytics and businesss intelligence\Sample - Superstore.csv",encoding='latin1')

print(df.columns.tolist())

# Bar chart — Sales by category Which product category generates the highest sales?

category_sales = df.groupby("Category")["Sales"].sum()

plt.bar(category_sales.index,category_sales.values)

plt.title("Sales by Category")

plt.xlabel("Category")

plt.ylabel("Total Sales")

plt.show()

#Line chart — Monthly sales trend Are sales increasing or decreasing over time convert the date column and extract the month.

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

print(monthly_sales)

plt.figure(figsize=(12,5))

plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker = "o"
)

plt.title("Monthly sales trend :")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()
