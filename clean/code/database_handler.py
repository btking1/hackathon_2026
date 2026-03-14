class DataProcessor:
    def __init__(self, data):
        self.data = data
    
    def filter_by_threshold(self, threshold):
        return [item for item in self.data if item > threshold]
    
    def compute_average(self):
        if not self.data:
            return 0
        return sum(self.data) / len(self.data)
    
    def normalize(self):
        min_val = min(self.data)
        max_val = max(self.data)
        if max_val == min_val:
            return [0] * len(self.data)
        return [(x - min_val) / (max_val - min_val) for x in self.data]
