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
    filename2 = input('Enter csv with marc data (including \'.csv\'): ')

df_1 = pd.read_csv(filename, header=0)
df_2 = pd.read_csv(filename2, header=0)

counts = df_2.url.value_counts()
print(counts.head)


map_list = []
for i, v in counts.iteritems():
    print(i, v)
    if v > 1:
        df_temp = df_2.loc[df_2['url'] == i]
        maps = len(df_temp[df_temp.type == 'map'])
        if maps > 1:
            i = i.replace('https://jscholarship.library.jhu.edu/handle/', '')
            map_list.append({'handle': i, 'type': 'multiple', 'numberOfMaps': maps})

m_df = pd.DataFrame.from_dict(map_list)
frame = pd.merge(df_1, m_df, how='left', on=['handle'], suffixes=('_1', '_2'))

print(frame.columns)
print(frame.head)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
frame.to_csv(path_or_buf='mergedCSV_'+dt+'.csv')
