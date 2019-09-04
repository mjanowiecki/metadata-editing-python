import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='collectionHandle of the collection to retreive. optional - if not provided, the script will ask for input')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
f = csv.writer(open('noDuplicateRows.csv', 'w', encoding='utf-8'))

noDuplicateList = []
with open(filename) as itemMetadataFile:
    csv = csv.reader(itemMetadataFile)
    for row in csv:
        if row not in noDuplicateList:
            noDuplicateList.append(row)

for item in noDuplicateList:
    f.writerow(item)
