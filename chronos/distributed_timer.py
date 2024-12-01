from typing import List
from chronos.base_timer import BaseChronosTimer

class DistributedChronosTimer(BaseChronosTimer):
    def __init__(self, name: str = None, default_unit: str = "seconds"):
        super().__init__(name=name, default_unit=default_unit)
        self._external_timings: List[float] = []

    def add_timing(self, elapsed_time: float):
        self._external_timings.append(elapsed_time)

    def get_total_time(self, unit: str = "seconds") -> float:
        if not self.elapsed:
            raise RuntimeError("Timer has not finished yet.")
        total_elapsed = self.elapsed + sum(self._external_timings)
        return self._convert_time(total_elapsed, unit)
