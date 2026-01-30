import pandas as Pd
df = Pd.read_csv('user_data.csv')
print(df['Usernames'])
print(df.iloc[1][['Usernames', 'Passwords']])
sorted_usernames = df.sort_values('Usernames')
print(sorted_usernames)
sorted_passwords = df.sort_values('Passwords',ascending=False)
print(sorted_passwords)