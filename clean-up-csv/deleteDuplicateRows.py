"""
Deletes any rows with the exact same information from a CSV.
"""

import pandas as pd
import argparse
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

df.to_csv(path_or_buf='noDuplicateRows_'+filename, index=False, quoting=csv.QUOTE_ALL)
