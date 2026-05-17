import pandas as pd
import sqlite3

df = pd.DataFrame({
    "name": ["John", "Mike", "Sara"],
    "country": ["us", "canada", "us"],
    "salary": [104, 450, 0]
})

# Remove duplicates
df = df.drop_duplicates()

print(df)

# Fill null values in salary
df['salary'] = df['salary'].fillna(30)

print(df['salary'])

# Fill remaining nulls with mean
df['salary'] = df['salary'].fillna(df['salary'].mean())

print(df)

# Group by country and calculate average salary
Df = df.groupby('country')['salary'].mean()

print(Df)
df["department"] = "IT"
print(df)
df["salary"]=df["salary"]* 0.5
df["department"]=df["department"].replace('IT','CS')
print(df)
df["department"]=df["department"].replace('CS','IT')
print(df)
df["status"] = df["salary"].apply(
    lambda x: "High" if x > 200 else "Low"
)
print(df)
df.loc[df["salary"]==0,"salary"]=1500
print(df)
Avg=df.groupby('country')['salary'].mean()
print(Avg)
print(df)
df.to_csv("result.csv",index=False)
print(df)
gr=df[df['salary']>200]
print(gr)
gr.to_csv("High.csv",index=False)