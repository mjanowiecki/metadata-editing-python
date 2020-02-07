import csv
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

f = csv.writer(open('oneColumn_'+dt+'.csv', 'w'))

all_columns_list = []
with open(filename) as multipleColumnsFile:
    multipleColumns = csv.reader(multipleColumnsFile)
    for row in multipleColumns:
        for item in row:
            if item:
                # if item not in all_columns_list:
                all_columns_list.append(item)
for item in all_columns_list:
    f.writerow([item])
