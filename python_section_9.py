import pandas as pd
import numpy as np

def calculate_distance_matrix(file_path):
    # Step 1: Load the dataset
    df = pd.read_csv(file_path)
    
    # Step 2: Extract unique IDs and initialize the distance matrix
    unique_ids = pd.concat([df['id_start'], df['id_end']]).unique()
    distance_matrix = pd.DataFrame(index=unique_ids, columns=unique_ids, data=np.inf)
    
    # Step 3: Fill the matrix with known distances
    for _, row in df.iterrows():
        id_a = row['id_start']
        id_b = row['id_end']
        distance = row['distance']
        
        # Update distance in both directions
        distance_matrix.loc[id_a, id_b] = distance
        distance_matrix.loc[id_b, id_a] = distance  # Ensure symmetry

    # Set the diagonal values to 0 (distance from a location to itself)
    np.fill_diagonal(distance_matrix.values, 0)

    # Step 4: Calculate cumulative distances using Floyd-Warshall algorithm
    for k in unique_ids:
        for i in unique_ids:
            for j in unique_ids:
                # If the path through k is shorter, update the distance
                if distance_matrix.loc[i, k] + distance_matrix.loc[k, j] < distance_matrix.loc[i, j]:
                    distance_matrix.loc[i, j] = distance_matrix.loc[i, k] + distance_matrix.loc[k, j]

    return distance_matrix

# Specify the path to your dataset
file_path = '/content/sample_data/dataset-2.csv'  # Adjust the path as necessary

# Calculate the distance matrix
distance_matrix_df = calculate_distance_matrix(file_path)

# Print the resulting distance matrix
print(distance_matrix_df)
