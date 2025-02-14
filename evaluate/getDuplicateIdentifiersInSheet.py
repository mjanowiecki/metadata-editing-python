"""
Finds all identifiers in a spreadsheet that appear more than 1 time in the identifier column.
Creates a new spreadsheet containing all the rows with duplicated identifiers.
"""

import argparse
import pandas as pd
from datetime import datetime
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-id', '--identifier')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.identifier:
    identifier = args.identifier
else:
    identifier = input('Enter name of identifier columns: ')

df = pd.read_csv(filename, dtype='string')

duplicates = df.duplicated(subset=[identifier], keep=False)

duplicate_list = []
for index, value in duplicates.items():
    if value is True:
        row = df.iloc[index]
        duplicate_list.append(row)
    else:
        pass


duplicated = pd.DataFrame(duplicate_list)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
duplicated.to_csv('duplicatedIds_'+dt+'.csv', index=False, quoting=csv.QUOTE_ALL)
