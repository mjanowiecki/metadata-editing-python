"""Parses human names from column in sheet into title, first, middle, last, suffix and nickname."""

import pandas as pd
import argparse
from datetime import datetime
import csv
from nameparser import HumanName

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-c', '--column_name')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter first filename (including \'.csv\'): ')
if args.column_name:
    column_name = args.column_name
else:
    column_name = input('Enter column to check: ')


df = pd.read_csv(filename, header=0)

item_list = []
for index, row in df.iterrows():
    person_name = row.get(column_name)
    name = HumanName(person_name)
    name_dictonary = name.as_dict()
    for k, v in name_dictonary.items():
        row[k] = v
    item_list.append(row)

dt = datetime.now().strftime('%Y-%m-%d%H.%M.%S')
df_new = pd.DataFrame.from_records(item_list)
new_filename = 'parsedNames_'+filename+'_'+dt+'.csv'
df_new.to_csv(new_filename, index=False, quoting=csv.QUOTE_ALL)
