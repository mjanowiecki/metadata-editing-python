import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')  # Original data.
parser.add_argument('-f2', '--file2')  # New subject information.
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
if args.id:
    identifier = args.id
else:
    identifier = input('Enter name of identifier columns: ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

df_1 = pd.read_csv(filename, header=0)
df_2 = pd.read_csv(filename2, header=0)

df_2.auth_name = df_2.auth_name.str.strip()

# Organize + sort new subjects by identifier.
pivoted = pd.pivot_table(df_2, index=[identifier], values='auth_name',
                         aggfunc=lambda x: '|'.join(str(v) for v in x))
print(pivoted.sort_values(ascending=True, by=identifier).head())

# Turn pivot table into dataframe.
new_subjects = pd.DataFrame(pivoted)
new_subjects = new_subjects.reset_index()

# Remove any duplicated subjects.
littleList = []
for index, value in new_subjects.auth_name.items():
    newValues = []
    valueList = value.split('|')
    for v in valueList:
        if v not in newValues:
            newValues.append(v)
        else:
            pass
    newValues = '|'.join(newValues)
    littleList.append(newValues)

# Create spreadsheet of new subjects organized by identifier.
new_subjects['noDuplicates'] = littleList
print(new_subjects.columns)
print(new_subjects.head)
new_subjects.to_csv(path_or_buf='newSubjectsByBibNumber'+dt+'.csv')

# Merge new subjects to original data using identifier.
updated_marc = pd.merge(df_1, new_subjects, how='left', on=[identifier])
print(updated_marc.columns)
print(updated_marc.head)
updated_marc.to_csv(path_or_buf='updated_'+filename)