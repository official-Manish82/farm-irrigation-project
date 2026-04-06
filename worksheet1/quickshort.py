import time
import random
import matplotlib.pyplot as plt

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# ---------------- PART 1 ----------------
# Before & After Sorting (single n)

n = 20
elements = random.sample(range(1, 100), n)
original_list = list(elements)

print("Before Sorting:", original_list)

start_time = time.time()
quick_sort(elements, 0, n - 1)
end_time = time.time()

print("After Sorting :", elements)
print(f"Time taken for {n} elements: {end_time - start_time:.6f} seconds")

# ---------------- PART 2 ----------------
# Time vs n (Graph)

n_values = [50, 100, 200, 500, 1000]
time_taken = []

for n in n_values:
    arr = random.sample(range(1, 10000), n)
    start = time.time()
    quick_sort(arr, 0, n - 1)
    end = time.time()
    time_taken.append(end - start)
    print(f"n = {n}, Time taken = {end - start:.6f} seconds")

plt.plot(n_values, time_taken, marker='o')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Quick Sort Time Complexity Analysis")
plt.grid(True)
plt.show()
