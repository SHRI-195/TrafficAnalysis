from collections import defaultdict

class TrafficFlowReducer:
    def __init__(self):
        self.traffic_data = defaultdict(list)

    def reduce(self, input_lines):
        for line in input_lines:
            stop_light, trips = line.strip().split("\t")
            stop_id_from, light_timing = stop_light.split(",")
            self.traffic_data[(stop_id_from, light_timing)].append(int(trips))

        for key, trips in self.traffic_data.items():
            stop_id_from, light_timing = key
            avg_trips = sum(trips) / len(trips)
            if avg_trips > 100:  # Threshold for congestion
                print(f"Optimize light timing at {stop_id_from}, currently at {light_timing}")
