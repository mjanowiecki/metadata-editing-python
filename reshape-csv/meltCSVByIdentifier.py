"""

local_id	name	            genus
3VMPT       Litoria tyleri	    Litoria
3VHQP	    Lithobates pipiens	Lithobates
76CHN	    Pelophylax plancyi	Pelophylax

local_id    variable	    value
3VMPT       name	    Litoria tyleri
3VHQP	    name        Lithobates pipiens
76CHN	    name        Pelophylax plancyi
3VMPT       genus       Litoria
3VHQP	    genus       Lithobates
76CHN	    genus	    Pelophylax

"""

import pandas as pd
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-id', '--identifier')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.identifier:
    identifier = args.identifier
else:
    identifier = input('Enter name of identifier columns: ')

df_1 = pd.read_csv(filename, header=0)

df_1 = df_1.melt(id_vars=[identifier])
print(df_1.head)
df_1.to_csv('melted_.csv', index=False, quoting=csv.QUOTE_ALL)
