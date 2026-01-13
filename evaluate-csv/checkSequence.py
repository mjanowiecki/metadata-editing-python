"""Adds new column with complete identifier sequence to sheet, allowing you to easily see what identifiers in the sequence are missing. """

# original
# column_name
# 82
# 83
# 85

# new
# column_name  sequence
# 82            82
# 83            83
#               84
# 85            85



import argparse
import pandas as pd
from datetime import datetime
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-c', '--column_name')
parser.add_argument('-m', '--min_seq')
parser.add_argument('-x', '--max_seq')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.column_name:
    column_name = args.column
else:
    column_name = input('Enter name of identifier columns: ')
if args.min_seq:
    min_seq = args.min_seq
else:
    min_seq = input('Enter lowest number of the sequence: ')
if args.max_seq:
    max_seq= args.max_seq
else:
    max_seq = input('Enter highest number of the sequence: ')


df_1 = pd.read_csv(filename, header=0, dtype='string')
df_1[column_name] = df_1[column_name].str.zfill(4)
min_seq = int(min_seq)
max_seq = int(max_seq)

my_list = []
for i in range(0, 1000):
    i = str(i).zfill(4)
    my_list.append(i)
df_2 = pd.DataFrame({column_name: my_list,
                     'sequence': my_list}, dtype='string')

frame = pd.merge(df_1, df_2, how='outer', on=column_name, suffixes=('_1', '_2'), indicator=True)


print(frame.columns)
print(frame.head)
dt = datetime.now().strftime('%Y-%m-%d')
frame.to_csv(filename[:-4]+'_'+dt+'.csv', index=False, quoting=csv.QUOTE_ALL)
