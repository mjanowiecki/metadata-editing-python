import argparse
import pandas as pd
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

df = pd.read_csv(filename)

duplicates = df.duplicated(subset=[identifier], keep=False)

duplicate_list = []
for index, value in duplicates.iteritems():
    if value is True:
        row = df.iloc[index]
        duplicate_list.append(row)
    else:
        pass


duplicated = pd.DataFrame(duplicate_list)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
duplicated.to_csv('duplicatedIds_'+dt+'.csv', index=False)
