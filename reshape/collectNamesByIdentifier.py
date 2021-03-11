import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')  # Original data.
parser.add_argument('-f2', '--file2')  # New name information.
parser.add_argument('-id', '--identifier')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter second filename (including \'.csv\'): ')
if args.identifier:
    identifier = args.identifier
else:
    identifier = input('Enter name of identifier columns: ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

df_1 = pd.read_csv(filename, header=0)
df_2 = pd.read_csv(filename2, header=0)
df_2 = df_2.drop(columns=['link'])

# Create old_names dataframe from original data.
old_names = df_1[[identifier, 'people', 'corporate']].copy()
# Split name strings into lists.
old_names.people = old_names.people.str.split('|')
old_names.corporate = old_names.corporate.str.split('|')

# Combine corporate names + people names by identifier.
old_names['allNames'] = ''
for index, value in old_names.people.iteritems():
    if isinstance(value, list):
        old_names.at[index, 'allNames'] = value + old_names.at[index, 'corporate']
    else:
        old_names.at[index, 'allNames'] = old_names.at[index, 'corporate']
# Drop original columns.
old_names = old_names.drop(columns=['people', 'corporate'])
# Explode/list each name by identifier.
old_names = old_names.explode('allNames')

# Merge exploded old_names with new name information.
merged = pd.merge(old_names, df_2, how='left', left_on=['allNames'],
                  right_on=['unique_names'], suffixes=('_1', '_2'))
# Drop columns.
merged = merged.drop(columns=['unique_names', 'viaf_id'])

# Pivot table, combining names associated with an identifier.
pivoted = pd.pivot_table(merged, index=[identifier], values='names_fixed',
                         aggfunc=lambda x: '|'.join(str(v) for v in x))


print(pivoted.sort_values(ascending=True, by=identifier).head())

# Create new_names from pivot table.
new_names = pd.DataFrame(pivoted)
new_names = new_names.reset_index()

# Create CSV for new_names.
print(new_names.columns)
print(new_names.head)
new_names.to_csv(path_or_buf='newNamesByIdentifier'+dt+'.csv')

# Merge new_names with original data. Create CSV.
updated_sheet = pd.merge(df_1, new_names, how='left', on=['bib'])
print(updated_sheet.columns)
print(updated_sheet.head)
updated_sheet.to_csv(path_or_buf='updated_sheet'+dt+'.csv')
