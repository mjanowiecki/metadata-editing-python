import pandas as pd
import argparse
from datetime import datetime
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-c', '--column1')
parser.add_argument('-c2', '--column2')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.column1:
    column1 = args.column1
else:
    column1 = input('Enter identifier column: ')
if args.column2:
    column2 = args.column2
else:
    column2 = input('Enter column to count values: ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

df = pd.read_csv(filename, header=0)

all_items = []
for count, row in df.iterrows():
    row = row
    identifier = row[column1]
    values = row[column2]
    values = str(values).split('||')
    total_values = len(set(values))
    row['total_values'] = total_values
    all_items.append(row)

updated_df = pd.DataFrame.from_records(all_items)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
new_filename = 'totalValuesOf'+column2+'_'+dt+'.csv'
updated_df.to_csv(new_filename, index=False, quoting=csv.QUOTE_ALL)
