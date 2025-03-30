import csv

class TrafficFlowMapper:
    def __init__(self, filename):
        self.filename = filename

    def map(self):
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                stop_id_from = row['stop_id_from']
                light_timing = int(row['SRI'])  
                num_trips = int(row['Number_of_trips'])
                
                print(f"{stop_id_from},{light_timing}\t{num_trips}")
