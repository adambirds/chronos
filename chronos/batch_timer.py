from statistics import mean, median
from typing import Any, List

from chronos.base_timer import BaseChronosTimer


class BatchChronosTimer:
    def __init__(self, name: str = None, default_unit: str = "seconds") -> None:
        self.name = name
        self.default_unit = default_unit
        self.timings: List[float] = []

    def time_task(self, task: callable, *args: list[str], **kwargs: dict[str, Any]) -> None:
        with BaseChronosTimer(name=self.name, default_unit=self.default_unit) as timer:
            task(*args, **kwargs)
        self.timings.append(timer.elapsed)

    def get_statistics(self, unit: str = "seconds") -> dict[str, float]:
        # Use a BaseChronosTimer instance to perform the conversion
        converter = BaseChronosTimer(name="Batch Converter", default_unit=unit)
        converted_timings = [converter._convert_time(t, unit) for t in self.timings]
        return {
            "average_time": mean(converted_timings),
            "median_time": median(converted_timings),
            "total_time": sum(converted_timings),
            "timing_count": len(self.timings),
        }
