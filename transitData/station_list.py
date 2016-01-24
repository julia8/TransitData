import csv

with open('/tmp/data/2013-07-CitiBiketripdata.csv') as infile:
    reader = csv.reader(infile)

    next(reader)
    for row in reader:
        # Trip Start station
        print( ','.join((str(row[3]), str(row[4]), str(row[5]), str(row[6]))))
        # Trip End station
        print( ','.join((str(row[7]), str(row[8]), str(row[9]), str(row[10]))))