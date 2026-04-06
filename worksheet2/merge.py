import time
import random
import matplotlib.pyplot as plt


# -------- MERGE SORT FUNCTIONS --------

def merge(arr, left, mid, right):
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


# ---------------- PART 1 ----------------
# Single n (Before & After Sorting)

n = 20
elements = random.sample(range(1, 100), n)
original_list = list(elements)

print("Before Sorting:", original_list)

start_time = time.time()
merge_sort(elements, 0, n - 1)
end_time = time.time()

print("After Sorting :", elements)
print(f"Time taken for {n} elements: {end_time - start_time:.6f} seconds")


# ---------------- PART 2 ----------------
# Multiple n (Time vs n Graph)

n_values = [50, 100, 200, 500, 1000]
time_taken = []

for n in n_values:
    arr = random.sample(range(1, 10000), n)
    start = time.time()
    merge_sort(arr, 0, n - 1)
    end = time.time()

    time_taken.append(end - start)
    print(f"n = {n}, Time taken = {end - start:.6f} seconds")


plt.plot(n_values, time_taken, marker='o')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Merge Sort Time Complexity Analysis")
plt.grid(True)
plt.show()
