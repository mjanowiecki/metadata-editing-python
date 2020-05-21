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
df_2 = df_2.drop(columns=['link'])
df_names = df_1[['bib', 'people', 'corporate']].copy()
df_names.people = df_names.people.str.split('|')
df_names.corporate = df_names.corporate.str.split('|')
df_names['allNames'] = ''
for index, value in df_names.people.iteritems():
    if isinstance(value, list):
        df_names.at[index, 'allNames'] = value + df_names.at[index, 'corporate']
    else:
        df_names.at[index, 'allNames'] = df_names.at[index, 'corporate']

df_names = df_names.drop(columns=['people', 'corporate'])
df_names = df_names.explode('allNames')

frame = pd.merge(df_names, df_2, how='left', left_on=['allNames'], right_on=['unique_names'], suffixes=('_1', '_2'))
frame = frame.drop(columns=['unique_names', 'viaf_id'])

pivoted = pd.pivot_table(frame, index=['bib'], values='names_fixed', aggfunc=lambda x: '|'.join(str(v) for v in x))
print(pivoted.sort_values(ascending=True, by='bib').head())

new_names = pd.DataFrame(pivoted)
new_names = new_names.reset_index()

print(new_names.columns)
print(new_names.head)
new_names.to_csv(path_or_buf='newNamesByBibNumber'+dt+'.csv')


updated_marc = pd.merge(df_1, new_names, how='left', on=['bib'])
print(updated_marc.columns)
print(updated_marc.head)
updated_marc.to_csv(path_or_buf='updated_marc'+dt+'.csv')
