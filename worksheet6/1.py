def display_subset(subset):
    print(*subset)

def subset_sum(arr, subset, index, current_sum, target):
   
    if current_sum == target:
        display_subset(subset)
        return

   
    if current_sum > target:
        return

    for i in range(index, len(arr)):
        
        subset.append(arr[i])

        subset_sum(arr, subset, i + 1, current_sum + arr[i], target)

        
        subset.pop()

def find_subset(arr, target):
    subset = []
    subset_sum(arr, subset, 0, 0, target)

# Input
weights = [10, 7, 5, 18, 12, 20, 15]
target = 35

# Call function
find_subset(weights, target)