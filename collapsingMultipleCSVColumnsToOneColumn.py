import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='collectionHandle of the collection to retreive. optional - if not provided, the script will ask for input')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

f=csv.writer(open('oneColumn.csv', 'w'))

all_columns_list = []
with open(filename) as multipleColumnsFile:
    multipleColumns = csv.reader(multipleColumnsFile)
    for row in multipleColumns:
        for item in row:
            #if item not in all_columns_list:
            all_columns_list.append(item)
for item in all_columns_list:
    f.writerow([item])
