"""Combines all CSVs in a directory into a dataframe, and makes a new CSV for each column found in the combined dataframe."""

import pandas as pd
import argparse
import os
from datetime import datetime
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory')
args = parser.parse_args()

if args.directory:
    directory = args.directory
else:
    directory = input('Enter directory (including \'.csv\'): ')

new_df = pd.DataFrame()
for filename in os.listdir(directory):
    filename = directory + "/" + filename
    df = pd.read_csv(filename)
    handle = filename.replace(directory+'/', '').replace('Metadata.csv', '')
    print(handle)
    df['handle'] = handle
    new_df = new_df.append(df, ignore_index=True, sort=True)


column_names = list(new_df.columns.values)
for column in column_names:
    print(column)
    new_df = new_df[[column, 'itemID', 'handle']].copy()
    new_df = new_df.dropna(subset=[column])
    print(new_df.head)
    column_name = column.replace('.', '_')
    dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
    new_df.to_csv(column_name+'_'+dt+'.csv', index=False, quoting=csv.QUOTE_ALL)
