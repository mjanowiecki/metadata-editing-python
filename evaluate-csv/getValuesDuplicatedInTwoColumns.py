"""
Get any values duplicated in two columns in a sheet.
"""

import argparse
from datetime import datetime
import pandas as pd
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

columnsToCompare = ['old_description', 'new_description']
identifier = ['dc.identifier.uri']

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


df = pd.DataFrame.from_records(duplicated_values)
print(df.head(15))
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
df.to_csv('duplicatedValues_'+dt+'.csv', index=False, quoting=csv.QUOTE_ALL)
