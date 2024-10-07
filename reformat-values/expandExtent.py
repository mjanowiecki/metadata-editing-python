import csv
import argparse
import pandas as pd
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

item_list = []
with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for count, row in enumerate(itemMetadata):
        row = row
        extent = row['Extent']
        if len(extent) == 7:
            extent = '0'+extent+'hh:mm:ss'
            print(extent)
            row['Extent'] = extent
        elif len(extent) == 8:
            extent = '0'+extent+'hh:mm:ss'
            row['Extent'] = extent
            print(extent)
        else:
            print(count)
        item_list.append(row)

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
df_1 = pd.DataFrame.from_records(item_list)
filename = filename[:-4]
df_1.to_csv(filename+'_1.csv', index=False)
