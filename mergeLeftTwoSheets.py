import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-f2', '--file2')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter first filename (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter second filename (including \'.csv\'): ')

df_1 = pd.read_csv(filename, header=0)
print(df_1.columns)
df_2 = pd.read_csv(filename2, header=0)
print(df_2.columns)

frame = pd.merge(df_1, df_2, how='left', on=['fast_id'], suffixes=('_1', '_2'))


frame = frame.reindex(sorted(frame.columns), axis=1)
print(frame.columns)
print(frame.head)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
frame.to_csv(path_or_buf='mergedCSV_'+dt+'.csv')
