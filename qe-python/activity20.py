import pandas as pd

df = pd.read_excel('output.xlsx')
print("Number of rows & columns:", df.shape)
print(df['emails'])
sorted_df = df.sort_values(by='FirstName')
print(sorted_df)