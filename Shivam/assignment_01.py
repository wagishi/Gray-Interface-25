import numpy as np
#  To calculate euclidean distance
def euclidean_distance(vector1,vector2):
    distance=0
    for i in range(len(vector1)):
        distance += (vector1[i]-vector2[i])**2
    
    euclidean_dist = np.sqrt(distance)
    print("Euclidean distance between", vector1, "and", vector2, "is:", euclidean_dist)

# To calculate manhattan distance
def manhattan_distance(vector1,vector2):
    distance=0

    for i in range(len(vector1)):
        distance += abs(vector1[i]-vector2[i])

    manhattan_distance=distance
    print("Manhattan distance between", vector1, "and", vector2, "is:", manhattan_distance)

# To calulate angle between two vectors  
def angle_between_vectors(vector1,vector2):
    dot_product = np.dot(vector1, vector2)
    magnitude1 = 0
    magnitude2 = 0
    for i in range(len(vector1)):
        magnitude1 += vector1[i] ** 2
        magnitude2 += vector2[i] ** 2
    magnitude1 = np.sqrt(magnitude1)
    magnitude2 = np.sqrt(magnitude2)

    if magnitude1 == 0 or magnitude2 == 0:
        print("One of the vectors is zero, angle is undefined.")
        return

    cos_theta = dot_product / (magnitude1 * magnitude2)# also called as cosine similarity
    angle_rad = np.arccos(cos_theta)
    angle_deg = np.degrees(angle_rad)

    print("Angle between", vector1, "and", vector2, "is:", angle_deg, "degrees")  


# to calculate cosine distance
def cosine_distance(vector1, vector2):
    dot_product = np.dot(vector1, vector2)
    magnitude1 = 0
    magnitude2 = 0
    for i in range(len(vector1)):
        magnitude1 += vector1[i] ** 2
        magnitude2 += vector2[i] ** 2
    magnitude1 = np.sqrt(magnitude1)
    magnitude2 = np.sqrt(magnitude2)
    if magnitude1 == 0 or magnitude2 == 0:
        print("One of the vectors is zero, cosine distance is undefined.")
        return

    cosine_similarity = dot_product / (magnitude1 * magnitude2)
    cosine_distance = 1 - cosine_similarity

    print("Cosine distance between", vector1, "and", vector2, "is:", cosine_distance)


#for euclidean distance
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
euclidean_distance(vector1, vector2)
#for manhattan distance
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
manhattan_distance(vector1, vector2)
#for angle between vectors
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
angle_between_vectors(vector1, vector2)
#for cosine distance
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
cosine_distance(vector1, vector2)


