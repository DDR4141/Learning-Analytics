import pandas as pd
import numpy as np

df = pd.read_csv("ultimate_student_productivity_dataset_5000.csv")
#%% Работа с дубликатами
print(f" До удаления дубликатов. Rows: {df.shape[0]}, Columns: {df.shape[1]}")

df = df.drop_duplicates()
print(f" После удаления дубликатов. Rows: {df.shape[0]}, Columns: {df.shape[1]}")
#%% Работа с пропусками
print(df.isnull().sum().sum())