Vector Distance Calculator

This Python script calculates various distance metrics and the angle between two input vectors.
It uses NumPy for numerical computations and supports the following metrics:

1.Euclidean Distance

2.Manhattan Distance

3.Cosine Distance

4.Angle Between Vectors (in degrees)

🧮 Features

Handles vector inputs of any dimensionality (as long as both vectors are of equal length).

Implements custom functions for distance and angle calculations using basic NumPy operations.

Provides user-friendly input prompts.

📦 Requirements

Python 3.x
NumPy
Install NumPy (if not already installed):

bash
pip install numpy

🚀 How to Use

Run the script:

bash
python Task1.py

Enter the two vectors when prompted. Separate each component with a space:

Enter vector 1 : 1 2 3
Enter vector 2 : 4 5 6

Output:

Results:
Euclidean Distance: 5.196152422706632
Manhattan Distance: 9.0
Cosine Distance: 0.025368153802923787
Angle Between Vectors (degrees): 12.933154491899135

📄 Functions Explained

1.euclidean_distance(vec1, vec2): Calculates the L2 norm (straight-line distance).

2.Manhattan_distance(vec1, vec2): Computes the L1 norm (sum of absolute differences).

3.magnitude(vec): Helper function to compute the magnitude of a vector.

4.cosine_distance(vec1, vec2): Calculates 1 - cosine similarity.

5.angle_between_vectors(vec1, vec2): Returns the angle in degrees using the arccos of cosine similarity.

🛑 Error Handling

Ensures both vectors are of the same length before computation.

If they aren't, it outputs an error message and terminates further calculations.

📁 File Structure

Task1.py
README.md
