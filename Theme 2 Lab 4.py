BYTES_ONE_CHAR = 1  # размер одного символа в байтах

# никаких магических чисел
pages = 100  # TODO ввести количество страниц
lines = 50  # TODO ввести количество строк
chars = 25  # TODO ввести количество символов в строке

total_chars = pages * lines * chars
total_bytes = total_chars + BYTES_ONE_CHAR

disk_size = 1.44 * 1024 * 1024

print(disk_size // total_bytes)  # TODO найти количество книг, которое поместится на дискете
