import polyline
import pandas as pd
import math

# Haversine formula to calculate the distance between two lat/lon points
def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # Radius of Earth in meters
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def decode_polyline_to_df(polyline_str):
    # Step 1: Decode the polyline string
    coords = polyline.decode(polyline_str)

    # Step 2: Create DataFrame with latitude, longitude
    df = pd.DataFrame(coords, columns=['latitude', 'longitude'])

    # Step 3: Calculate distances between successive points
    distances = [0]  # First row distance is 0
    for i in range(1, len(coords)):
        lat1, lon1 = coords[i - 1]
        lat2, lon2 = coords[i]
        distance = haversine(lat1, lon1, lat2, lon2)
        distances.append(distance)
    
    # Add distances to DataFrame
    df['distance'] = distances

    return df
