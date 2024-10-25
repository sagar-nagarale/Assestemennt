import re

def find_all_dates(text):
    # Regular expression pattern to match dates in "dd-mm-yyyy", "mm/dd/yyyy", "yyyy.mm.dd"
    date_pattern = r'\b(?:\d{2}-\d{2}-\d{4}|\d{2}/\d{2}/\d{4}|\d{4}\.\d{2}\.\d{2})\b'
    
    # Find all matches of the pattern in the text
    dates = re.findall(date_pattern, text)
    
    return dates
