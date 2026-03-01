<h1 align="center">Bucket Sort</h1>

## Overview

**Bucket Sort** is a distribution-based sorting algorithm that works by:

1. Dividing elements into several groups called **buckets**
2. Sorting each bucket individually
3. Concatenating the buckets to form the final sorted list

It works best when input values are **uniformly distributed** over a known range.

It is known for being:

* ✅ Very fast for uniformly distributed data
* ✅ Can achieve near linear time
* ✅ Easy to parallelize
* ❌ Requires extra memory for buckets
* ❌ Performance depends on data distribution

<a href="/src/main.py">Check out for source code</a>

---

## ⚙️ How Bucket Sort Works

### Steps

1. Create empty buckets
2. Distribute elements into buckets based on value range
3. Sort each bucket (often using insertion sort)
4. Merge all buckets into one sorted array

---

### Example Walkthrough

Sort this list of numbers between 0 and 1:

```id="bk1"
[0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
```

#### Step 1 — Create buckets

Example: 5 buckets for range [0,1)

```
Bucket 0: [0.23, 0.25]
Bucket 1: [0.32]
Bucket 2: [0.42, 0.47]
Bucket 3: []
Bucket 4: [0.52, 0.51]
```

#### Step 2 — Sort each bucket

```
Bucket 0: [0.23, 0.25]
Bucket 1: [0.32]
Bucket 2: [0.42, 0.47]
Bucket 4: [0.51, 0.52]
```

#### Step 3 — Merge buckets

```id="bk2"
[0.23, 0.25, 0.32, 0.42, 0.47, 0.51, 0.52]
```

---

## ⏱️ Time & Space Complexity

| Case           | Complexity |
| -------------- | ---------- |
| Best / Average | O(n + k)   |
| Worst Case     | O(n²)      |

Where:

* `n` = number of elements
* `k` = number of buckets

**Space Complexity:** O(n + k)

Worst case happens when many elements fall into one bucket.

---

## 🧠 Python Implementation

```python id="bk3"
def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Create buckets
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Put elements into buckets
    for num in arr:
        index = int(num * bucket_count)
        buckets[index].append(num)

    # Sort each bucket and merge
    result = []
    for bucket in buckets:
        result.extend(sorted(bucket))

    return result


# Example usage
numbers = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
print(bucket_sort(numbers))
# Output: [0.23, 0.25, 0.32, 0.42, 0.47, 0.51, 0.52]
```

---

## 🧪 Example Runs

### Example 1

Input:

```id="bk4"
[0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21]
```

Output:

```id="bk5"
[0.17, 0.21, 0.26, 0.39, 0.72, 0.78, 0.94]
```

### Example 2 (Integers with scaling)

Input:

```id="bk6"
[29, 25, 3, 49, 9, 37, 21, 43]
```

After scaling to 0–1 range and sorting:

```id="bk7"
[3, 9, 21, 25, 29, 37, 43, 49]
```

---

## 👍 Advantages

* Extremely fast for uniformly distributed data
* Can reach near O(n) performance
* Works well with floating point numbers
* Easy to parallelize

---

## 👎 Disadvantages

* Requires extra memory
* Needs known data range
* Poor performance if data is unevenly distributed
* Implementation can be tricky for arbitrary ranges

---

## 📌 When to Use Bucket Sort

Use Bucket Sort when:

* Values are uniformly distributed
* Range of data is known
* Sorting floating-point numbers
* Parallel sorting is beneficial

Common uses include:

* Sorting probabilities
* Sorting normalized scientific data
* Sorting uniformly distributed measurements

---

## 🏁 Summary

Bucket Sort is a powerful distribution-based sorting algorithm that can achieve near-linear performance when data is evenly spread across a range. While not suitable for every dataset, it is extremely efficient in the right conditions.
