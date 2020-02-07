import csv
import argparse
import ast
from fuzzywuzzy import fuzz
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

f = csv.writer(open('fuzzyListMatches_'+dt+'.csv', 'w', encoding='utf-8'))
f2 = csv.writer(open('noMatches_'+dt+'.csv', 'w', encoding='utf-8'))


def convertDictToList(dict):
    if dict:
        valueList = list(ratio_matches.values())
        keyList = list(ratio_matches.keys())
        dictList = valueList + keyList
    else:
        dictList = []
    return dictList


with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        list_to_combinate = row['bitstreams']
        handle = row['handle']
        list_to_combinate = ast.literal_eval(list_to_combinate)
        ratio_matches = {}
        if isinstance(list_to_combinate, list):
            item_count = len(list_to_combinate)
            print('count:'+str(item_count))
            if item_count > 1:
                list_copy = list_to_combinate.copy()
                compares = 0
                for item in list_to_combinate:
                    list_copy.remove(item)
                    if list_copy:
                        for item2 in list_copy:
                            ratio = fuzz.token_sort_ratio(item, item2)
                            compares = compares + 1
                            if ratio > 90:
                                ratio_matches[item] = item2
        dictList = convertDictToList(ratio_matches)
        set1 = set(dictList)
        set2 = set(list_to_combinate)
        not_matched = set1.symmetric_difference(set2)
        if not_matched:
            not_matched = list(not_matched)
            ratio_matches['not matched'] = not_matched
        for key, value in ratio_matches.items():
            if key == 'not matched':
                for v in value:
                    f2.writerow([handle]+[v])
            else:
                f.writerow([handle]+[key]+[value])
