def flatten_dict(d, parent_key=''):
    items = []
    for key, value in d.items():
        # Concatenate parent key and current key with a dot separator
        new_key = f"{parent_key}.{key}" if parent_key else key

        if isinstance(value, dict):
            # Recursive call for nested dictionary
            items.extend(flatten_dict(value, new_key).items())
        elif isinstance(value, list):
            # Handle lists by iterating over each item with its index
            for i, item in enumerate(value):
                list_key = f"{new_key}[{i}]"
                if isinstance(item, dict):
                    items.extend(flatten_dict(item, list_key).items())
                else:
                    items.append((list_key, item))
        else:
            # Add non-dictionary, non-list items to the flattened dictionary
            items.append((new_key, value))
    
    return dict(items)
