import pandas as pd
import argparse
from datetime import datetime
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-f2', '--file2')
parser.add_argument('-c', '--column_name')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter first filename (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter second filename (including \'.csv\'): ')
if args.column_name:
    column_name = args.column_name
else:
    column_name = input('Enter column to merge on: ')


df_1 = pd.read_csv(filename, dtype=object)
print(df_1.columns)
df_2 = pd.read_csv(filename2, dtype=object)
print(df_2.columns)
df_2[column_name] = df_2[column_name].astype(str)
df_2[column_name] = df_2[column_name].str.strip()
df_2[column_name] = df_2[column_name].str.strip("'")
df_1[column_name] = df_1[column_name].astype(str)
df_1[column_name] = df_1[column_name].str.strip()
df_1[column_name] = df_1[column_name].str.strip("'")

frame = pd.merge(df_1, df_2, how='outer', on=[column_name], suffixes=('_1', '_2'))

# frame = frame.reindex(sorted(frame.columns), axis=1)
frame.drop_duplicates(inplace=True)
# print(frame.columns)
print(frame.head)
dt = datetime.now().strftime('%Y-%m-%d')
frame.to_csv(filename[:-4]+'_'+dt+'.csv', index=False, quoting=csv.QUOTE_ALL)
