import pandas as pd

def calculate_toll_rate(unrolled_df):
    # Step 1: Define the rate coefficients for each vehicle type
    rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }
    
    # Step 2: Calculate toll rates for each vehicle type
    for vehicle_type, coefficient in rate_coefficients.items():
        unrolled_df[vehicle_type] = unrolled_df['distance'] * coefficient

    return unrolled_df

# Example Usage
toll_rate_df = calculate_toll_rate(unrolled_distance_df)

# Display the resulting DataFrame with toll rates
print(toll_rate_df)
