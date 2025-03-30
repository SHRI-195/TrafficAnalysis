import csv

class PollutionMapper:
    def __init__(self, filename):
        self.filename = filename

    def map(self):
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                stop_id_from = row['stop_id_from']
                num_trips = int(row['Number_of_trips'])
                degree_of_congestion = float(row['Degree_of_congestionin'])
                print(f"{stop_id_from}\t{num_trips},{degree_of_congestion}")
