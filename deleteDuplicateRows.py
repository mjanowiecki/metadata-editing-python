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

old_file = filename.replace('.csv', '')

noDuplicateList = []

f = csv.writer(open(old_file+'NoDuplicateRows_'+dt+'.csv', 'w', encoding='utf-8'))
with open(filename) as itemMetadataFile:
    csv = csv.reader(itemMetadataFile)
    for row in csv:
        if row not in noDuplicateList:
            noDuplicateList.append(row)
        else:
            print('pass')

for item in noDuplicateList:
    f.writerow(item)
