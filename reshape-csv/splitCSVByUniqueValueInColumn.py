"""Generates a new CSV for each unique value found in a column of a CSV.
The new CSVs are named based on the unique values found."""

import argparse
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
    column_name = input('Enter column to divide by value: ')

df = pd.read_csv(filename, dtype='str')
unique = df[column_name].unique()
print(unique)
for value in unique:
    new_df = df.loc[df[column_name] == value].copy()
    print(len(new_df))
    new_df.drop(columns=column_name, inplace=True)
    new_df.dropna(axis=0, how='all', inplace=True)
    new_df.dropna(axis=1, how='all', inplace=True)
    new_df.to_csv(value+'.csv', index=False, quoting=csv.QUOTE_ALL)
