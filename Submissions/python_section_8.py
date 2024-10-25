import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Helper function to generate all time intervals for a given entry
def generate_time_intervals(row):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # Parse start and end day indices
    start_day_idx = days.index(row['startDay'])
    end_day_idx = days.index(row['endDay'])
    
    # Parse start and end times
    start_time = datetime.strptime(row['startTime'], '%H:%M:%S')
    end_time = datetime.strptime(row['endTime'], '%H:%M:%S')
    
    # Initialize intervals
    intervals = []
    
    current_day_idx = start_day_idx
    current_time = start_time
    
    # Iterate through days until we reach the end day
    while True:
        if current_day_idx == end_day_idx and current_time > end_time:
            break
        # Add interval tuple (day index, hour index)
        intervals.append((current_day_idx, current_time.hour))
        
        # Move to the next hour
        current_time += timedelta(hours=1)
        if current_time.hour == 0:
            current_day_idx = (current_day_idx + 1) % 7  # Move to next day

    return intervals

# Main function to check for completeness
def check_time_coverage(df):
    # Initialize an empty dictionary to store intervals for each (id, id_2) pair
    coverage = {}
    
    # Populate the dictionary with time intervals for each row in the DataFrame
    for _, row in df.iterrows():
        key = (row['id'], row['id_2'])
        intervals = generate_time_intervals(row)
        
        # Add intervals to coverage dictionary
        if key not in coverage:
            coverage[key] = set()
        coverage[key].update(intervals)
    
    # Define the complete set of all intervals for a full week
    full_week_intervals = {(day, hour) for day in range(7) for hour in range(24)}
    
    # Check each (id, id_2) pair for completeness
    result = {}
    for key, intervals in coverage.items():
        result[key] = intervals != full_week_intervals  # True if incomplete, False if complete
    
    # Convert result dictionary to a MultiIndex Series
    return pd.Series(result, name="incomplete").astype(bool)
