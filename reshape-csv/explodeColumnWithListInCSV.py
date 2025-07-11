"""Takes a column where each cell contains multiple values, and creates a new row for each value, duplicating its original identifier."""

import pandas as pd
import argparse
from datetime import datetime
import ast
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-c', '--column_name')
parser.add_argument('-d', '--delimiter')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.column_name:
    column_name = args.column_name
else:
    column_name = input('Enter column to explode: ')
if args.delimiter:
    delimiter = args.delimiter
else:
    delimiter = input('Enter delimiter of string list: ')


df = pd.read_csv(filename, header=0)
# If column is formatted as string.
df[column_name] = df[column_name].str.split(delimiter)

# If column is formatted as list.
# df[column_name] = df[column_name].apply(ast.literal_eval)
df.reset_index()
df = df.explode(column_name)

print(df.columns)
print(df.head)
dt = datetime.now().strftime('%Y-%m-%d%H.%M.%S')
new_filename = column_name+'Exploded_'+dt+'.csv'
df.to_csv(new_filename, index=False, quoting=csv.QUOTE_ALL)
