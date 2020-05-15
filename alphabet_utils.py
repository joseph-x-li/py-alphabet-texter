import time

class AlphabetUtils:
    def __init__(self):
        self.times = [-1 for _ in range(26)]
        self.prev = ""
        self.now = ""
        self.KEY = "abcdefghijklmnopqrstuvwxyz"
        
    def __repr__(self):
        base = ""
        base += f"Previous String: {self.prev}\n"
        base += f"Current String: {self.now}\n"
        base += f"KEY: {self.KEY}\n"
        return base
        
    def _calculate_times(self):
        for i in range(26):
            if i >= len(self.now):
                self.times[i] = -1
            elif i >= len(self.prev):
                if (self.now[i] == self.KEY[i]):
                    self.times[i] = time.time()
                else:
                    self.times[i] = -1
            elif self.now[i] != self.prev[i]:
                if self.now[i] == self.KEY[i]:
                    self.times[i] = time.time()
                else:
                    self.times[i] = -1
        return
    
    def _get_correct_chars(self):
        base = [False for _ in range(26)]
        for i in range(min(len(self.now), 26)):
            if self.now[i] == self.KEY[i]:
                base[i] = True
        return base
            
    def _get_time_diffs(self):
        return [(y - x) for (x, y) in zip(self.times[:25], self.times[1:])]
    
    def tell(self, current_input):
        self.prev = self.now
        self.now = current_input
        self._calculate_times()
        return (current_input == self.KEY, 
                self._get_correct_chars(),
                self._get_time_diffs())