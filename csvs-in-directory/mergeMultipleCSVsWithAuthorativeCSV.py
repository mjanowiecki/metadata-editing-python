"""Merges each CSV in a directory against one authoritative CSV. Uses an alternative identifier in all CSVs to count when there is more than one match found."""

import pandas as pd
import argparse
import os
import csv
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory')
parser.add_argument('-f', '--file')
parser.add_argument('-c', '--column_name')
parser.add_argument('-m', '--method')
parser.add_argument('-a', '--alt_id')
args = parser.parse_args()

if args.directory:
    directory = args.directory
else:
    directory = input('Enter directory: ')
if args.file:
    filename = args.file
else:
    filename = input('Enter authoritative filename (including \'.csv\'): ')
if args.column_name:
    column_name = args.column_name
else:
    column_name = input('Enter column to merge on: ')
if args.method:
    method = args.method
else:
    method = input('Enter type of merge (left, right, inner, outer, cross): ')
if args.alt_id:
    alt_id = args.alt_id
else:
    alt_id = input('Enter column to merge on: ')


authority = pd.read_csv(filename, header=0, dtype=object)

for count, csv_name in enumerate(os.listdir(directory)):
    csv_name = directory + "/" + csv_name
    if csv_name.endswith('.csv'):
        print('')
        print(csv_name)
        df = pd.read_csv(csv_name, header=0, dtype=object)
        alt_id_counts = df[alt_id].value_counts()
        df['alt_id_counts'] = df[alt_id].map(alt_id_counts)
        original_row_count = len(df)
        print('Total rows: {}'.format(str(original_row_count)))
        frame = pd.merge(df, authority, how=method, on=column_name, suffixes=('_1', '_2'), indicator=True)
        new_row_count = len(frame)
        print("Added rows: {}.".format(str(new_row_count-original_row_count)))
        alt_with_suffix = alt_id+'_1'
        new_alt_id_counts = frame[alt_with_suffix].value_counts()
        matched_rows = frame[frame._merge == 'both'].shape[0]
        print('Matched rows: {}'.format(matched_rows))
        frame['new_alt_id_counts'] = frame[alt_with_suffix].map(new_alt_id_counts)
        frame['only_one_match'] = frame['new_alt_id_counts'].eq(frame.alt_id_counts)
        dt = datetime.now().strftime('%Y-%m-%d')
        frame.to_csv(csv_name[:-4] + '_' + dt + '.csv', index=False, quoting=csv.QUOTE_ALL)


