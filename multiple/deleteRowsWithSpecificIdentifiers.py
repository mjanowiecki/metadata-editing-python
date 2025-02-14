import argparse
import pandas as pd
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-f2', '--file2')
parser.add_argument('-id', '--identifier')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter file with ids to remove (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter second filename (including \'.csv\'): ')
if args.identifier:
    identifier = args.identifier
else:
    identifier = input('Enter identifier column: ')


df_1 = pd.read_csv(filename, header=0, dtype=str)
df_2 = pd.read_csv(filename2, header=0, dtype=str)

startingIDCount = df_2[identifier].unique().tolist()
startingIDCount = len(startingIDCount)
print('Total numbers of identifiers: {}.'.format(startingIDCount))

toRemove = df_1[identifier].unique().tolist()
toRemoveCount = len(toRemove)
print('{} identifiers to remove from sheet 2.'.format(toRemoveCount))

remainingIDs = startingIDCount - toRemoveCount
print("Remaining id count should be {}.".format(remainingIDs))


all_items = []
for count, row in df_2.iterrows():
    row = row
    id_value = row[identifier]
    if id_value not in toRemove:
        all_items.append(row)
    else:
        print(id_value)

updated_df = pd.DataFrame.from_records(all_items)
actualRemainingIDs = updated_df[identifier].unique().tolist()
actualRemainingIDs = len(actualRemainingIDs)
print('Remaining identifiers: {}.'.format(actualRemainingIDs))
filename2 = filename2[:-4]
updated_df.to_csv(filename2+'_updated.csv', index=False, quoting=csv.QUOTE_ALL)
