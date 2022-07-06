import csv
import argparse
from langdetect import detect_langs
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

f = csv.writer(open('languageDetected_'+dt+'.csv', 'w'))
f.writerow(['itemID']+['uri']+['collectionName']+['title']+['item_type']+['language'])

with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        itemID = row['itemID']
        uri = row['uri']
        collectionName = row['collectionName']
        title = row['title']
        item_type = row['type'].strip()
        if title.isupper():
            title = title.title()
        title_length = len(title)
        if title_length > 20:
            probabilities = detect_langs(title)
            match_found = ''
            for probability in probabilities:
                probability = str(probability)
                language = probability[:2]
                percent = probability[3:]
                percent = float(percent)
                if percent > .9:
                    f.writerow([itemID] + [uri] + [collectionName] + [title] + [item_type] + [language])
                    match_found == 'true'
                    break
                else:
                    match_found = 'false'
            if match_found == 'false':
                f.writerow([itemID] + [uri] + [collectionName] + [title] + [item_type] + [probabilities])
        else:
            f.writerow([itemID] + [uri] + [collectionName] + [title] + [item_type] + ['none'])