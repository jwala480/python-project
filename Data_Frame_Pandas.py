# Program using DataFrame concept with possible operations
import pandas as pd
data= {"Name":["Dilly","Pavan","Nikhil"],"Maths":[90,99,85],"Python":[90,95,89]}
df = pd.DataFrame(data)
print(df)
# Printing only Name column
print(df["Name"])
#Adding another column name Total
df["Total"] = df["Maths"] + df["Python"]
print(df)
#To find max marks in Total column
max_marks = df["Total"].max()
topper = df[df["Total"]==max_marks] 
print("Topper of the class:",topper)
#Adding another column name Average
df["Average"] = df["Total"]/2
#To find highest score based on Average
high_scores = df[df["Average"]>80]
print("Students with Average > 80:\n",high_scores)
# Sorting the values in Total column
sorted_df = df.sort_values(by="Total",ascending=False)
# To find topper in given DataFrame
topper= df.sort_values(by="Total",ascending=False).iloc[0]
print("Sorted DataFrame:",sorted_df)
top2 = sorted_df.iloc[0:2]
print("Top Two members :",top2)