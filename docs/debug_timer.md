# DebuggingChronosTimer

The `DebuggingChronosTimer` allows pausing and resuming timers during debugging sessions.

## Example

```python
from chronos import DebuggingChronosTimer

with DebuggingChronosTimer("Debug Task") as timer:
    input("Press Ctrl+Z to pause, and again to resume. Press Enter to finish.")
```
