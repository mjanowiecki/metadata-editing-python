import csv
import argparse
from datetime import datetime
from fuzzywuzzy import fuzz
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')


def addToList(key):
    value = row[key]
    value = value.split('|')
    for v in value:
        newNames.append(v)


all_rows = []
with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        allNames = row['names_fixed']
        bib = row['bib']
        allNames = allNames.split('|')
        newNames = []
        addToList('director')
        addToList('distributor')
        addToList('producer_1')
        addToList('producer_2')
        addToList('publisher')
        addToList('announcer')
        addToList('performer')
        addToList('presenter')
        addToList('writer')
        addToList('editor')
        addToList('speaker')
        addToList('undetermined')
        addToList('narrator')
        little_dict = {}
        newNames = set(newNames)
        allNames = set(allNames)
        noCleanedName = newNames - allNames
        noCleanedName = sorted(list(noCleanedName))
        noRelator = allNames - newNames
        noRelator = sorted(list(noRelator))
        little_dict['noCleanedName'] = noCleanedName
        little_dict['noRelator'] = noRelator
        little_dict['bib'] = bib
        all_rows.append(little_dict)



df = pd.DataFrame.from_dict(all_rows)
print(df.head(15))
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
df.to_csv(path_or_buf='confirmChanges_'+dt+'.csv', header='column_names', encoding='utf-8', sep=',', index=False)
