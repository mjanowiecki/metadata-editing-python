"""Strips white spaces from all cells in CSV."""

import pandas as pd
import argparse
import csv
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

df = pd.read_csv(filename)
columns = df.columns.to_list()
for column in columns:
    df[column] = df[column].astype(str)
    df[column] = df[column].str.strip()

filename = filename[:-4]
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
new_filename = 'stripped'+filename+'_'+dt+'.csv'
df.to_csv(new_filename, index=False, quoting=csv.QUOTE_ALL)
