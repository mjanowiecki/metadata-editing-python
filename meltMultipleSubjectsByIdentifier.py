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

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

df_1 = pd.read_csv(filename, header=0)
df_1['fast0'] = df_1['0_auth_name']+'|'+df_1['0_fast_id']
df_1['fast1'] = df_1['1_auth_name']+'|'+df_1['1_fast_id']
df_1['fast2'] = df_1['2_auth_name']+'|'+df_1['2_fast_id']
df_1 = df_1.drop(columns=['0_auth_name', '1_auth_name', '2_auth_name', '0_fast_id', '1_fast_id', '2_fast_id'])
print(df_1.head)
df_1 = df_1.melt(id_vars=['bib', 'old_subject'])
df_1 = df_1.dropna(subset=['value'], how='all')
print(df_1.head)

df_1[['header', 'identifier']] = df_1.value.str.split('|', expand=True)
df_1 = df_1.drop(columns=['value'])
print(df_1.head)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
df_1.to_csv(path_or_buf='squished_'+dt+'.csv', index=False)
