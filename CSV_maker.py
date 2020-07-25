from Create_inverted_index import *

import csv

csv_inverted_index = inverted_index
with open('inverted_index.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, csv_inverted_index.keys())
    w.writeheader()
    w.writerow(csv_inverted_index)