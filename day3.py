import pandas as pd 

#load the cleaned data set
df = pd.read_csv(r"C:\Users\acer\Videos\Retail sales analytics and businesss intelligence\Sample - Superstore.csv",encoding='latin1')

# display the default first five rows
print(df.head())

# just for the use case of see the column names to access 
print(df.columns.to_list())

# i wanna see those columns values 
print(df[["Category","Profit","Sales"]])

# i wanna see the only orders with sales above 500
high_sales = df[df["Sales"]>500]
print(high_sales.head())

# lets try to display the profitable and big orders and loss orders
print("profitable :")
profitable = df[df["Profit"]>0]
print(profitable.head())

print("big_orders :")
big_orders = df[df["Profit"]>1000]
print(big_orders.head())

print("loss_orders :")
loss_orders = df[df["Profit"]<0]
print(loss_orders.head())

# lest try to figure the total sales and total profit
print("Total sales :")
print(df["Sales"].sum())

print("Total profit :")
print(df["Profit"].sum())

# we gonna use new function that helps a lot that name of the functions is groupby that is used to group the value by the some od the category
print("grouped :")
grouping = df.groupby("Category")["Sales"].sum()
print(grouping)

# lets categorize the both profit and sales together by "groupby"
category_summary = df.groupby("Category").agg(
    total_sales = ("Sales", "sum"),
    total_profit = ("Profit","sum")
)
print(category_summary)

#lets sort the total sales
category_summary = category_summary.sort_values(
    by = "total_sales",
    ascending=False
)
print(category_summary)

# we gonna categorize by the region column
region_summary = df.groupby("Region").agg(
    total_sales  = ("Sales","sum"),
    total_profit = ("Profit", "sum")
)
print(region_summary)

region_summary = region_summary.sort_values(
    by="total_profit",
    ascending=True
)
print(region_summary)
