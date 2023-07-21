import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-f2', '--file2')
parser.add_argument('-c', '--columnName')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter first filename (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter second filename (including \'.csv\'): ')
if args.columnName:
    columnName = args.columnName
else:
    columnName = input('Enter column to merge on: ')


df_1 = pd.read_csv(filename, header=0, dtype={columnName: str})
print(df_1.columns)
df_2 = pd.read_csv(filename2, header=0, dtype={columnName: str})
print(df_2.columns)
df_2[columnName] = df_2[columnName].astype(str)
df_2[columnName] = df_2[columnName].str.strip()
df_1[columnName] = df_1[columnName].astype(str)
df_1[columnName] = df_1[columnName].str.strip()

frame = pd.merge(df_1, df_2, how='left', on=[columnName], suffixes=('_1', '_2'))

# frame = frame.reindex(sorted(frame.columns), axis=1)
# frame.drop_duplicates(inplace=True)
# print(frame.columns)
print(frame.head)
dt = datetime.now().strftime('%Y-%m-%d')
frame.to_csv(filename[:-4]+'_'+dt+'.csv', index=False)