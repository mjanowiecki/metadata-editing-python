"""Finds all CSVs in a directory and combines them into one large CSV."""

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
    directory = input('Enter directory: ')

new_df = pd.DataFrame()
for filename in os.listdir(directory):
    filename = directory + "/" + filename
    if filename.endswith('.csv'):
        print(filename)
        df = pd.read_csv(filename, dtype='str', sep=',')
        new_df = pd.concat([new_df, df], ignore_index=True, sort=True)

new_df = new_df.drop_duplicates()
print(new_df.head)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
new_filename = 'combined_'+dt+'.csv'
new_df.to_csv(new_filename, index=False, quoting=csv.QUOTE_ALL)
