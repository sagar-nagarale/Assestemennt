def reverse_by_n(lst, n):
    result = []
    for i in range(0, len(lst), n):
        # Temporary list to store the current group
        group = []
        # Reverse the group manually
        for j in range(i, min(i + n, len(lst))):
            group.insert(0, lst[j])
        # Add the reversed group to the result list
        result.extend(group)
    return result
