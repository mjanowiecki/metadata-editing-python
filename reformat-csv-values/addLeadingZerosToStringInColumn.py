"""Appends given number of leading zeros to string in column."""

import pandas as pd
import argparse
from datetime import datetime
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-l', '--leading_zeros')
parser.add_argument('-c', '--column_name')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.leading_zeros:
    leading_zeros = args.leading_zeros
else:
    leading_zeros = input('Enter number of zeros to add: ')
if args.column_name:
    column_name = args.column_name
else:
    column_name = input('Enter relevant column: ')

df = pd.read_csv(filename, header=0)
leading_zeros = int(leading_zeros)
df[column_name] = df[column_name].astype(str)
df[column_name] = df[column_name].str.strip()
df[column_name] = df[column_name].str.zfill(leading_zeros)

dt = datetime.now().strftime('%Y-%m-%d%H.%M.%S')
filename = filename[:-4]
new_filename = filename+'_wLeadingZeros_'+dt+'.csv'
df.to_csv(new_filename, index=False, quoting=csv.QUOTE_ALL)
