import argparse
from datetime import datetime
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-f2', '--file2')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter first filename (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter second filename (including \'.csv\'): ')


df_1 = pd.read_csv(filename, header=0)
df_2 = pd.read_csv(filename2, header=0)

deletedList = df_1['deleted'].unique().tolist()
print(len(deletedList))

allItems = []
for count, row in df_2.iterrows():
    row = row
    jhir = row['uri']
    print(jhir)
    if jhir in deletedList:
        print(jhir)
    else:
        allItems.append(row)

updated_df = pd.DataFrame.from_dict(allItems)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
updated_df.to_csv('isleMaps_'+dt+'.csv', index=False)
