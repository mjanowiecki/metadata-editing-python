"""Get any values duplicated in two columns in a CSV."""

import argparse
from datetime import datetime
import pandas as pd
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-c', '--column1')
parser.add_argument('-c2', '--column2')
parser.add_argument('-id', '--identifier')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.column1:
    column1 = args.column1
else:
    column1 = input('First column: ')
if args.column2:
    column2 = args.column2
else:
    column2 = input('Second column: ')
if args.identifier:
    identifier = args.identifier
else:
    identifier = input('Enter name of identifier columns: ')

columnsToCompare = [column1, column2]

df = pd.read_csv(filename)
df_subset = df[columnsToCompare + identifier]

duplicated_values = []
for index, row in df_subset.iterrows():
    valuesToCompare = []
    for column in columnsToCompare:
        value = str(row[column]).strip()
        valuesToCompare.append(value)
    totalValues = len(valuesToCompare)
    unique = len(set(valuesToCompare))
    if unique != totalValues:
        duplicated_values.append(row)


df_updated = pd.DataFrame.from_records(duplicated_values)
print(df.head(15))
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
filename = filename[:-4]
new_filename ='duplicatedValuesIn'+filename+'_'+dt+'.csv'
df_updated.to_csv(new_filename, index=False, quoting=csv.QUOTE_ALL)
