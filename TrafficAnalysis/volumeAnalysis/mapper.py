import csv

class TrafficVolumeMapper:
    def __init__(self, filename):
        self.filename = filename

    def map(self):
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                stop_id_from = row['stop_id_from']
                time = row['time']
                num_trips = int(row['Number_of_trips'])
                print(f"{stop_id_from},{time}\t{num_trips}")
