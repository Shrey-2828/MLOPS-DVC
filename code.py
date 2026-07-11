import pandas as pd 
import os

data={
    "name" : ["adi","dev","kartik"],
    "age" : [12,45,67],
    "id" : [100,101,102]
}

df=pd.DataFrame(data)

new_row_loc = {'name': 'GF1', 'age': 20, 'id': 103}
df.loc[len(df.index)] = new_row_loc

new_row_loc = {'name': 'GF2', 'age': 27, 'id': 104}
df.loc[len(df.index)] = new_row_loc


dir_name='data'
dir1=os.makedirs(dir_name,exist_ok=True)

file_path=os.path.join(dir_name,'student.csv')

df.to_csv(file_path,index=False)

print(f"CSV file saved at {file_path}")


