# 🏴‍☠️ Treasure Quest: The Straw Hat Crew!
This project simulates a scheduling system where the Straw Hat Pirates manage an ever-growing pile of treasure. Implemented as part of COL106 Assignment 3, the system uses heap-based priority scheduling to assign treasures to crewmates and track their processing.

## ⚓ Problem Overview
Each treasure arrives at a specific time, has a size (i.e., processing time), and is uniquely identified. The goal is to:
- Assign each treasure to the crewmate with the least total workload.
- At each time step, crewmates pick the treasure from their queue with the highest priority, calculated as:
> Priority = Wait Time - Remaining Size
In case of ties, treasures with lower IDs are preferred.
## 🧠 Key Features
- Dynamic Heap: A custom heap implementation to manage crewmates' treasure queues.
- Load Balancing: New treasures are always assigned to the least-loaded crewmate.
- Accurate Simulation: Tracks treasure processing over time and computes final completion times.
- Time-Efficient: Implements all core operations in O(log n + log m) or better.
## 🧱 Project Structure
> crewmate.py       # Defines the Crewmate class and load-tracking logic
> 
> custom.py         # Utility functions and extra classes
> 
> heap.py           # Array-based min-heap implementation
> 
> straw hat.py      # Core class: StrawHatTreasury for treasure scheduling
> 
> treasure.py       # Treasure class and metadata

## 📌 Constraints & Notes
- No use of dict, set, or hash-based structures.
- Only built-in sort() is allowed (and only in get_completion_time()).
- Heap operations must follow expected complexity constraints.
- Arrival times are strictly increasing.
