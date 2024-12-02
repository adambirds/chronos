# BatchChronosTimer

The `BatchChronosTimer` helps time multiple tasks and compute aggregate statistics like average, median, and total times.

## Example

```python
from chronos import BatchChronosTimer

def example_task():
    import time
    time.sleep(0.5)

batch_timer = BatchChronosTimer("Batch Example")
for _ in range(3):
    batch_timer.time_task(example_task)

stats = batch_timer.get_statistics("seconds")
print(f"Average time: {stats['average_time']} seconds")
print(f"Total time: {stats['total_time']} seconds")
```

## Methods

- **`time_task(task: callable, *args, **kwargs)`**: Time a single task and store the elapsed time.
- **`get_statistics(unit: str = "seconds")`**: Return aggregate statistics for the batch.
