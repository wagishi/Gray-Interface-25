## Task 1

* **File** `Task_1.py`: Contains four core functions to compute Euclidean distance, Manhattan distance, Cosine distance, and the angle between vectors.
  
**What was done**:
Implemented the following functions:

* `euclidean_distance(v1, v2)`: Computes the Euclidean (L2) distance between two vectors.
* `manhattan_distance(v1, v2)`: Computes the Manhattan (L1) distance.
* `cosine_distance(v1, v2)`: Computes the cosine distance (1 - cosine similarity).
* `angle_between_vectors(v1, v2)`: Computes the angle (in degrees) between two vectors.

**How it was done**:

* Used `numpy` for efficient array manipulation and computation.
* Use `numpy` functions for mathematical calculation instead of loops, because they are much faster than loops.
* Used `np.linalg.norm` for calculating vector magnitudes.
* Included edge case handling for zero vectors in cosine and angle calculations to avoid division by zero errors.
