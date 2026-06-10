import pandas as pd
import random

data = []

# O(1) examples
o1 = [
"""def get_first(arr):
    return arr[0]""",
"""def add(a, b):
    return a + b""",
"""def lookup(hashmap, key):
    return hashmap.get(key, -1)""",
"""def is_even(n):
    return n % 2 == 0""",
"""def swap(a, b):
    return b, a""",
"""def get_last(arr):
    return arr[-1]""",
"""def constant_loop():
    for i in range(100):
        print(i)""",
"""def check_empty(arr):
    return len(arr) == 0""",
"""def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    return c""",
"""def hash_insert(d, key, val):
    d[key] = val
    return d""",
"""def get_middle(arr):
    mid = len(arr) // 2
    return arr[mid]""",
"""def abs_val(n):
    return n if n >= 0 else -n""",
"""def power_of_two(n):
    return n & (n - 1) == 0""",
"""def celsius_to_fahrenheit(c):
    return c * 9/5 + 32""",
"""def count_digits(n):
    import math
    if n == 0:
        return 1
    return int(math.log10(abs(n))) + 1"""
]

# O(log n) examples
ologn = [
"""def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1""",
"""def find_sqrt(n):
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            left = mid + 1
        else:
            right = mid - 1
    return right""",
"""def power(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    return base * power(base, exp - 1)""",
"""def search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1""",
"""def first_bad_version(n, is_bad):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if is_bad(mid):
            right = mid
        else:
            left = mid + 1
    return left""",
"""def count_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count""",
"""def find_peak(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left""",
"""def lower_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo""",
"""def gcd(a, b):
    while b:
        a, b = b, a % b
    return a""",
"""def log_base2(n):
    result = 0
    while n > 1:
        n //= 2
        result += 1
    return result"""
]

# O(n) examples
on = [
"""def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1""",
"""def find_max(arr):
    max_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x
    return max_val""",
"""def reverse_array(arr):
    result = []
    for i in range(len(arr) - 1, -1, -1):
        result.append(arr[i])
    return result""",
"""def count_occurrences(arr, target):
    count = 0
    for x in arr:
        if x == target:
            count += 1
    return count""",
"""def two_sum(arr, target):
    seen = {}
    for i, x in enumerate(arr):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []""",
"""def prefix_sum(arr):
    result = [0] * len(arr)
    result[0] = arr[0]
    for i in range(1, len(arr)):
        result[i] = result[i-1] + arr[i]
    return result""",
"""def remove_duplicates(arr):
    seen = set()
    result = []
    for x in arr:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result""",
"""def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True""",
"""def longest_increasing_run(arr):
    max_run = 1
    cur = 1
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            cur += 1
            max_run = max(max_run, cur)
        else:
            cur = 1
    return max_run""",
"""def merge_sorted(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result""",
"""def kadane(arr):
    max_sum = cur = arr[0]
    for x in arr[1:]:
        cur = max(x, cur + x)
        max_sum = max(max_sum, cur)
    return max_sum""",
"""def count_vowels(s):
    count = 0
    for ch in s:
        if ch.lower() in 'aeiou':
            count += 1
    return count"""
]

# O(n log n) examples
onlogn = [
"""def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result""",
"""def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, l_inv = count_inversions(arr[:mid])
    right, r_inv = count_inversions(arr[mid:])
    merged = []
    inversions = l_inv + r_inv
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions""",
"""def sort_and_search(arr, targets):
    arr.sort()
    results = []
    for t in targets:
        left, right = 0, len(arr) - 1
        found = False
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == t:
                found = True; break
            elif arr[mid] < t:
                left = mid + 1
            else:
                right = mid - 1
        results.append(found)
    return results""",
"""def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)""",
"""def sort_and_remove_duplicates(arr):
    if not arr:
        return []
    arr.sort()
    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            result.append(arr[i])
    return result""",
"""def find_closest_pair(arr):
    arr.sort()
    min_diff = float('inf')
    for i in range(1, len(arr)):
        min_diff = min(min_diff, arr[i] - arr[i-1])
    return min_diff""",
"""def heap_sort(arr):
    import heapq
    heap = arr[:]
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(len(heap))]""",
"""def sort_by_frequency(arr):
    from collections import Counter
    freq = Counter(arr)
    return sorted(arr, key=lambda x: (-freq[x], x))""",
"""def kth_largest(arr, k):
    arr.sort(reverse=True)
    return arr[k-1]""",
"""def meeting_rooms(intervals):
    intervals.sort(key=lambda x: x[0])
    count = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            count += 1
    return count"""
]

