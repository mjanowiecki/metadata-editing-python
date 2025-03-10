"""Prints URL listed in CSV column if 200 code is not returned."""

import requests
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-c', '--column_name')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.column_name:
    column_name = args.column_name
else:
    column_name = input('Enter column to check: ')

df = pd.read_csv(filename, header=0)
link_list = df[column_name].tolist()

bad_links = []
for count, link in enumerate(link_list):
    r = requests.head(link, timeout=120)
    print(count, r.status_code)
    if r.status_code != 200:
        bad_links.append(link)
print(bad_links)
