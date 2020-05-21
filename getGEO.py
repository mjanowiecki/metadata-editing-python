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
f = csv.writer(open('geoHandles_'+dt+'.csv', 'w', encoding='utf-8'))


handles = []
with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        bitstream = row['bitstream']
        handle = row['handle']
        if 'GEO.tfw' in bitstream:
            if handle not in handles:
                handles.append(handle)
            else:
                pass
for item in handles:
    f.writerow([item])
