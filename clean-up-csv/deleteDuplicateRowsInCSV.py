"""Deletes any rows with the exact same information from a CSV."""

import pandas as pd
import argparse
from datetime import datetime
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

df = pd.read_csv(filename)
df = df.drop_duplicates()

filename = filename[:-4]
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
new_filename = 'noDuplicateRows'+filename+'_'+dt+'.csv'
df.to_csv(new_filename, index=False, quoting=csv.QUOTE_ALL)
