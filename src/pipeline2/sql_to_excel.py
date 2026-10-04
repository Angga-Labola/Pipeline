import pandas as pd

from db_conn import engine

query = "SELECT * from customers"

file_path = r"C:\Users\ASUS\OneDrive\Documents\python project\pipeline2\output\ "

df = pd.read_sql(query,engine)
df.to_excel(f"{file_path} customers2.xlsx", index = False)
print('Successful 100%')