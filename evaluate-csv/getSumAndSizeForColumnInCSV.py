"""Gets the sum (sum of values) and size (total count of non-empty value)
of each unique value in a specific column."""

import pandas as pd
import argparse
from datetime import datetime
import csv

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

df = pd.read_csv(filename, header=0)

unique_1 = df[column_name].unique()
unique_1 = list(unique_1)
group = df.groupby([column_name]).sum()
group2 = df.groupby([column_name]).size()
group = group.reset_index()
group2 = group2.reset_index()
print(group2.head)
frame = pd.merge(group, group2, how='left', on=[column_name])

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
filename = filename[:-4]
new_filename = 'statsFor'+filename+'_'+dt+'.csv'
frame.to_csv(new_filename, index=False, quoting=csv.QUOTE_ALL)
print(len(unique_1))
print(unique_1)
