from datetime import datetime

import csv
import argparse
import re


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='collectionHandle of the collection to retreive. optional - if not provided, the script will ask for input')
parser.add_argument('-t', '--file2', help='collectionHandle of the collection to retreive. optional - if not provided, the script will ask for input')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter filename (including \'.csv\'): ')

f=csv.writer(open('uris.csv', 'w', encoding='utf-8'))
f.writerow(['dc.identifier']+['full.identifier']+['uri']+['link'])


with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    # list = list(itemMetadata)
    # total = len(list)
    # print(total)
    for row in itemMetadata:
        identifier = row['full.identifier']
        print(identifier)
        with open(filename2) as otherMetadata:
            otherMetadata = csv.DictReader(otherMetadata)
            for row in otherMetadata:
                other_identifier = row['dc.identifier.other']
                uri = row['uri']
                itemID = row['itemID']
                if identifier == other_identifier:
                    f.writerow([identifier]+[uri]+[itemID])
                    print("found: "+identifier)
                    # total = total - 1
                    # print(total)
                    break
            else:
                f.writerow([identifier]+['no uri found']+['no id found'])
