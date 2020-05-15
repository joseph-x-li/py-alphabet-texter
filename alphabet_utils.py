import time

class AlphabetUtils:
    def __init__(self, KEY = "abcdefghijklmnopqrstuvwxyz"):
        self.KEY = KEY
        self.KEYLEN = len(self.KEY)
        self.prev = ""
        self.now = ""
        self.times = [-1 for _ in range(self.KEYLEN)]
        
    def __repr__(self):
        base = ""
        base += f"Previous String: {self.prev}\n"
        base += f"Current String: {self.now}\n"
        base += f"KEY: {self.KEY}\n"
        return base
        
    def _calculate_times(self):
        for i in range(self.KEYLEN):
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
        base = [False for _ in range(self.KEYLEN)]
        for i in range(min(len(self.now), self.KEYLEN)):
            if self.now[i] == self.KEY[i]:
                base[i] = True
        return base
            
    def _get_time_diffs(self):
        return [(y - x) for (x, y) in zip(self.times[:(self.KEYLEN - 1)], self.times[1:])]
    
    def tell(self, current_input):
        self.prev = self.now
        self.now = current_input
        self._calculate_times()
        return (current_input == self.KEY, 
                self._get_correct_chars(),
                self._get_time_diffs())
        
    def set_KEY(self, new_key):
        self.KEY = new_key
        self.KEYLEN = len(self.KEY)
        return
    
    def reset(self):
        self.prev = ""
        self.now = ""
        self.times = [-1 for _ in range(self.KEYLEN)]
        return