import pandas as pd
import numpy as np

def find_ids_within_ten_percentage_threshold(unrolled_df, reference_id):
    # Step 1: Calculate the average distance for the reference_id
    average_distance = unrolled_df.loc[unrolled_df['id_start'] == reference_id, 'distance'].mean()
    
    if np.isnan(average_distance):  # Handle case where there are no distances for the reference_id
        return []

    # Step 2: Calculate the lower and upper bounds for the 10% threshold
    lower_bound = average_distance * 0.9
    upper_bound = average_distance * 1.1

    # Step 3: Find all id_start values within the threshold
    filtered_ids = unrolled_df[
        (unrolled_df['distance'] >= lower_bound) & 
        (unrolled_df['distance'] <= upper_bound)
    ]['id_start'].unique()  # Get unique ids

    # Step 4: Sort the result
    sorted_ids = sorted(filtered_ids)

    return sorted_ids

# Example Usage
reference_id = 1001400  # Replace with the desired reference ID
resulting_ids = find_ids_within_ten_percentage_threshold(unrolled_distance_df, reference_id)

# Display the resulting IDs
print(resulting_ids)
