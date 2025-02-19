"""Collects every Nth row from a CSV to create a sample of data."""

import csv
import argparse
import itertools
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='enter filename to retrieve')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

old_file = filename.replace('.csv', '')

f = csv.writer(open('sampledRowsFrom'+old_file+'_'+dt+'.csv', 'w'))
f.writerow(['samples'])

with open(filename) as csvfile:
    sampled_rows = itertools.islice(csvfile, 1, None, 40)
    for sample in sampled_rows:
        f.writerow([sample])
