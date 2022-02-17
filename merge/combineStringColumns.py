import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')


df_1 = pd.read_csv(filename, header=0)
print(df_1.columns)

columnsToCombine = ['subject', 'person', 'geo_location', 'corporate_body']


def combineByRow(row):
    all_items = []
    for column in columnsToCombine:
        if pd.notnull(row[column]):
            for value in str(row[column]).split('|'):
                all_items.append(value)
    all_items = list(set(all_items))
    all_items = '|'.join(all_items)
    return all_items


df_1['title.alternative'] = df_1.apply(lambda row: combineByRow(row), axis=1)


dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
filename = filename[:-4]
df_1.to_csv(filename+'_mergedColumn'+dt+'.csv', index=False)
