import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

df_1 = pd.read_csv(filename, header=0)

df_1 = df_1.melt(id_vars=['oclc_id'])
print(df_1.head)
df_1.to_csv('melted_.csv')