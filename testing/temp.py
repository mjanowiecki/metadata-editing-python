import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-id', '--identifier')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.identifier:
    identifier = args.identifier
else:
    identifier = input('Enter name of identifier columns: ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

df_1 = pd.read_csv(filename, header=0, dtype='str')

allItems = []
for count, item in df_1.iterrows():
    item = item
    bib = item['bib']
    barcode = item['barcode']
    cnumber = item['call_number']
    if bib is not None:
        list = [bib, barcode, cnumber]
        item['list'] = list
    allItems.append(item)

df = pd.DataFrame.from_records(allItems)
df.to_csv('new_'+dt+'.csv')
