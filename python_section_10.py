import pandas as pd

def unroll_distance_matrix(distance_matrix):
    # Step 1: Create an empty list to store the unrolled data
    unrolled_data = []

    # Step 2: Iterate through the distance matrix
    for id_start in distance_matrix.index:
        for id_end in distance_matrix.columns:
            # Exclude self-connections
            if id_start != id_end:
                distance = distance_matrix.loc[id_start, id_end]
                unrolled_data.append({'id_start': id_start, 'id_end': id_end, 'distance': distance})

    # Step 3: Create a DataFrame from the unrolled data
    unrolled_df = pd.DataFrame(unrolled_data)

    return unrolled_df

# Assuming distance_matrix_df is the DataFrame created in the previous step
unrolled_distance_df = unroll_distance_matrix(distance_matrix_df)

# Display the unrolled DataFrame
print(unrolled_distance_df)
