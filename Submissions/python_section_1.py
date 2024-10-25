import pandas as pd
import re
from itertools import permutations
from datetime import datetime, timedelta
from math import radians, cos, sin, asin, sqrt

# Question 1: Reverse List by N Elements
def reverse_list_by_n(lst, n):
    result = []
    for i in range(0, len(lst), n):
        sublist = lst[i:i + n]
        for item in reversed(sublist):
            result.append(item)
    return result

# Question 2: Lists & Dictionaries
def group_strings_by_length(strings):
    length_dict = {}
    for string in strings:
        length = len(string)
        if length not in length_dict:
            length_dict[length] = []
        length_dict[length].append(string)
    return dict(sorted(length_dict.items()))

# Question 3: Flatten a Nested Dictionary
def flatten_dictionary(nested_dict):
    flat_dict = {}

    def flatten_helper(d, parent_key=''):
        for k, v in d.items():
            new_key = f"{parent_key}.{k}" if parent_key else k
            if isinstance(v, dict):
                flatten_helper(v, new_key)
            elif isinstance(v, list):
                for i, item in enumerate(v):
                    flatten_helper({f"{new_key}[{i}]": item})
            else:
                flat_dict[new_key] = v

    flatten_helper(nested_dict)
    return flat_dict

# Question 4: Generate Unique Permutations
def unique_permutations(lst):
    return list(map(list, set(permutations(lst))))

# Question 5: Find All Dates in a Text
def find_all_dates(text):
    date_patterns = [
        r'\d{2}-\d{2}-\d{4}',  # dd-mm-yyyy
        r'\d{2}/\d{2}/\d{4}',  # mm/dd/yyyy
        r'\d{4}\.\d{2}\.\d{2}'  # yyyy.mm.dd
    ]
    dates = []
    for pattern in date_patterns:
        dates.extend(re.findall(pattern, text))
    return dates

# Question 6: Decode Polyline, Convert to DataFrame with Distances
def decode_polyline(polyline):
    # This function assumes you have the necessary logic to decode the polyline
    # Add your decoding logic here or use an appropriate library
    coordinates = []  # Replace with the actual decoding logic
    # Assuming coordinates are [(lat1, lon1), (lat2, lon2), ...]
    
    distance_list = []
    for i in range(1, len(coordinates)):
        lat1, lon1 = radians(coordinates[i-1][0]), radians(coordinates[i-1][1])
        lat2, lon2 = radians(coordinates[i][0]), radians(coordinates[i][1])
        
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        r = 6371000  # Radius of Earth in meters
        distance = r * c
        distance_list.append(distance)
    
    df = pd.DataFrame(coordinates, columns=['latitude', 'longitude'])
    df['distance'] = [0] + distance_list
    return df

# Question 7: Matrix Rotation and Transformation
def rotate_and_transform_matrix(matrix):
    n = len(matrix)
    
    # Rotate the matrix 90 degrees clockwise
    rotated = [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]
    
    # Transform the matrix by summing row and column excluding itself
    transformed = []
    for i in range(n):
        row_sum = sum(rotated[i])
        for j in range(n):
            col_sum = sum(rotated[k][j] for k in range(n))
            transformed.append(row_sum + col_sum - rotated[i][j])
    
    return [transformed[i * n:(i + 1) * n] for i in range(n)]

# Question 8: Time Check
def check_time_data(df):
    df['start'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
    df['end'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])
    
    grouped = df.groupby(['id', 'id_2'])
    result = pd.Series(index=grouped.groups.keys())
    
    for key, group in grouped:
        full_day = pd.date_range(start=group['start'].min().normalize(), end=group['end'].max().normalize(), freq='D')
        weekdays = group['start'].dt.day_name().unique()
        result[key] = (len(full_day) == 7) and (len(weekdays) == 7)
    
    return result

