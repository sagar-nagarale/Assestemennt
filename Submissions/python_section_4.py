def unique_permutations(nums):
    def backtrack(start):
        # Base case: if the start index reaches the end, we have a unique permutation
        if start == len(nums):
            results.append(nums[:])
            return
        seen = set()  # Track elements used at this position to avoid duplicates
        for i in range(start, len(nums)):
            if nums[i] in seen:
                continue
            seen.add(nums[i])
            nums[start], nums[i] = nums[i], nums[start]  # Swap elements
            backtrack(start + 1)  # Recurse with next position fixed
            nums[start], nums[i] = nums[i], nums[start]  # Backtrack

    results = []
    nums.sort()  # Sort to handle duplicates by ensuring they are consecutive
    backtrack(0)
    return results
