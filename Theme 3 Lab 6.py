list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_num = max(list_numbers)
index_max = list_numbers.index(max_num)
index_len = len(list_numbers) - 1
list_numbers[index_max], list_numbers[index_len] = list_numbers[index_len], list_numbers [index_max]
print(list_numbers)
