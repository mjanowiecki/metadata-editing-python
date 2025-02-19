"""Counts how many values are found in each column of spreadsheets in a directory. This count information is then added by handle (or filename) to a new CSV."""

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
    counts = df.count()
    handle = filename.replace(directory+'/', '').replace('Metadata.csv', '')
    print(handle)
    df_count = counts.to_frame()
    df_count = df_count.reset_index()
    df_count['handle'] = handle
    print(df_count.head)
    new_df = new_df.append(df_count, sort=True)

print(new_df.head)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
new_df.to_csv(path_or_buf='countedValues_'+dt+'.csv', index=False, quoting=csv.QUOTE_ALL)
