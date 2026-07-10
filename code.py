import pandas as pd 
import os

data={
    "name" : ["adi","dev","kartik"],
    "age" : [12,45,67],
    "id" : [100,101,102]
}

df=pd.DataFrame(data)

dir_name='data'
dir1=os.makedirs(dir_name,exist_ok=True)

file_path=os.path.join(dir_name,'student.csv')

df.to_csv(file_path,index=False)

print(f"CSV file saved at {file_path}")

