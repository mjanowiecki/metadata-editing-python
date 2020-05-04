import requests
import csv
from datetime import datetime
import argparse
from fuzzywuzzy import fuzz
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='Enter filename with csv.')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

# Some config for FAST and MESH APIs.
api_base_url = "http://fast.oclc.org/searchfast/fastsuggest"
fast_uri_base = "http://id.worldcat.org/fast/{0}"

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')


#  Find exact matches from FAST API.
def fastExact_function(search_subject):
    fast_url = api_base_url + '?&query=' + search_subject
    fast_url += '&queryIndex=suggestall&queryReturn=suggestall,idroot,auth,tag,raw&suggest=autoSubject&rows=5&wt=json'
    try:
        data = requests.get(fast_url).json()
        for item in data:
            if item == 'response':
                response = data.get(item)
                if response.get('numFound') > 0:
                    for metadata in response:
                        if metadata == 'docs':
                            keyInfo = response.get(metadata)
                            for info in keyInfo:
                                auth_name = info.get('auth')
                                fast_id = info.get('idroot')
                                ratio = fuzz.token_sort_ratio(auth_name, search_subject)
                                if auth_name == search_subject or ratio == 100:
                                    result_dict['auth_name'] = auth_name
                                    result_dict['fast_id'] = fast_id
                                    break
                                else:
                                    pass
    except ValueError:
        pass


#  Find close matches from FAST API
def fastClose_function(search_subject):
    global fast_found
    fast_url = api_base_url + '?&query=' + search_subject
    fast_url += '&queryIndex=suggestall&queryReturn=suggestall,idroot,auth,tag,raw&suggest=autoSubject&rows=5&wt=json'
    try:
        data = requests.get(fast_url).json()
        for item in data:
            if item == 'response':
                response = data.get(item)
                if response.get('numFound') > 0:
                    for metadata in response:
                        if metadata == 'docs':
                            keyInfo = response.get(metadata)
                            for count, info in enumerate(keyInfo[:5]):
                                auth_name = info.get('auth')
                                fast_id = info.get('idroot')
                                result_dict[str(count)+'_'+'auth_name'] = auth_name
                                result_dict[str(count)+'_'+'fast_id'] = fast_id
    except ValueError:
        pass


result_list = []
with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        result_dict = {}
        bib = row['bib']
        result_dict['bib'] = bib
        search_subject = row['subjects'].strip()
        result_dict['old_subject'] = search_subject
        print(search_subject)
        #  Improve quality of API search.
        search_subject = search_subject.replace(' -- ', ' ')
        search_subject = search_subject.replace('-', ' ')
        search_subject = search_subject.replace('.', '')
        #  Loop through function to find matches.
        fastExact_function(search_subject)
        data = result_dict.get('auth_name')
        if data is None:
            fastClose_function(search_subject)
        else:
            pass
        print(result_dict)
        result_list.append(result_dict)

df = pd.DataFrame.from_dict(result_list)
print(df.columns)
print(df.head)
df.to_csv(path_or_buf='fastResults_'+dt+'.csv', header='column_names', index=False)
