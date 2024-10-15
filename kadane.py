def kadane(arr):
    # Initialize current sum and max sum
    max_current = arr[0]
    max_global = arr[0]

    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Update the current max sum (either extend the previous subarray or start a new one)
        max_current = max(arr[i], max_current + arr[i])

        # Update the global max sum if the current max sum is greater
        if max_current > max_global:
            max_global = max_current

    return max_global

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = kadane(arr)
print(f"The maximum sum of a contiguous subarray is: {max_sum}")
