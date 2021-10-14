import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

df = pd.read_csv(filename)
columns = list(df.columns.values)
for column in columns:
    df[column] = df[column].str.strip()

df.to_csv('stripped_'+filename, index=False)
