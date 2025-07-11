"""For CSV where some identifiers are repeated in multiple rows, and each row has a number value,
add up number values for each identifier."""

import pandas as pd
import argparse
from datetime import datetime
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-id', '--identifier')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.identifier:
    identifier = args.identifier
else:
    identifier = input('Enter name of identifier column: ')

df = pd.read_csv(filename, header=0, dtype=object)

# Count how many times the identifier appears in the df.
# Returns dataframe "counts" with id and value_counts.
counts = df[identifier].value_counts()
updated_df = pd.merge(df, counts, how='left', on=[identifier], suffixes=('_1', '_2'))

print(counts)

dt = datetime.now().strftime('%Y-%m-%d%H.%M.%S')
new_filename = 'totalValuesBy'+identifier+'_'+dt+'.csv'
updated_df.to_csv(new_filename, index=False, quoting=csv.QUOTE_ALL)
