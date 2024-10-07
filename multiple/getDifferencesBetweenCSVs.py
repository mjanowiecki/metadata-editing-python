import pandas as pd
import argparse
from datetime import datetime
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-f2', '--file2')
parser.add_argument('-c', '--column_name')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter first ("left") filename (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter second ("right")  filename (including \'.csv\'): ')

df_left = pd.read_csv(filename, dtype=object)
columns_left = df_left.columns.values.tolist()

df_right = pd.read_csv(filename2, dtype=object)
columns_right = df_right.columns.values.tolist()

if df_left.equals(df_right):
    print('Spreadsheet {} is exactly the same as spreadsheet {}.'.format(filename, filename2))
else:
    try:
        diff = df_left.compare(df_right, keep_shape=True, result_names=("left", "right"))
        print(diff.head)
        dt = datetime.now().strftime('%Y-%m-%d')
        diff.to_csv('differences_' + dt + '.csv', quoting=csv.QUOTE_ALL)
    except ValueError:
        shape_left = df_left.shape
        row_total_left, columns_total_left = shape_left[0], shape_left[1]

        shape_right = df_right.shape
        row_total_right, columns_total_right = shape_right[0], shape_right[1]

        if row_total_left != row_total_right:
            if row_total_right > row_total_left:
                missing_row_count = row_total_right - row_total_left
                print('{} is missing {} rows found in {}'.format(filename, missing_row_count, filename2))
            else:
                missing_row_count = row_total_left - row_total_right
                print('{} is missing {} rows found in {}'.format(filename2, missing_row_count, filename))

        if columns_total_right != columns_total_left:
            missing_from_right = list(set(columns_left) - set(columns_right))
            missing_from_left = list(set(columns_right) - set(columns_left))
            if missing_from_left:
                print('{} is missing columns {} found in {}'.format(filename, missing_from_left, filename2))
            if missing_from_right:
                print('{} is missing columns {} found in {}'.format(filename2, missing_from_right, filename))
