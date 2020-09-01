import csv
import argparse
import ast
from fuzzywuzzy import fuzz
from datetime import datetime
import random
import string

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
    # Combine keys and values from dictionary into single list.
    if dict:
        dict1 = dict.copy()
        valueList = list(dict1.values())
        keyList = list(dict1.keys())
        dictList = valueList + keyList
    else:
        dictList = []
    return dictList


def checkIfDuplicates(listOfElems):
    # Check if given list contains any duplicates.
    setList = set(listOfElems)
    setList = list(setList)
    difference = len(listOfElems) - len(setList)
    return difference


def notInDict(v1, v2, dict):
    # Make sure v1 or v2 are not keys or values in dictonary.
    if v1 and v2 not in dict.values():
        if dict.get(v1) and matches.get(v2) is None:
            return True


total_count = 0
matched_count = 0
noMatches_count = 0
with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        # Get list of possible matches from csv.
        list_to_combinate = row['bitstreams']
        handle = row['handle']
        list_to_combinate = ast.literal_eval(list_to_combinate)
        item_count = len(list_to_combinate)
        total_count = total_count + item_count
        ratio_matches = {}
        matches = {}
        no_match = {}
        ratioList = []

        # Get fuzzy matches for pairs of items in list.
        # Add any item matches as list value to ratio_matches.
        # Key is ratio + randomly generated 4 letter string.
        if item_count >= 2:
            list_copy = list_to_combinate.copy()
            for item in list_to_combinate:
                list_copy.remove(item)
                if list_copy:
                    for item2 in list_copy:
                        ratio = fuzz.token_sort_ratio(item, item2)
                        if ratio > 85:
                            random_str = ''.join(random.choices(string.ascii_letters, k=4))
                            ratio = str(ratio) + random_str
                            ratio_matches[ratio] = [item, item2]
                            ratioList.extend([item, item2])

        # Check to see if any items are duplicated in dictionary values.
        if ratioList:
            result = checkIfDuplicates(ratioList)
            copy_ratio = ratio_matches.copy()
            for key, value in reversed(sorted(ratio_matches.items())):
                v1_1 = value[0]
                v1_2 = value[1]
                key_int = int(key[:-4])
                result = result
                # If no duplicates, add item pair as k, v to dict 'matches'.
                if result == 0:
                    matches[v1_1] = v1_2
                # If duplicates, add item pair with highest ratio to 'matches'.
                elif result > 0:
                    del copy_ratio[key]
                    if ratioList.count(v1_1) == 1 and ratioList.count(v1_2) == 1:
                        matches[v1_1] = v1_2
                    elif ratioList.count(v1_1) or ratioList.count(v1_2) > 1:
                        for key2, value2 in copy_ratio.items():
                            if v1_1 or v1_2 in value2:
                                v2_1 = value2[0]
                                v2_2 = value2[1]
                                key2_int = int(key2[:-4])
                                if key_int >= key2_int:
                                    if notInDict(v1_1, v1_2, matches):
                                        matches[v1_1] = v1_2
                                elif key2_int > key_int:
                                    if notInDict(v2_1, v2_2, matches):
                                        matches[v2_1] = v2_2
                                else:
                                    pass
                    else:
                        print('ERROR')

        # Determine if any items from original list are unmatched.
        dictList = convertDictToList(matches)
        set1 = set(dictList)
        set2 = set(list_to_combinate)
        not_matched = list(set2.difference(set1))
        # If unmatched, add to dicionary 'not_matched'.
        if not_matched:
            no_match[handle] = not_matched

        # Make spreadsheets from 'matches' and 'not_matched' dicionaries.
        for key, value in matches.items():
            f.writerow([handle]+[key]+[value])
            matched_count = matched_count + 2
        for key, value in no_match.items():
            for v in value:
                f2.writerow([key]+[v])
                noMatches_count = noMatches_count + 1

print('total count:'+str(total_count))
print('matched count:'+str(matched_count))
print('no matches count:'+str(noMatches_count))
