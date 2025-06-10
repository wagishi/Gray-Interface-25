import numpy as np
def euclidean_distance(vec1,vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    total = 0
    for i in range(len(vec1)):
        diff = (vec1[i]-vec2[i])**2
        total+=diff
    euclidean_distance = np.sqrt(total)
    return euclidean_distance

def Manhattan_distance(vec1,vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    manhattan_distance=0
    for i in range(len(vec1)):
        diff = np.abs(vec1[i]-vec2[i])
        manhattan_distance +=diff
    return manhattan_distance

def magnitude(vec):
    vec = np.array(vec)
    total = 0
    for i in range(len(vec)):
        square = vec[i]**2
        total +=square
    return np.sqrt(total)
        

def cosine_distance(vec1,vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    cosine_distance = 1- np.dot(vec1,vec2)/(magnitude(vec1)*magnitude(vec2))
    return cosine_distance

def angle_between_vectors(vec1,vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    theta = np.arccos(np.dot(vec1,vec2)/(magnitude(vec1)*magnitude(vec2)))
    theta_in_degrees = np.degrees(theta)
    return theta_in_degrees
    
vec1 = list(map(float, input("Enter vector 1 : ").split()))
vec2 = list(map(float, input("Enter vector 2 : ").split()))

if len(vec1) != len(vec2):
    print("Error: Vectors must be of same length.")
else:
    print("Results:")
    print("Euclidean Distance:", euclidean_distance(vec1, vec2))
    print("Manhattan Distance:", Manhattan_distance(vec1, vec2))
    print("Cosine Distance:", cosine_distance(vec1, vec2))
    print("Angle Between Vectors (degrees):", angle_between_vectors(vec1, vec2))