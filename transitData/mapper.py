import csv
from datetime import datetime

with open('/tmp/data/2013-07-count.csv','w') as outfile, \
    open('/tmp/data/2013-07-stations.csv','w') as stationsfile, \
    open('/tmp/data/2013-07-CitiBiketripdata.csv') as infile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    station_writer = csv.writer(stationsfile)

    next(reader)
    for row in reader:
        # 2013-07-01 00:00:00
        writer.writerow(
            (
                str(datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S').strftime('%H')),
                "field2"
            )
        )

        writer.writerow(str[row])
            
