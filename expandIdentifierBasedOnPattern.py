from datetime import datetime

import csv
import argparse
import re


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='collectionHandle of the collection to retreive. optional - if not provided, the script will ask for input')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

f=csv.writer(open('full_identifier.csv', 'w', encoding='utf-8'))
f.writerow(['dc.identifier']+['full.identifier'])



with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        identifier = row ['dc.identifier']
        if len(identifier) == 5:
            full_identifier = 'jhu_coll-0002_'+identifier
            f.writerow([identifier]+[full_identifier])
        elif len(identifier) == 4:
            full_identifier = 'jhu_coll-0002_0'+identifier
            f.writerow([identifier]+[full_identifier])
        elif len(identifier) == 3:
            full_identifier = 'jhu_coll-0002_00'+identifier
            f.writerow([identifier]+[full_identifier])
        else:
            print('Error '+identifier)
            f.writerow([identifier]+['ERROR'])
