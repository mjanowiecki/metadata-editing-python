"""Deletes any rows and columns that are completely blank from a CSV."""

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

df = pd.read_csv(filename, header=0, dtype="string")
df = df.dropna(axis=0, how='all')
df = df.dropna(axis=1, how='all')

filename = filename[:-4]
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
new_filename = 'noBlankRowsOrColumns'+filename+'_'+dt+'.csv'
df.to_csv(new_filename, index=False, quoting=csv.QUOTE_ALL)
