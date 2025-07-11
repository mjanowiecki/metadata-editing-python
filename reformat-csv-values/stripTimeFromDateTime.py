"""Strips the time from a standard DateTime stamp."""

import argparse
import pandas as pd
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

item_list = []
with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        row = row
        date1 = row[column_name]
        date1 = date1[:10]
        row[column_name] = date1
        item_list.append(row)


dt = datetime.now().strftime('%Y-%m-%d%H.%M.%S')
df = pd.DataFrame.from_records(item_list)
filename = filename[:-4]
df.to_csv(filename+'TimeStripped'+'_'+dt+'.csv', index=False, quoting=csv.QUOTE_ALL)
