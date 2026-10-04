import pandas as pd

from db_conn import engine

file_path = r"c:\Users\ASUS\Downloads\FSI-2023-DOWNLOAD.xlsx"
table_name = 'data_FSI'

df = pd.read_excel(file_path)

df.to_sql(
    name=table_name, 
    con=engine, 
    if_exists='replace',
    index = False
)

print('Successful 3000%')