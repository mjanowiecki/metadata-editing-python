import csv
import argparse
from langdetect import detect_langs

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

f = csv.writer(open('languagedetection.csv', 'w'))
f.writerow(['itemID']+['uri']+['collectionName']+['title']+['type']+['language'])

with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        itemID = row['itemID']
        uri = row['uri']
        collectionName = row['collectionName']
        title = row['title']
        type = row['type'].strip()
        if title.isupper():
            title = title.title()
        title_length = len(title)
        if title_length > 20:
            probabilities = detect_langs(title)
            matchfound = ''
            for probability in probabilities:
                probability = str(probability)
                language = probability[:2]
                percent = probability[3:]
                percent = float(percent)
                if percent > .9:
                    f.writerow([itemID]+[uri]+[collectionName]+[title]+[type]+[language])
                    matchfound == 'true'
                    break
                else:
                    matchfound = 'false'
            if matchfound == 'false':
                f.writerow([itemID]+[uri]+[collectionName]+[title]+[type]+[probabilities])
        else:
            f.writerow([itemID]+[uri]+[collectionName]+[title]+[type]+['none'])
