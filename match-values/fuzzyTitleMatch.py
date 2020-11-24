import argparse
from datetime import datetime
from fuzzywuzzy import fuzz, process
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-f2', '--file2')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter first filename (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter second filename (including \'.csv\'): ')

df_1 = pd.read_csv(filename, header=0)
print(df_1.columns)
df_2 = pd.read_csv(filename2, header=0)
print(df_2.columns)

df_1.title.str.strip()
df_2.title.str.strip()

df_1.sort_values(by=['title'], inplace=True)
df_2.sort_values(by=['title'], inplace=True)


def fuzzy_merge(df_1, df_2, key1, key2):
    """
    :param df_1: the left table to join
    :param df_2: the right table to join
    :param key1: key column of the left table
    :param key2: key column of the right table
    :param limit: number of matches returned, sorted high to low

    """
    list_2 = df_2[key2].tolist()

    m = df_1[key1].apply(lambda x: process.extract(x, list_2,
                         scorer=fuzz.ratio, limit=2))
    df_1['matches'] = m
    df_1['match1'] = df_1.matches.str.get(0)
    df_1['match2'] = df_1.matches.str.get(1)
    return df_1


frame = fuzzy_merge(df_1, df_2, 'title', 'title')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
frame.to_csv('fuzzyJoin_'+dt+'.csv', index=False)
