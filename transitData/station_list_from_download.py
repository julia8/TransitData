import urllib
import zipfile
import csv

def unzip(filename):
    fh = open(filename, 'rb')
    z = zipfile.ZipFile(fh)
    filename
    for name in z.namelist():
        outpath = "/tmp/data/"
        z.extract(name, outpath)
        outpath =  outpath + name
    fh.close()
    return outpath

folder = "https://s3.amazonaws.com/tripdata/"
filename = '201309-citibike-tripdata.zip'
tmp = "/tmp/data/" + filename
infile = urllib.urlretrieve(folder + filename, tmp)
datafile = unzip(tmp)

with open(datafile) as infile:
    reader = csv.reader(infile)

    next(reader)
    for row in reader:
        # Trip Start station
        print( ','.join((str(row[3]), str(row[4]), str(row[5]), str(row[6]))))
        # Trip End station
        print( ','.join((str(row[7]), str(row[8]), str(row[9]), str(row[10]))))