import pandas as pd 
df = pd.read_csv(r"C:\Users\acer\Videos\Retail sales analytics and businesss intelligence\Sample - Superstore.csv",encoding='latin1')
# just for the use case of see the column names to access 
print(df.columns.to_list())

#“Show me the 10 orders with the highest sales.”
top_orders = df.sort_values(
    by = "Sales",
    ascending=False
)
print(top_orders.head(10))

#Imagine you want to know how many orders belong to each product category.
print(df["Category"].value_counts())

#Calculate multiple business metrics Let's build a more useful category summary.
category_summary = df.groupby("Category").agg(
    total_sales = ("Sales","sum"),
    total_profit = ("Profit","sum"),
    average_sales = ("Sales","mean"),
    order_count = ("Order ID","nunique")
)
print(category_summary)

#Calculate profit margin
category_summary["profit_margin"] = (
    category_summary["total_sales"]/category_summary["total_profit"]
)*100

print(category_summary.sort_values(
    by="profit_margin",
    ascending=False
))

#Let's combine the techniques we've learned.
print(
    df.groupby("Product Name")["Sales"]   
      .sum()
      .sort_values(ascending=False)
      .head(10)
      )

#Which products have the greatest total losses?
product_profit =(
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values(ascending = False)

    ) 

print(product_profit.head(10))

#Which region generates the most profit?
region_profit = (df.groupby("Region")["Profit"].sum())
print(region_profit.sort_values().head(10))


