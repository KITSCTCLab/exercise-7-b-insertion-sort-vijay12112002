from typing import List

def insertionSort(array) -> List[int]:
  for step in range(size):
    min_idx = step
    for i in range(step + 1, size):
      if array[i] < array[min_idx]:
        min_idx = i
    (array[step], array[min_idx]) = (array[min_idx], array[step])
  return array

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
