import os
import time

class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.results = []

    def process_data(self):
        for item in self.data:
            time.sleep(0.5)  # Inefficient delay
            if item % 2 == 0:
                self.results.append(item * 2)
            else:
                self.results.append(item + 1)
        
    def save_results(self):
        file = open("results.txt", "w")  # File not closed properly
        for result in self.results:
            file.write(str(result) + "\n")
        
    def print_results(self):
        for i in range(len(self.results)):  # Inefficient iteration
            print("Result:", self.results[i])

data = [1, 2, 3, 4, 5]
processor = DataProcessor(data)
processor.process_data()
processor.save_results()
processor.print_results()
