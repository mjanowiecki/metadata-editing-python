import json
from pprint import pprint
from operator import itemgetter
import requests
import csv
import time
from datetime import datetime
from fuzzywuzzy import fuzz
import re
from itertools import chain
import codecs
import unicodedata
import argparse
import ast



parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='enter filename with csv. optional - if not provided, the script will ask for input')
parser.add_argument('-b', '--batch', help='Batch letter to name outputs. optional - if not provided, the script will ask for input')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

if args.batch:
    batch = args.batch
else:
    batch = input('Enter batch letter: ')

# some config
api_base_url = "http://fast.oclc.org/searchfast/fastsuggest"
#For constructing links to FAST.
fast_uri_base = "http://id.worldcat.org/fast/{0}"


f = csv.writer(open('subjectMatchesToReview_Batch'+batch+'2_'+datetime.now().strftime('%Y-%m-%d %H.%M.%S')+'.csv', 'w'))
f.writerow(['uri']+['dc.subject']+['cleanedSubject']+['result_list']+['result_list_edited']+['match'])


row_count = 0
with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        row_count = row_count + 1
        print(row_count)
        uri = row['uri']
        old_subject = row['dc.subject']
        search_subject = row['cleanedSubject']
        search_list = row['results']
        search_list = ast.literal_eval(search_list)
        result_list = []
        for subject in search_list:
            subject = subject.replace("Md", "Maryland")
            print(subject)
            url = api_base_url + '?&query=' + subject
            url += '&queryIndex=suggestall&queryReturn=suggestall,idroot,auth,tag,raw&suggest=autoSubject&rows=3&wt=json'
            try:
                data = requests.get(url).json()
                for item in data:
                    if item == 'response':
                        response = data.get(item)
                        if response.get('numFound') == 0:
                            pass
                        else:
                            for metadata in response:
                                if metadata == 'docs':
                                    keyInfo = response.get(metadata)
                                    for info in keyInfo:
                                        name = info.get('auth')
                                        ratio = fuzz.token_sort_ratio(name, subject)
                                        print('Options', name, ratio)
                                        if name == subject:
                                            if name not in result_list:
                                                result_list.append(name)
                                                break
                                        elif ratio == 100:
                                            if name not in result_list:
                                                result_list.append(name)
                                                break
                                        elif ratio > 30:
                                            if name not in result_list:
                                                result_list.append(name)
                                        else:
                                            pass
                    else:
                        pass
            except:
                pass

        f.writerow([uri]+[old_subject]+[search_subject]+[result_list]+[result_list])
    else:
        f.writerow([uri]+[old_subject]+[search_subject]+[result_list]+[result_list])
