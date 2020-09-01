
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
df = df.dropna(axis=0, how='all')
df = df.dropna(axis=1, how='all')

df.to_csv(path_or_buf='noBlankRowsOrColumns_'+filename, index=False)
