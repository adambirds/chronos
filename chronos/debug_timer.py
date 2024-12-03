import signal
import time

from chronos.timer import ChronosTimer


class DebuggingChronosTimer(ChronosTimer):
    def __enter__(self):
        signal.signal(signal.SIGTSTP, self._pause_timer)  # Capture Ctrl+Z for pausing
        signal.signal(signal.SIGCONT, self._resume_timer)  # Capture resume signal
        return super().__enter__()

    def _pause_timer(self, signum, frame):
        print("\nTimer paused. Press Ctrl+Z again to resume.")
        self._running = False
        self._pause_time = time.perf_counter()

    def _resume_timer(self, signum, frame):
        print("Timer resumed.")
        self._running = True
        self.start_time += time.perf_counter() - self._pause_time
