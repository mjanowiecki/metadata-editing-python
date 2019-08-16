import json
import requests
import secrets
import time
import csv
from datetime import datetime
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

secretsVersion = input('To edit production server, enter the name of the secrets file: ')
if secretsVersion != '':
    try:
        secrets = __import__(secretsVersion)
        print('Editing Production')
    except ImportError:
        print('Editing Stage')
else:
    print('Editing Stage')

baseURL = secrets.baseURL
email = secrets.email
password = secrets.password
filePath = secrets.filePath
verify = secrets.verify
skippedCollections = secrets.skippedCollections

startTime = time.time()
data = {'email':email,'password':password}
header = {'content-type':'application/json','accept':'application/json'}
session = requests.post(baseURL+'/rest/login', headers=header, verify=verify, params=data).cookies['JSESSIONID']
cookies = {'JSESSIONID': session}
headerFileUpload = {'accept':'application/json'}
cookiesFileUpload = cookies
status = requests.get(baseURL+'/rest/status', headers=header, cookies=cookies, verify=verify).json()
print('authenticated')

fileName = filePath+input('Enter fileName (including \'.csv\'): ')
replacedKey = input('Enter key: ')
replacementKey = replacedKey

f=csv.writer(open(filePath+'replacedKeyValuePair'+datetime.now().strftime('%Y-%m-%d %H.%M.%S')+'.csv', 'w'))
f.writerow(['itemID']+['replacedKey']+['replacedValue']+['replacementValue']+['delete']+['post'])

with open(fileName) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        itemMetadataProcessed = []
        itemID = row['link']
        dc_title = row['dc.title']
        dc_description_abstract =  row['dc.description.abstract']
        decade = row['dc.subject']

        itemMetadata = requests.get(baseURL+str(itemID)+'/metadata', headers=header, cookies=cookies, verify=verify).json()
        if decade != 'not converted':
            subjectElement = {'key': 'dc.subject', 'language':'en_US', 'value': decade}
            itemMetadataProcessed.append(subjectElement)
        for element in itemMetadata:
            languageValue = element['language']
            try:
                element['key']
            if element['key'] == 'dc.title':
                replacedValue1 = element['value']
                replacedKey1 = element['key']
                replacementKey1 = replacedKey
                updatedMetadataElement = {}
                updatedMetadataElement['key'] = replacementKey
                updatedMetadataElement['value'] = dc_title
                updatedMetadataElement['language'] = languageValue
                itemMetadataProcessed.append(updatedMetadataElement)

                provNote = '\''+replacedKey1+': '+replacedValue1+'\' was replaced by \''+replacementKey1+': '+dc_title+'\' through a batch process on '+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'.'
                provNoteElement = {}
                provNoteElement['key'] = 'dc.description.provenance'
                provNoteElement['value'] = provNote
                provNoteElement['language'] = 'en_US'
                itemMetadataProcessed.append(provNoteElement)
            elif element['key'] == 'dc.description.abstract':
                replacedValue2 = element['value']
                replacedKey2 = element['key']
                replacementKey2 = replacedKey
                updatedMetadataElement = {}
                updatedMetadataElement['key'] = replacementKey
                updatedMetadataElement['value'] = dc_description_abstract
                updatedMetadataElement['language'] = languageValue
                itemMetadataProcessed.append(updatedMetadataElement)

                provNote = '\''+replacedKey2+': '+replacedValue2+'\' was replaced by \''+replacementKey2+': '+dc_description_abstract+'\' through a batch process on '+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'.'
                provNoteElement = {}
                provNoteElement['key'] = 'dc.description.provenance'
                provNoteElement['value'] = provNote
                provNoteElement['language'] = 'en_US'
                itemMetadataProcessed.append(provNoteElement)

            else:
                itemMetadataProcessed.append(element)
        print(itemMetadata)
        itemMetadataProcessed = json.dumps(itemMetadataProcessed)

        delete = requests.delete(baseURL+str(itemID)+'/metadata', headers=header, cookies=cookies, verify=verify)
        print(delete)
        post = requests.put(baseURL+str(itemID)+'/metadata', headers=header, cookies=cookies, verify=verify, data=itemMetadataProcessed)
        print(post)
        f.writerow([itemID]+[replacedKey1]+[replacedValue1]+[dc_title]+[replacedKey2]+[replacedValue2]+[dc_description_abstract]+[delete]+[post])
