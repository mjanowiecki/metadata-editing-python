import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

df_1 = pd.read_csv(filename, header=0)
combined = []
print(df_1.columns)
for index, row in df_1.iterrows():
    row = dict(row)
    newDict = {}
    if pd.isna(row.get('bib_p_1')) and pd.isna(row.get('match_p_1')):
        newDict['mergedBib'] = row.get('bib_p_2')
        newDict['mergedMatch'] = row.get('match_p_2')
        newDict['handle'] = row.get('handle')
        combined.append(newDict)
    elif pd.isna(row.get('bib_p_2')) and pd.isna(row.get('match_p_2')):
        newDict['mergedBib'] = row.get('bib_p_1')
        newDict['mergedMatch'] = row.get('match_p_1')
        newDict['handle'] = row.get('handle')
        combined.append(newDict)
    elif row.get('match_p_2') == 'none':
        newDict['mergedBib'] = row.get('bib_p_1')
        newDict['mergedMatch'] = row.get('match_p_1')
        newDict['handle'] = row.get('handle')
        combined.append(newDict)
    elif row.get('match_p_2') == 'probable':
        newDict['mergedBib'] = row.get('bib_p_1')
        newDict['mergedMatch'] = row.get('match_p_1')
        newDict['handle'] = row.get('handle')
        combined.append(newDict)
    else:
        print(row)
df_2 = pd.DataFrame(combined)

frame = pd.merge(df_1, df_2, how='left', on=['handle'], suffixes=('_1', '_2'))

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
frame.to_csv(path_or_buf='allFixed_'+dt+'.csv')
