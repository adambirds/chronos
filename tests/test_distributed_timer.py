from chronos.distributed_timer import DistributedChronosTimer
import time

def test_distributed_timer():
    with DistributedChronosTimer("Distributed Test") as timer:
        time.sleep(1)
    timer.add_timing(0.5)
    timer.add_timing(1.5)
    assert abs(timer.get_total_time("seconds") - 3.0) < 0.01

