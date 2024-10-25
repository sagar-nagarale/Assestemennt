def group_by_length(strings):
    length_dict = {}
    for string in strings:
        length = len(string)
        # Add the string to the appropriate list in the dictionary
        if length not in length_dict:
            length_dict[length] = []
        length_dict[length].append(string)
    # Sort the dictionary by keys (lengths)
    return dict(sorted(length_dict.items()))
