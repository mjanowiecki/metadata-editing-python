from datetime import datetime

import csv
import argparse
import re

# Converts CSV made from getArchivalObjectRefIdsForResource.py to ISO dates.

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

f = csv.writer(open('metadataWithDates.csv', 'w'))
f.writerow(['title']+['uri']+['ref_id']+['date']+['dataBegin']+['level'])

with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        title = row['title']
        uri = row['uri']
        ref_id = row['ref_id']
        dataBegin = row['dataBegin']
        level = row['level']
        date = row['dateExpression'].strip()
        match = re.search(r'\-', date)
        if match:
            pass
        else:
            try:
                date = datetime.strptime(date, '%Y')
                date.isoformat()
                date = str(date)
                date = date[0:4]
                print(date)
            except:
                try:
                    date = datetime.strptime(date, '%Y %B')
                    date.isoformat()
                    date = str(date)
                    date = date[0:7]
                    print(date)
                except:
                    try:
                        date = datetime.strptime(date, '%Y %B %d')
                        date.isoformat()
                        date = str(date)
                        date = date[0:10]
                        print(date)
                    except:
                        pass
        date = str(date)
        f.writerow([title]+[uri]+[ref_id]+[date]+[dataBegin]+[level])
