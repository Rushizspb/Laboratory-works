list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
unik_chisla = set(list_) #Находим уникальные числа
summa_unik = sum(unik_chisla) #Сумма уникальных чисел
kolich_unik = len(unik_chisla)


print (summa_unik)
print (kolich_unik)
print (round(summa_unik / kolich_unik, 5))
