import requests
import pandas as pd
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

df = pd.read_csv(filename)
linkList = df['link'].tolist()

bad_links = []
for count, link in enumerate(linkList):
    r = requests.head(link, timeout=120)
    print(count, r.status_code)
    if r.status_code != 200:
        bad_links.append(link)
print(bad_links)
