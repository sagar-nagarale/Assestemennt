import pandas as pd
import numpy as np
from datetime import time, timedelta

def calculate_time_based_toll_rates(toll_rate_df):
    # Step 1: Add start_day, start_time, end_day, and end_time columns
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Generating dummy day and time data for the example. In practice, you'd get these from your input DataFrame.
    # Assuming each id_start, id_end pair will have a full week's worth of data.
    toll_rate_df['start_day'] = np.random.choice(days, size=len(toll_rate_df))
    toll_rate_df['end_day'] = np.random.choice(days, size=len(toll_rate_df))
    
    # Assigning random time values. In practice, you may have specific times to assign.
    toll_rate_df['start_time'] = [time(hour=np.random.randint(0, 24), minute=np.random.randint(0, 60)) for _ in range(len(toll_rate_df))]
    toll_rate_df['end_time'] = [time(hour=np.random.randint(0, 24), minute=np.random.randint(0, 60)) for _ in range(len(toll_rate_df))]
    
    # Step 2: Define discount factors
    def apply_discount(row):
        if row['start_day'] in ['Saturday', 'Sunday']:  # Weekend discount
            discount_factor = 0.7
        else:  # Weekday discounts
            if row['start_time'] < time(10, 0, 0):  # 00:00 to 10:00
                discount_factor = 0.8
            elif row['start_time'] < time(18, 0, 0):  # 10:00 to 18:00
                discount_factor = 1.2
            else:  # 18:00 to 23:59
                discount_factor = 0.8
        
        # Apply discount to each vehicle type
        for vehicle_type in ['moto', 'car', 'rv', 'bus', 'truck']:
            row[vehicle_type] *= discount_factor
        
        return row

    # Step 3: Apply discount to each row
    toll_rate_df = toll_rate_df.apply(apply_discount, axis=1)

    return toll_rate_df

# Example Usage
time_based_toll_rates_df = calculate_time_based_toll_rates(toll_rate_df)

# Display the resulting DataFrame with time-based toll rates
print(time_based_toll_rates_df)
