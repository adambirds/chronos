from chronos.base_timer import BaseChronosTimer
import time

def test_base_timer_basic():
    with BaseChronosTimer("Base Timer Test") as timer:
        time.sleep(1)
    assert timer.get_elapsed("seconds") >= 1

def test_base_timer_conversion():
    with BaseChronosTimer("Conversion Test") as timer:
        time.sleep(1)
    assert timer.get_elapsed("milliseconds") >= 1000

def test_base_timer_threshold_warning(capfd):
    with BaseChronosTimer("Threshold Test", threshold=0.5) as timer:
        time.sleep(1)
    captured = capfd.readouterr()
    assert "WARNING: Threshold Test exceeded the threshold" in captured.out
