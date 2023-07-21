import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-f2', '--file2')
parser.add_argument('-id', '--identifier')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter file with list of ids to keep in sheet 2: ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter file of metadata (including \'.csv\'): ')
if args.identifier:
    identifier = args.identifier
else:
    identifier = input('Enter identifier column: ')


df_1 = pd.read_csv(filename, header=0)
df_2 = pd.read_csv(filename2, header=0)

startingIDCount = df_2[identifier].unique().tolist()
startingIDCount = len(startingIDCount)
print('Total numbers of identifiers: {}.'.format(startingIDCount))

toKeep = df_1[identifier].unique().tolist()

toKeepCount = len(toKeep)
print('{} identifiers to keep from sheet 2.'.format(toKeepCount))

remainingIDs = toKeepCount
print("Remaining id count should be {}.".format(remainingIDs))


allItems = []
missing = []
for count, row in df_2.iterrows():
    row = row
    id_value = row[identifier]
    if id_value in toKeep:
        allItems.append(row)
    else:
        missing.append(id_value)

updated_df = pd.DataFrame.from_dict(allItems)
missing = list(set(missing))
missing_ids = pd.Series(missing)
actualRemainingIDs = updated_df[identifier].unique().tolist()
toKeep = set(toKeep)
actualRemainingIDs = set(actualRemainingIDs)
not_found = toKeep.difference(actualRemainingIDs)
print(not_found)
actualRemainingIDs = len(actualRemainingIDs)
print('Remaining identifiers: {}.'.format(actualRemainingIDs))
filename2 = filename2[:-4]
updated_df.to_csv(filename2+'_updated.csv', index=False)
missing_ids.to_csv('missing_ids.csv')