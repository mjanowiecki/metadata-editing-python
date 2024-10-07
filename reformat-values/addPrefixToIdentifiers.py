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

f = csv.writer(open('expandedIdentifiers' + filename, 'w'))
f.writerow(['identifier'] + ['dc.identifier.other'])

with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        identifier = row['identifier']
        zfill_identifier = str(identifier).zfill(5)
        prefix = 'jhu_coll-0002_'
        expanded_id = prefix + zfill_identifier
        f.writerow([identifier] + [expanded_id])
