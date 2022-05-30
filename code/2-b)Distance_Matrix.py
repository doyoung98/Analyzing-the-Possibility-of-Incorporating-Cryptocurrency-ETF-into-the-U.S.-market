
def Translate_To_Distance_Matrix(dataset):
    distance_matrix = ((1 - dataset) / 2.) ** 0.5
    return distance_matrix