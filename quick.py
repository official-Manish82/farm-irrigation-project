import time
def partition(arr, low, high):
  pivot = arr[high]
  i = low - 1
  for j in range(low, high):
    if arr[j] <= pivot:
      i =i + 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1
def quick_sort(arr, low, high):
  if low < high:
    pi = partition(arr, low, high)
    quick_sort(arr, low, pi - 1)
    quick_sort(arr, pi + 1, high)

elements = [10,7,8,9,5,2,6,3,4,90,11,23,55,44,12,34,1,21]
n = len(elements)
original_list =list(elements)
start_time = time.time()
quick_sort(elements, 0, n - 1)
end_time = time.time()
time_required = end_time - start_time

print("Original list:", original_list)
print("Sorted list:", elements)
print(f"Time taken to sort the list: {time_required:.6f} seconds")