"""Takes a column where each cell contains multiple values, and creates a new row for each value, duplicating its original identifier."""

import pandas as pd
import argparse
from datetime import datetime
import ast
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
    column_name = input('Enter column to explode: ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

df = pd.read_csv(filename, header=0)
# If column is formatted as string.
df[column_name] = df[column_name].str.split('|')

# If column is formatted as list.
# df[column_name] = df[column_name].apply(ast.literal_eval)
df.reset_index()
df = df.explode(column_name)

print(df.columns)
print(df.head)
df.to_csv(path_or_buf=column_name+'Exploded_'+dt+'.csv', index=False, quoting=csv.QUOTE_ALL)
