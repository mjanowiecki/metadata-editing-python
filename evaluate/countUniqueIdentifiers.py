import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-c', '--columnName')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.columnName:
    columnName = args.columnName
else:
    columnName = input('Enter column to check: ')

df_1 = pd.read_csv(filename, header=0)

unique_1 = df_1[columnName].unique()
unique_1 = list(unique_1)
print(len(unique_1))
