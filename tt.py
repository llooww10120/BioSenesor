import csv
from os import write
with open('te.csv' ,'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['t','tt','tt'])
