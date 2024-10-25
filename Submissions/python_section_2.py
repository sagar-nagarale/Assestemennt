import pandas as pd
import numpy as np
import itertools
from datetime import time

# Question 9: Distance Matrix Calculation
def calculate_distance_matrix(df):
    locations = df['id'].unique()
    distance_matrix = pd.DataFrame(np.inf, index=locations, columns=locations)

    for _, row in df.iterrows():
        distance_matrix.at[row['id'], row['id_2']] = row['distance']
    
    # Fill diagonal with 0s
    np.fill_diagonal(distance_matrix.values, 0)

    # Calculate cumulative distances using Floyd-Warshall algorithm
    for k in locations:
        for i in locations:
            for j in locations:
                if distance_matrix.at[i, j] > distance_matrix.at[i, k] + distance_matrix.at[k, j]:
                    distance_matrix.at[i, j] = distance_matrix.at[i, k] + distance_matrix.at[k, j]

    return distance_matrix

# Question 10: Unroll Distance Matrix
def unroll_distance_matrix(distance_matrix):
    unrolled = []
    for id_start in distance_matrix.index:
        for id_end in distance_matrix.columns:
            if id_start != id_end:
                unrolled.append({'id_start': id_start, 'id_end': id_end, 'distance': distance_matrix.at[id_start, id_end]})
    return pd.DataFrame(unrolled)

# Question 11: Finding IDs within Percentage Threshold
def find_ids_within_ten_percentage_threshold(unrolled_df, reference_id):
    avg_distance = unrolled_df[unrolled_df['id_start'] == reference_id]['distance'].mean()
    lower_bound = avg_distance * 0.9
    upper_bound = avg_distance * 1.1
    result = unrolled_df[(unrolled_df['distance'] >= lower_bound) & (unrolled_df['distance'] <= upper_bound)]
    return sorted(result['id_start'].unique())

# Question 12: Calculate Toll Rate
def calculate_toll_rate(unrolled_df):
    toll_rates = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }
    
    for vehicle, rate in toll_rates.items():
        unrolled_df[vehicle] = unrolled_df['distance'] * rate
    
    return unrolled_df

# Question 13: Calculate Time-Based Toll Rates
def calculate_time_based_toll_rates(toll_df):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    new_rows = []

    for _, row in toll_df.iterrows():
        for day in days_of_week:
            for hour in range(24):
                start_time = time(hour, 0)
                end_time = time(hour, 59, 59)
                discount_factor = 1

                if day in days_of_week[:5]:  # Weekdays
                    if hour < 10:
                        discount_factor = 0.8
                    elif hour < 18:
                        discount_factor = 1.2
                    else:
                        discount_factor = 0.8
                else:  # Weekends
                    discount_factor = 0.7

                # Create a new row for the time interval
                new_row = row.copy()
                new_row['start_day'] = day
                new_row['end_day'] = day
                new_row['start_time'] = start_time
                new_row['end_time'] = end_time

                # Adjust toll rates according to discount
                for vehicle in ['moto', 'car', 'rv', 'bus', 'truck']:
                    new_row[vehicle] *= discount_factor
                
                new_rows.append(new_row)

    return pd.DataFrame(new_rows)
