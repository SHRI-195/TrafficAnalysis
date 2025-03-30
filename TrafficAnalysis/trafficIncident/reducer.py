from collections import defaultdict

class TrafficIncidentReducer:
    def __init__(self):
        self.incidents = defaultdict(list)

    def reduce(self, input_lines):
        for line in input_lines:
            stop_id_from, speed = line.strip().split("\t")
            self.incidents[stop_id_from].append(float(speed))

        for stop_id, speeds in self.incidents.items():
            if len(speeds) > 5:  
                print(f"Traffic incident detected at {stop_id} with {len(speeds)} low-speed instances.")
