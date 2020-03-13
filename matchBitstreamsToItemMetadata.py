import argparse
from datetime import datetime
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-f2', '--file2')
parser.add_argument('-hi', '--hierarchy')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter 2nd filename (including \'.csv\'): ')
if args.hierarchy:
    hierarchy = args.hierarchy
else:
    hierarchy = input('Want to map parent-child hiearchies? yes or no: ')

df = pd.read_csv(filename)
df_2 = pd.read_csv(filename2)

df['handle'] = df['dc.identifier.uri'].copy()
df.handle = df.handle.str.replace('http://jhir.library.jhu.edu/handle/', '')

new_df = pd.merge(df_2, df, how='left', on='handle')

if hierarchy == 'yes':
    size = new_df.handle.value_counts()
    for i, v in size.items():
        if v == 1:
            size[i] = 'solo'
        elif v > 1:
            size[i] = 'child'
            print(v)
    size = size.to_frame(name='hierarchy')
    size.index.name = 'handle'
    new_df = pd.merge(new_df, size, how='left', on='handle')
    parents = new_df.loc[new_df['hierarchy'] == 'child']
    parents.hierarchy = parents.hierarchy.str.replace('child', 'parent')
    parents = parents.drop(columns=['bitstream_1', 'bitstream_2'])
    parents = parents.drop_duplicates()
    print(parents.head)
    new_df = new_df.append(parents, ignore_index=True, sort=True)
else:
    pass


print(new_df.columns)
print(new_df.head)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
new_df.to_csv(path_or_buf='remediatedBitstreams_'+dt+'.csv', index=False)
