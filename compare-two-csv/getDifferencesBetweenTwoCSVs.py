"Finds and records any differences between two similar CSVs."

import pandas as pd
import argparse
from datetime import datetime
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-f2', '--file2')
parser.add_argument('-id', '--identifier')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter first ("left") filename (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter second ("right")  filename (including \'.csv\'): ')
if args.identifier:
    identifier = args.identifier
else:
    identifier = input('Enter name of identifier columns: ')


df_left = pd.read_csv(filename, dtype=object, index_col=identifier)
df_left.sort_values(by=[identifier], inplace=True)
df_left = df_left.reindex(sorted(df_left.columns), axis=1)
columns_left = df_left.columns.tolist()
print(columns_left)


df_right = pd.read_csv(filename2, dtype=object, index_col=identifier)
df_right.sort_values(by=[identifier], inplace=True)
df_right = df_right.reindex(sorted(df_right.columns), axis=1)
columns_right = df_right.columns.tolist()
print(columns_right)

if df_left.equals(df_right):
    print('Spreadsheet {} is exactly the same as spreadsheet {}.'.format(filename, filename2))
else:
    try:
        diff = df_left.compare(df_right, keep_shape=True, result_names=("left", "right"))

        print(diff.head)
        dt = datetime.now().strftime('%Y-%m-%d')
        diff = diff.dropna(axis=0, how='all')
        diff = diff.dropna(axis=1, how='all')
        diff.to_csv('differences_'+dt+'.csv', quoting=csv.QUOTE_ALL)
    except ValueError as e:
        print(e)
        shape_left = df_left.shape
        print(shape_left)
        rows_total_left, columns_total_left = shape_left[0], shape_left[1]

        shape_right = df_right.shape
        print(shape_right)
        rows_total_right, columns_total_right = shape_right[0], shape_right[1]

        missing_from_right = list(set(columns_left) - set(columns_right))
        missing_from_left = list(set(columns_right) - set(columns_left))

        if missing_from_left:
            print('{} is missing columns {} found in {}'.format(filename, missing_from_left, filename2))
        if missing_from_right:
            print('{} is missing columns {} found in {}'.format(filename2, missing_from_right, filename))
        if rows_total_left != rows_total_right:
            if rows_total_right > rows_total_left:
                missing_row_count = rows_total_right - rows_total_left
                print('{} is missing {} rows found in {}'.format(filename, missing_row_count, filename2))
            else:
                missing_row_count = rows_total_left - rows_total_right
                print('{} is missing {} rows found in {}'.format(filename2, missing_row_count, filename))
