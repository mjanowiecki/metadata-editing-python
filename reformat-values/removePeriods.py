import csv
import argparse
import re
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
        altTitle = row['Alternative Title']
        title = row['Title']
        altTitle = altTitle.strip()
        title = title.strip()
        match = re.search(r'\.$', altTitle)
        match2 = re.search(r'\.$', title)
        if match:
            print(match.group())
            altTitle = altTitle[:-1]
            row['Alternative Title'] = altTitle
        else:
            pass
        if match2:
            print(match2.group())
            title = title[:-1]
            row['Title'] = title

        itemList.append(row)

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
df_1 = pd.DataFrame.from_records(itemList)
filename = filename[:-4]
df_1.to_csv(filename+'_noPeriods.csv', index=False)
