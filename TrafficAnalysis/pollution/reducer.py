from collections import defaultdict

class PollutionReducer:
    def __init__(self):
        self.pollution_data = defaultdict(list)

    def reduce(self, input_lines):
        for line in input_lines:
            stop_id_from, data = line.strip().split("\t")
            num_trips, degree_of_congestion = map(float, data.split(","))
            self.pollution_data[stop_id_from].append((num_trips, degree_of_congestion))

        for stop_id, data in self.pollution_data.items():
            total_trips = sum([x[0] for x in data])
            avg_congestion = sum([x[1] for x in data]) / len(data)
            print(f"Pollution analysis for {stop_id}: Total Trips: {total_trips}, Average Congestion: {avg_congestion}")
