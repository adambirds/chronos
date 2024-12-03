# ChronosTimer

`ChronosTimer` provides the core functionality for timing tasks with features like:

-   Unit conversion (e.g., seconds, minutes, milliseconds).
-   Threshold warnings.
-   Logging to a file.
-   Real-time progress reporting.

## Example

```python
from chronos import ChronosTimer

with ChronosTimer("Example Task") as timer:
    import time
    time.sleep(1)

print(f"Elapsed time: {timer.get_elapsed('seconds')} seconds")
```

## Parameters

| Parameter      | Type    | Default   | Description                                          |
| -------------- | ------- | --------- | ---------------------------------------------------- |
| `name`         | `str`   | `None`    | Name of the task being timed.                        |
| `log_file`     | `str`   | `None`    | Path to log file for saving timing data.             |
| `threshold`    | `float` | `None`    | Warn if the elapsed time exceeds this threshold.     |
| `interval`     | `float` | `None`    | Interval for real-time progress reporting (seconds). |
| `default_unit` | `str`   | `seconds` | Default time unit for output.                        |
