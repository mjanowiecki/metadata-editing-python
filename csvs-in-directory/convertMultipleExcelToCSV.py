"""Converts all Excel files in a directory to CSVs."""

import pandas as pd
import argparse
import os
import csv


parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory')
args = parser.parse_args()

if args.directory:
    directory = args.directory
else:
    directory = input('Enter directory: ')


for count, filename in enumerate(os.listdir(directory)):
    print(count)
    filename = directory + "/" + filename
    if filename.endswith('.xlsx'):
        df = pd.read_excel(filename, dtype=str)
        new_filename = filename.replace('.xlsx', '.csv')
        df.to_csv(new_filename, index=False, quoting=csv.QUOTE_ALL)
