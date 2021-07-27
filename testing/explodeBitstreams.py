import argparse
from datetime import datetime
import pandas as pd
import ast

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-f2', '--file2')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter first filename (including \'.csv\'): ')


df = pd.read_csv(filename)


df_matched = df[['handle', 'matched']].copy()
allItems = []
for index, row in df_matched.iterrows():
    littleDict = {}
    handle = row['handle']
    matched = row['matched']
    if pd.notna(matched):
        matched = ast.literal_eval(matched)
        for i in range(len(matched)-1):
            pair = [matched[i], matched[i+1]]
            print(pair)
            pair0 = pair[0].rsplit('.', 1)
            pair0 = pair0[0]
            pair1 = pair[1].rsplit('.', 1)
            pair1 = pair1[0]
            print(pair0, pair1)
            if pair0 == pair1:
                littleDict = {}
                littleDict['handle'] = handle
                littleDict['matchedPair'] = pair
                allItems.append(littleDict)
                print(littleDict)
            else:
                pass

allItems = pd.DataFrame.from_dict(allItems)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
allItems.to_csv('matchedBitstreamsExploded_'+dt+'.csv')
