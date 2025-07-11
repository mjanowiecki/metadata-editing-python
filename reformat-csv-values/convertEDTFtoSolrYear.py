""""""

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

item_list = []
with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        row = row
        date = row['edtf']
        date = date.strip()
        match1 = re.search(r'^\d\d\d\d$', date)
        match2 = re.search(r'^\d\d\d\d-\d\d-\d\d$', date)
        match3 = re.search(r'^\d\d\d\d-\d\d$', date)
        match4 = re.search(r'^\d\d\d\d[\?%~]$', date)
        match5 = re.search(r'^\d\d\d\d-\d\d[\?%~]$', date)
        match6 = re.search(r'^\d\d\d\d-\d\d-\d\d[\?%~]$', date)
        if match1:
            row['solr'] = date
        elif match2 or match3 or match4 or match5 or match6:
            date = date[0:4]
            row['solr'] = date
        elif "/" in date and ("X" not in date) and (".." not in date):
            print(date)
            start = re.search(r'^\d\d\d\d', date)
            end = re.search(r'/\d\d\d\d', date)
            start = start.group()
            end = end.group()
            end = int(end.strip("/"))+1
            solr_list = list(range(int(start), end))
            print(solr_list)
            row['solr'] = solr_list
        else:
            pass
        item_list.append(row)

dt = datetime.now().strftime('%Y-%m-%d%H.%M.%S')
df_1 = pd.DataFrame.from_records(item_list)
filename = filename[:-4]
df_1.to_csv(filename+'_'+dt+'.csv', index=False)
