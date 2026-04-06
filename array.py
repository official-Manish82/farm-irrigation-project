import random
import time
from typing import List, Optional


def create_array(values: Optional[List[int]] = None, n: int = 0, randomize: bool = False) -> List[int]:
	
	if values is not None:
		return list(values)
	if randomize:
		return [random.randint(0, 9999) for _ in range(n)]
	return [0] * n


def display(arr: List[int]) -> None:
	"""Print array elements on one line."""
	print('Array:', arr)


def insert_at(arr: List[int], index: int, value: int) -> None:
	"""Insert value at index (0-based). If index > len(arr), append."""
	if index < 0:
		raise IndexError('Negative index not supported')
	if index >= len(arr):
		arr.append(value)
	else:
		arr.insert(index, value)


def delete_at(arr: List[int], index: int) -> int:
	"""Delete element at index and return it."""
	if index < 0 or index >= len(arr):
		raise IndexError('Index out of range')
	return arr.pop(index)


def search_value(arr: List[int], value: int) -> int:
	"""Return index of first occurrence or -1 if not found."""
	try:
		return arr.index(value)
	except ValueError:
		return -1


def sort_array(arr: List[int], in_place: bool = True) -> List[int]:
	"""Sort the array. By default sorts in place and returns the array.
	Also returns a new sorted list if in_place is False.
	"""
	if in_place:
		arr.sort()
		return arr
	else:
		return sorted(arr)


def reverse_array(arr: List[int]) -> None:
	"""Reverse the array in place."""
	arr.reverse()


def demo_sequence():
	"""Run a demo showing the operations and timings."""
	print('--- Array operations demo ---')

	a = create_array(n=10, randomize=True)
	display(a)

	print('\nInsert 12345 at index 3')
	insert_at(a, 3, 12345)
	display(a)

	print('\nDelete element at index 5')
	removed = delete_at(a, 5)
	print('Removed:', removed)
	display(a)

	target = a[2]
	print(f"\nSearch for value {target}")
	idx = search_value(a, target)
	print('Found at index:', idx)

	print('\nSort the array and measure time')
	start = time.perf_counter()
	sort_array(a, in_place=True)
	duration = (time.perf_counter() - start) * 1e6
	print(f'Sort time: {duration:.0f} microseconds')
	display(a)

	print('\nReverse the array')
	reverse_array(a)
	display(a)


if __name__ == '__main__':
	demo_sequence()

