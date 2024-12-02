# Welcome to Chronos

Chronos is a Python library for advanced task timing and performance monitoring. With features like distributed timing, batch timing, real-time visualization, and debugging-friendly timers, Chronos provides powerful tools for developers.

## Quickstart

Install Chronos using pip:

```
pip install chronos-context-timer
```

Start timing tasks with the basic `ChronosTimer`:

```python
from chronos import ChronosTimer

with ChronosTimer("My Task") as timer:
    # Simulate work
    import time
    time.sleep(1)

print(f"Elapsed time: {timer.get_elapsed('seconds')} seconds")
```

Explore the documentation to learn more about advanced features.
