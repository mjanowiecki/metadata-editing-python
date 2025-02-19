"""Loops through a spreadsheet of filenames and adds column containing file extensions to original CSV."""

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
    filename = input('Enter first filename (including \'.csv\'): ')


df = pd.read_csv(filename)

all_items = []
for index, row in df.iterrows():
    row = row
    filename = row['filename']
    if pd.notna(filename):
        fileList = filename.rsplit('.', 1)
        name = fileList[0]
        ext = fileList[1]
        row['ext'] = ext
        all_items.append(row)


updated_df = pd.DataFrame.from_records(all_items)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
updated_df.to_csv('matchedPairs_'+dt+'.csv', index=False, quoting=csv.QUOTE_ALL)
