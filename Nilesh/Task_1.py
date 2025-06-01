import numpy as np

def euc_dist(v1:np.array, v2:np.array):
    return np.linalg.norm(v1 - v2)
    
def man_dist(v1:np.array, v2:np.array):
    return np.linalg.norm(v1 - v2, ord=1)
    
def cos_dist(v1:np.array, v2:np.array):
    return 1 - np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))

def angle(v1:np.array, v2:np.array):
    return np.degrees(np.arccos(np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))))

v1 = np.array(list(map(float,input("Enter Vector : ").split())))
v2 = np.array(list(map(float,input("Enter Vector : ").split())))
print(f"Euclidean Distance : {euc_dist(v1,v2)}")
print(f"Manhattan Distance : {man_dist(v1,v2)}")
print(f"Cosine Distance : {cos_dist(v1,v2)}")
print(f"Angle Between Vectors : {angle(v1,v2)} degrees")