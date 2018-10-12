
import csv
import argparse
import itertools

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='enter filename to retreive. optional - if not provided, the script will ask for input')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = raw_input('Enter filename (including \'.csv\'): ')

f=csv.writer(open('sampledtitles.csv','wb'))
f.writerow(['samples'])

with open(filename) as csvfile:
     rows = csv.reader(csvfile)
     sampled_rows = itertools.islice(csvfile, 1, None, 40)
     for sample in sampled_rows:
         f.writerow([sample])
