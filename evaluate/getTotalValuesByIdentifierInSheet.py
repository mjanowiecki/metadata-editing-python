import pandas as pd
import argparse
from datetime import datetime

# For spreadsheet where some identifiers are repeated in multiple rows, and
# each row has a number value , add up number values for each identifier.
# Here, we are finding total number of maps by identifier.

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
    identifier = input('Enter name of identifier column: ')

df = pd.read_csv(filename, header=0)

# Count how many times the identifier appears in the df.
# Returns dataframe "counts" with id and value_counts.
counts = df[identifier].value_counts()
print(counts.head)


duplicate_list = []
for identifier, count in counts.items():
    print(identifier, count)
    if count > 1:
        # If id appears more than once, create temporary dataframe.
        # Count how many times that id had column where type == "map".
        df_temp = df.loc[df[identifier] == identifier]
        maps = len(df_temp[df_temp.type == 'map'])
        # If type == map more than 1 time, create dictionary and add to list.
        if maps > 1:
            identifier = identifier.replace('https://jscholarship.library.jhu.edu/handle/', '')
            duplicate_list.append({identifier: id, 'type': 'multiple',
                                  'numberOfMaps': maps})

# Turn duplicate list into new dataframe.
duplicates = pd.DataFrame.from_records(duplicate_list)

print(duplicates.columns)
print(duplicates.head)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
duplicates.to_csv(path_or_buf='totalValuesBy'+identifier+'_'+dt+'.csv')