# O(n^2) examples
on2 = [
"""def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr""",
"""def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr""",
"""def has_duplicate_pair(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False""",
"""def matrix_multiply(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C""",
"""def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]""",
"""def find_all_pairs(arr):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            pairs.append((arr[i], arr[j]))
    return pairs""",
"""def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr""",
"""def max_subarray_brute(arr):
    max_sum = float('-inf')
    for i in range(len(arr)):
        cur = 0
        for j in range(i, len(arr)):
            cur += arr[j]
            max_sum = max(max_sum, cur)
    return max_sum""",
"""def count_pairs_with_diff(arr, k):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs(arr[i] - arr[j]) == k:
                count += 1
    return count""",
"""def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix"""
]

# O(2^n) examples
o2n = [
"""def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)""",
"""def all_subsets(arr):
    if not arr:
        return [[]]
    rest = all_subsets(arr[1:])
    return rest + [[arr[0]] + s for s in rest]""",
"""def count_paths(grid, r, c):
    if r == 0 or c == 0:
        return 1
    return count_paths(grid, r-1, c) + count_paths(grid, r, c-1)""",
"""def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)""",
"""def generate_parentheses(n):
    result = []
    def backtrack(s, open, close):
        if len(s) == 2 * n:
            result.append(s)
            return
        if open < n:
            backtrack(s + '(', open+1, close)
        if close < open:
            backtrack(s + ')', open, close+1)
    backtrack('', 0, 0)
    return result""",
"""def subset_sum(arr, target, idx=0):
    if target == 0:
        return True
    if idx == len(arr) or target < 0:
        return False
    return (subset_sum(arr, target - arr[idx], idx+1) or
            subset_sum(arr, target, idx+1))""",
"""def permutations(arr):
    if len(arr) <= 1:
        return [arr]
    result = []
    for i, x in enumerate(arr):
        rest = arr[:i] + arr[i+1:]
        for p in permutations(rest):
            result.append([x] + p)
    return result""",
"""def word_break(s, words):
    if not s:
        return True
    for word in words:
        if s.startswith(word):
            if word_break(s[len(word):], words):
                return True
    return False""",
"""def count_binary_strings(n):
    if n == 0:
        return 1
    return count_binary_strings(n-1) + count_binary_strings(n-1)""",
"""def naive_tsp(dist, visited, cur, n, count, cost, ans):
    if count == n and dist[cur][0]:
        ans[0] = min(ans[0], cost + dist[cur][0])
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            naive_tsp(dist, visited, i, n, count+1, cost+dist[cur][i], ans)
            visited[i] = False"""
]

# Combine with labels
label_map = {"O(1)": 0, "O(log n)": 1, "O(n)": 2, "O(n log n)": 3, "O(n^2)": 4, "O(2^n)": 5}

for snippet in o1:
    data.append({"code": snippet.strip(), "label": 0, "complexity": "O(1)"})
for snippet in ologn:
    data.append({"code": snippet.strip(), "label": 1, "complexity": "O(log n)"})
for snippet in on:
    data.append({"code": snippet.strip(), "label": 2, "complexity": "O(n)"})
for snippet in onlogn:
    data.append({"code": snippet.strip(), "label": 3, "complexity": "O(n log n)"})
for snippet in on2:
    data.append({"code": snippet.strip(), "label": 4, "complexity": "O(n^2)"})
for snippet in o2n:
    data.append({"code": snippet.strip(), "label": 5, "complexity": "O(2^n)"})

df = pd.DataFrame(data)
df.to_csv("complexity_dataset.csv", index=False)

print(f"Total samples: {len(df)}")
print(df["complexity"].value_counts())
print("\nSample row:")
print(df.iloc[0]["code"])
print("Label:", df.iloc[0]["complexity"])
