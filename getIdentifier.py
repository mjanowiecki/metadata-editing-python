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

itemList = []
with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        row = row
        fileName = row['fileName']
        ext = fileName[-3:]
        print(ext)
        if ext == 'tif':
            id = fileName[:-8]
            row['id'] = id
        elif ext == 'pdf':
            id = fileName[:-4]
            row['id'] = id
        else:
            pass
        itemList.append(row)

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
df_1 = pd.DataFrame.from_records(itemList)
filename = filename[:-4]
df_1.to_csv(filename+'_'+dt+'.csv', index=False)
