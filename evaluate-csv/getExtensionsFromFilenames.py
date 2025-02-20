"""Loops through a spreadsheet of filenames and adds column containing file extensions to original CSV."""

import argparse
from datetime import datetime
import pandas as pd
import csv

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
    column_name = input('Enter name of column containing filenames: ')


df = pd.read_csv(filename)

all_items = []
for index, row in df.iterrows():
    row = row
    filename = row[column_name]
    if pd.notna(filename):
        fileList = filename.rsplit('.', 1)
        name = fileList[0]
        ext = fileList[1]
        row['file_ext'] = ext
        all_items.append(row)


updated_df = pd.DataFrame.from_records(all_items)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
filename = filename[:-4]
new_filename = 'extensionsAddedTp'+filename+'_'+dt+'.csv'
updated_df.to_csv(new_filename, index=False, quoting=csv.QUOTE_ALL)
