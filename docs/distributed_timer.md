# DistributedChronosTimer

The `DistributedChronosTimer` aggregates timing data from multiple sources. It is ideal for distributed systems where timing data from multiple machines or processes needs to be combined.

## Example

```python
from chronos import DistributedChronosTimer

with DistributedChronosTimer("Distributed Task") as timer:
    import time
    time.sleep(1)

# Add external timings
timer.add_timing(0.5)
timer.add_timing(1.5)

print(f"Total elapsed time: {timer.get_total_time('seconds')} seconds")
```

## Methods

- **`add_timing(elapsed_time: float)`**: Add external timing data.
- **`get_total_time(unit: str = "seconds")`**: Get the total elapsed time (local + external).
