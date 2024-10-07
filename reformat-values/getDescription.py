import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter first filename (including \'.csv\'): ')


df = pd.read_csv(filename, header=0)

item_list = []
for index, row in df.iterrows():
    row = row
    descriptions = row['dc.description']
    if pd.notna(descriptions):
        for description in descriptions.split('|'):
            if "Johns Hopkins University, Levy Sheet Music Collection" in description:
                if '073a' in description:
                    row['box_item_info'] = description
                    item_list.append(row)
        else:
            pass

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
df_1 = pd.DataFrame.from_records(item_list)
df_1.to_csv(filename+'_'+dt+'.csv', index=False)
