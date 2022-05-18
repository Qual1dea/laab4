"""
Формируется матрица F следующим образом:
если в С количество нулей в нечетных столбцах в области 1 больше,
чем сумма чисел по периметру области 4, то поменять в C симметрично области 1 и 3 местами,
иначе С и Е поменять местами несимметрично. При этом матрица А не меняется.
После чего вычисляется выражение: А*(F+А)-K* FT .
Выводятся по мере формирования А, F и все матричные операции последовательно.
"""

import random
import time

def print_matrix(M, matrix_name,tt):
    print("Матрица:" + matrix_name + " \n промежуточное время = " +str(format(tt, '0.2f'))+ " seconds." )
    for i in M:  # перебор всех строк матрицы
        for j in i:  # перебираем все элементы в строке
            print("%5d" % j, end=' ')
        print()
try:
    row_q = int(input("Задайте количество строк и столбцов N в матрице:"))
    while row_q < 6:
        row_q = int(input(
            "Вы ввели неверное число\nЗадайте количество строк и столбцов N в матрице:"))
    K = int(input("Задайте коэффициент K:"))

    start = time.time()
    A, F, AF, FT = [], [], [], []  # задаем матрицы
    for i in range(row_q):
        A.append([0] * row_q)
        F.append([0] * row_q)
        AF.append([0] * row_q)
        FT.append([0] * row_q)
    time_next = time.time()
    print_matrix(F,"F",time_next-start)

    for i in range(row_q):  # заполняем матрицу А
        for j in range(row_q):
            A[i][j] = random.randint(-10,10)

    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "A",time_next-time_prev)
    for i in range(row_q):  # F
        for j in range(row_q):
            F[i][j] = A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F",time_next-time_prev)

    C = []  # задаем матрицу C
    size = row_q // 2
    for i in range(size):
        C.append([0] * size)

    for i in range(size):  # формируем подматрицу С
        for j in range(size):
            C[i][j] = F[i][size + row_q % 2 + j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(C, "C",time_next-time_prev)

    quantity = 0
    summa = 1
    for i in range(size):
        for j in range(size):
            if i < (size // 2) and j > (size // 2 - (size - 1) % 2):
                if j < (size - i - 1) and j < (size // 2 + i + size % 2) and j % 2 == 0 and C[i][j] == 0:
                    quantity += 1
                if i > size // 4 and ((size - 1 - i) < j < (size // 2 + i + size % 2)) and (
                        j == (size - i) or i == (size // 2 - 1) or j == (size // 2 + i - (size - 1) % 2)):
                    summa += C[i][j]

    if quantity > summa:
        for i in range(1, size // 2, 1):  # меняем подматрицу С
            for j in range(0, i, 1):
                C[i][j], C[i][size - j - 1] = C[i][size - j - 1], C[i][j]
        for i in range(size // 2, size, 1):
            for j in range(0, i, 1):
                C[i][j], C[i][size - j - 1] = C[i][size - j - 1], C[i][j]
        print_matrix(C, "C")
        for i in range(size):  # формируем матрицу F
            for j in range(size):
                F[i][size - row_q % 2 + j] = C[i][j]
    else:
        for j in range(row_q // 2 + row_q % 2, row_q, 1):
            for i in range(row_q // 2):
                F[i][j], F[row_q // 2 + row_q % 2 + i][j] = F[row_q // 2 + row_q % 2 + i][j], F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F",time_next-time_prev)
    print_matrix(A, "A",0)

    # считаем пример А*(F+А)-K* FT по действиям
    for i in range(row_q): #(F+A)
        for j in range(row_q):
           AF[i][j] = F[i][j] + A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF, "(F + A)",time_next-time_prev)

    for i in range(row_q):  # F*AF
      for j in range(row_q):
           AF[i][j] = F[i][j] * AF[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "K*FA",time_next-time_prev)

    for i in range(row_q):  # FT
        for j in range(i, row_q, 1):
          FT[i][j], FT[j][i] = F[j][i], F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(FT, "F^T",time_next-time_prev)

    for i in range(row_q):  # K*FT
       for j in range(row_q):
         FT[i][j] = K * FT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(FT, "K*F^T",time_next-time_prev)

    for i in range(row_q):  # А*(F+А)-K* FT
       for j in range(row_q):
         AF[i][j] = AF[i][j] - FT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF, "А*(F+А)-K* FT",time_next-time_prev)

    finish = time.time()
    result = finish - start
    print("Program time: " + str(result) + " seconds.")

except FileNotFoundError:
    print("\n это не число, перезапустите программу")