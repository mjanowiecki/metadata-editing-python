import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

noDuplicateList = []

f = csv.writer(open('noDuplicateRows.csv', 'w', encoding='utf-8'))
with open(filename) as itemMetadataFile:
    csv = csv.reader(itemMetadataFile)
    for row in csv:
        if row not in noDuplicateList:
            noDuplicateList.append(row)
        else:
            print('pass')

for item in noDuplicateList:
    f.writerow(item)
