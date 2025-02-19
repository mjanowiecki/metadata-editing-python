"""Gets the sum (sum of values) and size (total count of non-empty value)
of each unique value in a specific column."""

import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-c', '--column_name')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.column_name:
    column_name = args.column_name
else:
    column_name = input('Enter column to check: ')

df_1 = pd.read_csv(filename, header=0)

unique_1 = df_1[column_name].unique()
unique_1 = list(unique_1)
group = df_1.groupby([column_name]).sum()
group2 = df_1.groupby([column_name]).size()
group = group.reset_index()
group2 = group2.reset_index()
print(group2.head)
frame = pd.merge(group, group2, how='left', on=[column_name])

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
frame.to_csv(path_or_buf='stats_'+dt+'.csv', index=False)
print(len(unique_1))
print(unique_1)
