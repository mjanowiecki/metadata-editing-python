"""Loops through levels of XML to create generic CSV"""


import pandas as pd
import argparse
from datetime import datetime
from xml.etree import ElementTree
import os
import re
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory')
args = parser.parse_args()

if args.directory:
    directory = args.directory
else:
    directory = input('Enter directory: ')

prefix_string = ''

all_items = []
for filename in os.listdir(directory):
    filename = directory + "/" + filename
    if filename.endswith('.xml'):
        print(filename)
        tree = ElementTree.parse(filename)
        root = tree.getroot()
        item_dictionary = {}
        for child in root.iter():
            tag = child.tag
            tag = tag.replace(prefix_string, '')
            attributes = child.attrib
            text = child.text
            if text is not None:
                text = re.sub(r'\s{2}+', "", text)
                text = text.strip()
            if text != "" and (text is not None):
                print('"'+text+'"')
                tag_value = item_dictionary.get(tag)
                if tag_value is None:
                    item_dictionary[tag] = text
                else:
                    new_tag_value = tag_value+'|'+text
                    item_dictionary[tag] = new_tag_value
                if attributes:
                    attribute_list = []
                    for key, value in attributes.items():
                        combined = key + '=' + value
                        attribute_list.append(combined)
                    attribute_string = ', '.join(attribute_list)
                    tag_value = item_dictionary.get(tag)
                    new_tag_value = tag_value+' ('+attribute_string+')'
                    item_dictionary[tag] = new_tag_value
            else:
                if attributes:
                    attribute_list = []
                    for key, value in attributes.items():
                        combined = key+'='+value
                        attribute_list.append(combined)
                    attribute_string = ', '.join(attribute_list)
                    tag_value = item_dictionary.get(tag)
                    if tag_value is None:
                        item_dictionary[tag] = attribute_string
                    else:
                        new_tag_value = tag_value + '|' + attribute_string
                        item_dictionary[tag] = new_tag_value
        all_items.append(item_dictionary)

dt = datetime.now().strftime('%Y-%m-%d%H.%M.%S')
all_items = pd.DataFrame.from_records(all_items)
all_items.to_csv('metadataFromXML_'+dt+'.csv', index=False, quoting=csv.QUOTE_ALL)

