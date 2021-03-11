import pandas as pd
import argparse
from datetime import datetime

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
    columnName = input('Enter column to merge on: ')

df_1 = pd.read_csv(filename, header=0)

counts = df_1[columnName].value_counts()
print(counts.head)

item_list = []
for index, row in counts.iteritems():
    if row == 1:
        item_list.append(index)
items = []
for index, row in df_1.iterrows():
    print(row)
    uri = row[columnName]
    if uri in item_list:
        items.append(row)


frame = pd.DataFrame.from_dict(items)
print(frame.columns)
print(frame.head)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
frame.to_csv('uniqueIds_'+dt+'.csv')
