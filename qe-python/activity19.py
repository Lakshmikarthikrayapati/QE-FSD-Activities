import pandas as pd
data = {
    "FirstName": ["Satvik", "Avinash","Lahri"],
    "LastName": ["Shah","Kati","Rath"],
    "Emale": ["satshah@example.com","avinashk@example.com","lahri.rath@example.com"],
    "PhoneNumber": [123456, 234567, 345678]
}
df = pd.DataFrame(data)
df.to_excel("output.xlsx", index=False)