"""Print list of unique identifiers in CSV to terminal."""

import pandas as pd
import argparse

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
    identifier = input('Enter name of identifier columns: ')

df = pd.read_csv(filename, header=0)

unique_1 = df[identifier].unique()
unique_1 = list(unique_1)
print(unique_1)
