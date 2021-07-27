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
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter second filename (including \'.csv\'): ')


df = pd.read_csv(filename)

df_2 = pd.read_csv(filename2)

df_2 = df_2[['handle', 'bitstream']].copy()
df_2 = pd.pivot_table(df_2, index='handle',
                      values='bitstream',
                      aggfunc=lambda x: list(x))

df_2 = pd.DataFrame(df_2)
df_2 = df_2.reset_index()


def findBit(listValue, listType):
    if pd.notna(listValue):
        listValue = ast.literal_eval(listValue)
        print(listValue)
        for item in listValue:
            for index, row in df_2.iterrows():
                handle2 = row['handle']
                if handle == handle2:
                    bitstreams = row['bitstream']
                    for bitstream in bitstreams:
                        bitext = bitstream.rsplit('.', 1)
                        bit_string = bitext[0]
                        print(item, bit_string)
                        if bit_string == item:
                            print(bitstream)
                            listType.append(bitstream)


allItems = []
for index, row in df.iterrows():
    littleDict = {}
    lonelyList = []
    matchedList = []
    singleList = []
    handle = row['handle']
    lonely = row['lonely']
    matched = row['matched']
    print(matched)
    single = row['single']
    findBit(lonely, lonelyList)
    findBit(matched, matchedList)
    findBit(single, singleList)
    if lonelyList:
        littleDict['lonely'] = lonelyList
    print(matchedList)
    if matchedList:
        littleDict['matched'] = matchedList
    if singleList:
        littleDict['single'] = singleList
    littleDict['handle'] = handle
    allItems.append(littleDict)


allItems = pd.DataFrame.from_dict(allItems)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
allItems.to_csv('matchedBitstreams2_'+dt+'.csv')
