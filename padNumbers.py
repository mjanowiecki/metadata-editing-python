import csv
import argparse
import pandas as pd
from datetime import datetime
import re

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
    for count, row in enumerate(itemMetadata):
        row = row
        title = row['Title']
        print(title)
        title = re.sub(r'(\b[0-9]\b)', r'0\1', title)
        print(title)
        row['Title'] = title
        itemList.append(row)

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
df_1 = pd.DataFrame.from_records(itemList)
filename = filename[:-4]
df_1.to_csv(filename+'_1.csv', index=False)
