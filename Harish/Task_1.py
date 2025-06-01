import math
import numpy as np

def euclidean_distance(v1,v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    distance = np.linalg.norm(v1-v2)
    return (distance)

def manhattan_distance(v1,v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    distance = np.sum(np.abs(v1-v2))
    return (distance)

def cosine_distance(v1,v2):
    dot_product = np.dot(v1,v2)
    mag_v1 = np.linalg.norm(v1)
    mag_v2 = np.linalg.norm(v2)
    if mag_v1 == 0  or mag_v2 == 0:
        return "Undefined"
    else:
        cosine = dot_product/(mag_v1*mag_v2)
    return (1 - cosine)

def angle_between_vectors(v1,v2):
    dot_product = np.dot(v1,v2)
    mag_v1 = np.linalg.norm(v1)
    mag_v2 = np.linalg.norm(v2)
    if mag_v1 == 0  or mag_v2 == 0:
        return "Undefined"
    else:
        cosine = dot_product/(mag_v1*mag_v2)
    angle = math.degrees(math.acos(cosine))
    return (angle)


