python ../transitData/station_list.py | sort | uniq > stations.csv
python ../transitData/station_list_from_download.py | sort | uniq > stations_dl.csv
python ../transitData/station_list_from_download.py | sort | uniq > stations_201309.csv