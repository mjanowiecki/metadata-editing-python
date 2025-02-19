"""Strips the time from a standard DateTime stamp."""

import csv
import argparse
import pandas as pd
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

item_list = []
with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        row = row
        date1 = row['Date Available']
        date1 = date1[:10]
        row['Date Available'] = date1
        item_list.append(row)


dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
df_1 = pd.DataFrame.from_records(item_list)
filename = filename[:-4]
df_1.to_csv(filename+'_dates.csv', index=False)
