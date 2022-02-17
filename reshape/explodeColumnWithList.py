import pandas as pd
import argparse
from datetime import datetime
import ast

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
    columnName = input('Enter column to explode: ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

df = pd.read_csv(filename, header=0)
# If column is formatted as string.
df[columnName] = df[columnName].str.split(',')

# If column is formatted as list.
# df[columnName] = df[columnName].apply(ast.literal_eval)
df.reset_index()
df = df.explode(columnName)

print(df.columns)
print(df.head)
df.to_csv(path_or_buf=columnName+'Exploded_'+dt+'.csv')
