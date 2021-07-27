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

for count, link in enumerate(linkList):
    print(count)
    r = requests.head(link, timeout=120)
    if r.status_code != 200:
        print(link, r.status_code)
