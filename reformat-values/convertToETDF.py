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
        date = row['Date Created']
        date = date.strip()
        match = re.search(r'^approximately\s\d\d\d0s$', date)
        match1 = re.search(r'^approximately\s\d\d\d\d$', date)
        match2 = re.search(r'^approximately\s\d\d\d\d-\d\d\d\d$', date)
        match3 = re.search(r'^\d\d\d\d$', date)
        match4 = re.search(r'^\d\d\d\d\-\d\d-\d\d$', date)
        match5 = re.search(r'^\d\d\d\d\-\d\d$', date)
        match6 = re.search(r'^\d\d\d\d\?$', date)
        if match:
            print(match.group())
            date = match.group()
            date = date.replace('approximately ', '')
            date = date[0:3]+'0~/'+date[0:3]+'9~'
            print(date)
            row['edtf'] = date
        elif match1:
            print(match1.group())
            date = match1.group()
            date = date.replace('approximately ', '')
            date = date[0:4]+'~'
            print(date)
            row['edtf'] = date
        elif match2:
            print(match2.group())
            date = match2.group()
            date = date.replace('approximately ', '')
            date = date.replace('-', '')
            date = date.strip()
            date = date[0:4]+'~/'+date[4:]+'~'
            print(date)
            row['edtf'] = date
        elif match3 or match4 or match5 or match6:
            print(date)
            row['edtf'] = date
        itemList.append(row)

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
df_1 = pd.DataFrame.from_records(itemList)
df_1.to_csv(filename+'_'+dt+'.csv', index=False)
