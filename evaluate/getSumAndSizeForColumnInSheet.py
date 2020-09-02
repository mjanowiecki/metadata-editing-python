import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-c', '--columnName')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.columnName:
    columnName = args.columnName
else:
    columnName = input('Enter column to check: ')

df_1 = pd.read_csv(filename, header=0)

unique_1 = df_1[columnName].unique()
unique_1 = list(unique_1)
group = df_1.groupby([columnName]).sum()
group2 = df_1.groupby([columnName]).size()
group = group.reset_index()
group2 = group2.reset_index()
print(group2.head)
frame = pd.merge(group, group2, how='left', on=[columnName])

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
frame.to_csv(path_or_buf='stats_'+dt+'.csv', index=False)
print(len(unique_1))
print(unique_1)
