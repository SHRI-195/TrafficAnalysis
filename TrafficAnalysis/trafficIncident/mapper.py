import csv

class TrafficIncidentMapper:
    def __init__(self, filename, threshold_speed=20):
        self.filename = filename
        self.threshold_speed = threshold_speed

    def map(self):
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                speed = float(row['speed'])
                stop_id_from = row['stop_id_from']
                if speed < self.threshold_speed:
                    print(f"{stop_id_from}\t{speed}")
