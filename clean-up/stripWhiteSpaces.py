import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

column = 'barcode'
df = pd.read_csv(filename)
df[column] = df[column].str.strip()

df.to_csv(path_or_buf='noDuplicateRows_'+filename, index=False)
