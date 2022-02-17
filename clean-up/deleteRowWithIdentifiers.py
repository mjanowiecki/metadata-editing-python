import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')  # Original data
parser.add_argument('-f2', '--file2')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter filename (including \'.csv\'): ')

df_1 = pd.read_csv(filename, header=0)
df_2 = pd.read_csv(filename2, header=0)

idsToDelete = df_2['to_delete'].tolist()

all_items = []
count = 0
for index, row in df_1.iterrows():
    unique_id = row['itemID']
    if unique_id in idsToDelete:
        count = count + 1
        print(count)
        pass
    else:
        all_items.append(row)

updated_df = pd.DataFrame.from_dict(all_items)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
updated_df.to_csv(filename+dt+'.csv', index=False)
