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
df_1['pair0'] = df_1['0_auth_name']+'|'+df_1['0_vocab_id']
df_1['pair1'] = df_1['1_auth_name']+'|'+df_1['1_vocab_id']
df_1['pair2'] = df_1['2_auth_name']+'|'+df_1['2_vocab_id']
df_1 = df_1.drop(columns=['0_auth_name', '1_auth_name', '2_auth_name', '0_vocab_id', '1_vocab_id', '2_vocab_id'])
print(df_1.head)
df_1 = df_1.melt(id_vars=['bib', 'old_subject'])
df_1 = df_1.dropna(subset=['value'], how='all')
print(df_1.head)

df_1[['header', 'identifier']] = df_1.value.str.split('|', expand=True)
df_1 = df_1.drop(columns=['value'])
print(df_1.head)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
df_1.to_csv(path_or_buf='meltedColumnPairs_'+dt+'.csv', index=False)