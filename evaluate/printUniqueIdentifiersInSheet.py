import pandas as pd
import argparse

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
    column_name = input('Enter column to check: ')

df_1 = pd.read_csv(filename, header=0)

unique_1 = df_1[column_name].unique()
unique_1 = list(unique_1)
print(unique_1)
