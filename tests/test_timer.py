from chronos.timer import ChronosTimer
import time

def test_basic_timer():
    with ChronosTimer("Basic Test") as timer:
        time.sleep(1)
    assert timer.get_elapsed("seconds") >= 1
