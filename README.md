
# SSD Flash Memory Simulator

A beginner-level Python project that simulates basic SSD memory block allocation, write limits, faulty block handling, and write distribution.

## Project Overview

Solid-State Drives (SSDs) use flash memory to store data. This project models a simplified version of memory block allocation to demonstrate basic storage-system concepts.

This is an educational simulation and does not interact with physical SSD hardware.

## Features

- Simulates multiple memory blocks.
- Allocates writes to the available block with the fewest writes.
- Tracks write counts for each block.
- Enforces a configurable write limit.
- Allows blocks to be marked as faulty.
- Handles unavailable blocks and invalid block IDs.
- Includes automated unit tests using Python's `unittest`.

## Technologies Used

- Python
- unittest

## Project Structure

```text
ssd-flash-memory-simulator/
├── ssd_simulator.py
├── test_ssd_simulator.py
└── README.md
```

## Requirements

- Python 3.x
- No external packages required

## How to Run

Run the simulator:

```bash
python ssd_simulator.py
```

Run the unit tests:

```bash
python -m unittest test_ssd_simulator.py -v
```

## Testing

The test suite checks:

1. Successful write operations
2. Distribution of writes across blocks
3. Skipping faulty blocks
4. Handling unavailable memory blocks
5. Handling invalid block IDs
6. Enforcing write limits

The tests were run in Google Colab, and all six passed.

## Limitations

This project is a simplified educational model. It does not implement physical NAND Flash operations, erase cycles, garbage collection, error-correcting codes, or production SSD firmware.

## Future Improvements

- Simulate erase operations and erase-cycle counts.
- Compare different block-allocation strategies.
- Add more automated tests and performance measurements.
- Explore more advanced wear-leveling approaches.

## Author

Dipti Wagh

