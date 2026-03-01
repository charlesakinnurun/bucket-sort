import math

def bucket_sort(arr, bucket_size=5):
    """
    Bucket Sort is a distribution sort that works by partitioning an array 
    into a number of buckets. Each bucket is then sorted individually.
    
    Visualization of the process:
    [Elements] -> [Hash Function] -> [Bucket 0, Bucket 1, ...] -> [Sort Buckets] -> [Concatenate]
    """
    
    # Check if the input array is empty; if so, return it immediately
    if len(arr) == 0:
        return arr

    # Step 1: Find the minimum and maximum values to determine the range
    # This range helps us distribute elements evenly across buckets
    min_value = min(arr)
    max_value = max(arr)

    # Step 2: Calculate the number of buckets needed
    # (max - min) / bucket_size gives us the spread, +1 ensures we cover the upper bound
    bucket_count = math.floor((max_value - min_value) / bucket_size) + 1
    
    # Initialize the buckets as a list of empty lists
    buckets = [[] for _ in range(bucket_count)]

    print(f"--- Initialization ---")
    print(f"Input Array: {arr}")
    print(f"Min: {min_value}, Max: {max_value}")
    print(f"Creating {bucket_count} buckets with a range/size of {bucket_size} each.\n")

    # Step 3: Distribute input array elements into buckets
    # We use the formula: index = floor((value - min) / size)
    for i in range(len(arr)):
        bucket_index = math.floor((arr[i] - min_value) / bucket_size)
        buckets[bucket_index].append(arr[i])
        print(f"Distributing {arr[i]}: Placed in Bucket {bucket_index}")

    # Step 4: Visualize the buckets before they are sorted
    print("\n--- Current Buckets (Unsorted) ---")
    for idx, b in enumerate(buckets):
        # Using '|' to represent the bucket container visually
        print(f"Bucket {idx}: | {' , '.join(map(str, b)) if b else 'empty'} |")

    # Step 5: Sort individual buckets and concatenate them
    sorted_array = []
    print("\n--- Sorting and Merging ---")
    for i in range(len(buckets)):
        # We use Python's built-in sorted() which is Timsort (O(n log n))
        # In a strict Bucket Sort, you could use Insertion Sort here
        buckets[i].sort()
        
        print(f"Sorting Bucket {i}: {buckets[i]}")
        
        # Add the elements of the sorted bucket to the final result
        for value in buckets[i]:
            sorted_array.append(value)

    return sorted_array

def run_demonstration():
    """
    Runs the Bucket Sort on different types of datasets to show versatility.
    """
    
    # Example 1: Standard positive integers
    print("========================================")
    print("EXAMPLE 1: Standard Integers")
    data1 = [22, 45, 12, 8, 10, 6, 72, 81, 33, 18, 50, 14]
    result1 = bucket_sort(data1, bucket_size=10)
    print(f"\nFinal Sorted Result: {result1}")
    print("========================================\n")

    # Example 2: Floating point numbers (0.0 to 1.0)
    # Often, bucket sort is explained using decimals where index = value * n
    print("========================================")
    print("EXAMPLE 2: Floating Point Numbers")
    data2 = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    # Small bucket_size for decimals to see more buckets
    result2 = bucket_sort(data2, bucket_size=0.2)
    print(f"\nFinal Sorted Result: {result2}")
    print("========================================\n")

if __name__ == "__main__":
    # Start the program
    run_demonstration()