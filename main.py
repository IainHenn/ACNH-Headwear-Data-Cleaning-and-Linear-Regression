import pandas as pd

#Reading in CSV file 
df = pd.read_csv(r"C:\Users\Iaine\.vscode\Python Projects\ACNH Project\ACNH Items\headwear.csv")
print(df.head())

#Turning source into a string 
df["Source"] = df["Source"].astype("string")
print(df.dtypes)

#Top 5 highest selling headwear that can only be crafted 
top_selling_headwear_df = df.loc[(df['Sell'] > 500) & (df['Source'] != "Able Sisters")].sort_values(by = "Sell", ascending = False).head(5)
print(top_selling_headwear_df.filter(items = ["Name","Sell","Source"]))




#Turning buy into a string 
df["Buy"] = df["Buy"].astype("string")
print(df.dtypes)

#Turning "Not For Sale" items to price of 0 
df["Buy"] = df["Buy"].replace("NFS","0")

#Top 5 most expensive headwear to buy 
most_expensive_headwear_items = df.sort_values(by = "Buy", ascending = False).head(5)
print(most_expensive_headwear_items.filter(items = ["Name","Buy","Sell"]))