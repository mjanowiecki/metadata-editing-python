import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-c', '--column_name')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter first filename (including \'.csv\'): ')
if args.column_name:
    column_name = args.column_name
else:
    column_name = input('Enter column to fix: ')


df = pd.read_csv(filename, header=0)


item_list = []
for index, row in df.iterrows():
    row = row.copy()
    to_fix = row.get(column_name)
    if pd.notna(to_fix):
        to_fix = to_fix.split('|')
        row['original_total'] = len(to_fix)
        fixed = sorted(list(set(to_fix)))
        row['new_total'] = len(fixed)
        fixed = '|'.join(fixed)
        row['no_duplicates'] = fixed
    item_list.append(row)

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
df_1 = pd.DataFrame.from_records(item_list)
df_1.to_csv(filename+'_'+dt+'.csv', index=False)

