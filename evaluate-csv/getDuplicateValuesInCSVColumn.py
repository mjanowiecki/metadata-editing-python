"""Find any duplicated values within a column of a CSV,
and then creates a new CSV containing all the duplicated rows."""

import argparse
import chardet
import pandas as pd
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-c', '--column_name')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.column_name:
    column_name = args.column_name
else:
    column_name = input('Enter column to check for duplicates: ')


def find_encoding(name_file):
    r_file = open(name_file, 'rb').read()
    result = chardet.detect(r_file)
    character_encoding = result['encoding']
    return character_encoding


my_encoding = find_encoding(filename)
print(my_encoding)

df = pd.read_csv(filename, encoding=my_encoding)

dupRows = df[df.duplicated([column_name], keep=False)]

print(dupRows)
if dupRows.empty is False:
    dupRows.to_csv(path_or_buf='duplicatedValues_'+filename, index=False, quoting=csv.QUOTE_ALL)
    
