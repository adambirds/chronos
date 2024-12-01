from chronos.timer import ChronosTimer
import sys
import time

class ChronosTimerWithVisualization(ChronosTimer):
    def _report_progress(self):
        bar_length = 40
        while self._running:
            elapsed = time.perf_counter() - self.start_time
            converted = self._convert_time(elapsed, self.default_unit)
            progress = min(1, elapsed / self.threshold) if self.threshold else 0
            block = int(round(bar_length * progress))
            bar = "#" * block + "-" * (bar_length - block)
            sys.stdout.write(f"\r[{bar}] {converted:.2f} {self.default_unit} elapsed...")
            sys.stdout.flush()
            time.sleep(self.interval)
        print("")
