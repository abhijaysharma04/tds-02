import pandas as pd
import os

# Define the folder path
folder = r"C:\TDS-02\RollNo_23f3002675\Assignment_1\workdir\q-unicode-data"

# Define the target symbols
target_symbols = {'€', 'Ž', 'Š'}

# Initialize total sum
total = 0.0

# File 1: CP-1252 encoded CSV
file1 = os.path.join(folder, 'data1.csv')
df1 = pd.read_csv(file1, encoding='cp1252')
total += df1[df1['symbol'].isin(target_symbols)]['value'].sum()

# File 2: UTF-8 encoded CSV
file2 = os.path.join(folder, 'data2.csv')
df2 = pd.read_csv(file2, encoding='utf-8')
total += df2[df2['symbol'].isin(target_symbols)]['value'].sum()

# File 3: UTF-16 encoded TSV (tab-separated)
file3 = os.path.join(folder, 'data3.txt')
df3 = pd.read_csv(file3, sep='\t', encoding='utf-16')
total += df3[df3['symbol'].isin(target_symbols)]['value'].sum()

# Final result
print(f"\n✅ Sum of values for symbols € / Ž / Š = {total}")
