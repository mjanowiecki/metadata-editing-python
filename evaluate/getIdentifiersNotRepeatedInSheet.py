import pandas as pd
import argparse
from datetime import datetime

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
    column_name = input('Enter column with identifier: ')

df_1 = pd.read_csv(filename, header=0)

counts = df_1[column_name].value_counts()
print(counts.head)

item_list = []
for index, row in counts.items():
    if row == 1:
        item_list.append(index)
items = []
for index, row in df_1.iterrows():
    print(row)
    uri = row[column_name]
    if uri in item_list:
        items.append(row)


frame = pd.DataFrame.from_dict(items)
print(frame.columns)
print(frame.head)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
frame.to_csv('uniqueIds_'+dt+'.csv')
