import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-f2', '--file2')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter second filename (including \'.csv\'): ')
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

df_1 = pd.read_csv(filename, header=0)
df_2 = pd.read_csv(filename2, header=0)

df_2.auth_name = df_2.auth_name.str.strip()

pivoted = pd.pivot_table(df_2, index=['bib'], values='auth_name', aggfunc=lambda x: '|'.join(str(v) for v in x))
print(pivoted.sort_values(ascending=True, by='bib').head())

new_subjects = pd.DataFrame(pivoted)
new_subjects = new_subjects.reset_index()

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

new_subjects['noDuplicates'] = littleList
print(new_subjects.columns)
print(new_subjects.head)
new_subjects.to_csv(path_or_buf='newSubjectsByBibNumber'+dt+'.csv')


updated_marc = pd.merge(df_1, new_subjects, how='left', on=['bib'])
print(updated_marc.columns)
print(updated_marc.head)
updated_marc.to_csv(path_or_buf='updated_marc'+dt+'.csv')
