"""
Print any duplicated identifier pairs to terminal.
"""

import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')


df = pd.read_csv(filename)

duplicates = df.duplicated(subset=['handle', 'bitstreams'], keep=False)

duplicate_list = []
for index, value in duplicates.items():
    if value is True:
        duplicate_list.append(index)

for duplicate in duplicate_list:
    print(df.iloc[duplicate])


