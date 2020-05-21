import csv
import argparse
from datetime import datetime
from fuzzywuzzy import fuzz
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')


def addToDict(key):
    value = row[key]
    value = value.split('|')
    name_dict[key] = value


all_rows = []
with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        allNames = row['names_fixed']
        allNames = allNames.split('|')
        name_dict = {}
        addToDict('director')
        addToDict('producer')
        addToDict('announcer')
        addToDict('presenter')
        addToDict('writer')
        addToDict('narrator')
        values = name_dict.values()
        values = [v for little_list in values for v in little_list if v]
        values = set(values)
        for name in allNames:
            ratio_dict = {}
            for count, value in enumerate(values):
                pair = (name, value)
                ratio = fuzz.token_sort_ratio(name, value)
                ratio = str(ratio).zfill(3)
                ratio = str(ratio)+'_'+str(count)
                ratio_dict[ratio] = pair
            ratioValues = sorted(ratio_dict.keys(), reverse=True)
            try:
                highest = ratioValues[0]
                trueRatio = highest[:3]
                trueRatio = int(trueRatio)
                highestpair = ratio_dict.get(highest)
                if trueRatio > 50:
                    highestpair = ratio_dict.get(highest)
                    print(trueRatio)
                    print(highestpair)
                    for k, v in name_dict.items():
                        for count, item in enumerate(v):
                            if item == highestpair[1]:
                                v[count] = highestpair[0]
                                name_dict[k] = v
            except IndexError:
                pass
        addToDict('bib')
        addToDict('names_fixed')
        for k, v in name_dict.items():
            v = '|'.join(v)
            name_dict[k] = v
        all_rows.append(name_dict)

df = pd.DataFrame.from_dict(all_rows)
print(df.head(15))
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
df.to_csv(path_or_buf='relators_'+dt+'.csv', header='column_names', encoding='utf-8', sep=',', index=False)
