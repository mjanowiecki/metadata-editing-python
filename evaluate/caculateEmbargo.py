from datetime import datetime
from dateutil.relativedelta import relativedelta
import csv
import argparse

# Converts dates from getArchivalObjectRefIdsForResource.py to ISO dates.

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

f = csv.writer(open('metadataWithDates.csv', 'w'))
f.writerow(['date']+['title']+['notes'])

with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        date = row['dc.date.issued'].strip()
        title = row['dc.title']
        notes = row['Notes'].strip()
        if notes == 'Restrict until 25 years from creation date':
            try:
                date = datetime.strptime(date, "%Y-%m-%d")
                print(date)
                embargo_date = date+relativedelta(years=+25)
                print(embargo_date)
                embargo_date = str(embargo_date)
                embargo_date = embargo_date[0:10]
                f.writerow([embargo_date]+[title]+[notes])
            except:
                continue
