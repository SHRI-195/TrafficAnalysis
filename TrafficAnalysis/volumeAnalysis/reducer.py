from collections import defaultdict

class TrafficVolumeReducer:
    def __init__(self):
        self.traffic_data = defaultdict(list)

    def reduce(self, input_lines):
        for line in input_lines:
            stop_time, trips = line.strip().split("\t")
            stop_id_from, time = stop_time.split(",")
            self.traffic_data[(stop_id_from, time)].append(int(trips))

        for key, trips in self.traffic_data.items():
            stop_id_from, time = key
            avg_trips = sum(trips) / len(trips)
            print(f"{stop_id_from},{time}\t{avg_trips}")
