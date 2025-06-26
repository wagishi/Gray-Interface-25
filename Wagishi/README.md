## Task 1 – Vector Distance & Angle Computations
File: Task1.py

# Overview
This module implements Three core functions for measuring distances and angles between two numerical vectors:

euclidean_dist(a, b)
manhattan_dist(a, b)
cosine_dist_angle(a, b)

## Functions

# euclidean_dist(a, b)
   Compute the Euclidean (L2) distance between two numeric vectors.
   Formula
‖a − b‖₂ = √∑ᵢ (aᵢ − bᵢ)²

# manhattan_dist(a, b)
   Compute the Manhattan (L1) distance between two numeric vectors.
   Formula
‖a − b‖₁ = ∑ᵢ |aᵢ − bᵢ|

# cosine_dist_angle(a, b)
   Compute the Cosine distance (1 − cosine similarity) and the angle (in radians) between two numeric vectors.
   Formulas
Cosine similarity:
(a · b) / (‖a‖₂ · ‖b‖₂)
Cosine distance:
1 − cosine_similarity
Angle θ:
θ = arccos(cosine_similarity)
If either vector is zero (norm = 0), the function prints a warning and returns None.

