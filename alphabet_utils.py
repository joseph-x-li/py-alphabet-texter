import time


class AlphabetUtils:
    def __init__(self, key):
        """Initialize an AlphabetUtils object.

        Args:
            key (string): Reference string
        """
        self.key = key
        self.keylen = len(self.key)
        self._prev = ""
        self._now = ""
        self.best_time = None
        self.recent_time = None
        self.times = [-1 for _ in range(self.keylen)]

    def __repr__(self):
        return f"AlphabetUtils({self.key})"

    def _calculate_times(self):
        for i in range(self.keylen):
            if i >= len(self._now):
                self.times[i] = -1
            elif i >= len(self._prev):
                if self._now[i] == self.key[i]:
                    self.times[i] = time.time()
                else:
                    self.times[i] = -1
            elif self._now[i] != self._prev[i]:
                if self._now[i] == self.key[i]:
                    self.times[i] = time.time()
                else:
                    self.times[i] = -1

    def _get_correct_chars(self):
        ret_val = [False for _ in range(self.keylen)]
        for i in range(min(len(self._now), self.keylen)):
            if self._now[i] == self.key[i]:
                ret_val[i] = True
        return ret_val

    def _get_time_diffs(self):
        return [
            (y - x) for (x, y) in zip(self.times[: (self.keylen - 1)], self.times[1:])
        ]

    def tell(self, current_input):
        """Test the user's current input against the key.

        Args:
            current_input (string): The user's input.

        Returns:
            (bool, List[bool], List[float]): Boolean of whether current_input == key,
                list of correct characters,
                list of time differentials
        """
        self._prev = self._now
        self._now = current_input
        self._calculate_times()
        correct = current_input == self.key
        time_diffs = self._get_time_diffs()
        if correct:
            self.recent_time = sum(time_diffs)
            self.best_time = (
                self.recent_time
                if self.best_time is None
                else min(self.best_time, self.recent_time)
            )

        return (correct, self._get_correct_chars(), time_diffs)

    def set_key(self, new_key):
        """Set a new key and reset all times.

        Args:
            new_key (string): The new key.
        """
        self.key = new_key
        self.keylen = len(self.key)
        self.reset()

    def reset(self):
        """Reset all data fields, excluding best, recent, and key.
        """
        self._prev = ""
        self._now = ""
        self.times = [-1 for _ in range(self.keylen)]

    def get_scores(self):
        """Get recent and best scores.

        Returns:
            (string, string): First string is recent time. Second string is best time.
                Returns "-" if no recent/best time can be found.
        """
        x = "-" if self.recent_time is None else f"{self.recent_time:.3f}"
        y = "-" if self.best_time is None else f"{self.best_time:.3f}"
        return (x, y)

    def reset_secores(self):
        """Reset best and recent times.
        """
        self.recent_time = None
        self.best_time = None
