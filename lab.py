from random import randint

print("Введите кол-во вершин графа")
num = int(input())
c = num
matrix = [0] * c
count = 0
max = 0
izo = []
max_dom = []
inc_max_dom = []
konc = []
inc_konc = []
inc_izo = []

for i in range(num): #создание матрицы
    matrix[i] = [0] * c

for i in range(num): #заполнение матрицы
    c -= 1
    for j in range(c):
        if i == j:
            matrix[i][j] = 0
        else:
            matrix[i][j] = randint(0, 1)
            matrix[j][i] = matrix[i][j]

for i in range(len(matrix)): #определение размера матрицы, изолированных, 
    dom = 0
    for j in range(len(matrix)):
        if matrix[i][j] == 1:
            count += 1
            dom += 1
    if (dom > max) or (dom == max):
        max = dom
    if dom == 0:
        izo.append(i + 1)
    if dom == 1:
        konc.append(i + 1)

for i in range(len(matrix)): #определение доминирующих вершин
    a = 0
    for j in range(len(matrix)):
        if matrix[i][j] == 1:
            a += 1
    if a == max:
        max_dom.append(i + 1)

num_vertices = len(matrix)
num_edges = sum(sum(row) for row in matrix) // 2

inc_matrix = [[0] * num_edges for _ in range(num_vertices)]

edge_counter = 0
for i in range(num_vertices):
    for j in range(i+1, num_vertices):
        if matrix[i][j] == 1:
            inc_matrix[i][edge_counter] = 1
            inc_matrix[j][edge_counter] = 1
            edge_counter += 1

print("Матрица смежности")
for i in matrix:
    print(i)
    
print("Матрица инфидентности")
for row in inc_matrix:
    print(row)
    
count = count // 2
print("Размер графа:")
print(count)
print("Доминирующая(-ие) вершина(-(ы) (смежности):")
for x in max_dom:
    print(x)
print("Изолированная(-ые) вершина(-ы) (смежности):")
for x in izo:
    print(x)
print("Концевая(-ые) вершина(-ы) (смежности)")
for x in konc:
    print(x)

max = 0
count = 0
for i in inc_matrix:
    count += 1
    im = 0
    for j in i:
        im += j
    if im >= max:
        inc_max_dom.append(count)
        max = im
    if im == 1:
        inc_konc.append(count)
    if im == 0:
        inc_izo.append(count)
print("-----------------------------------------------")
print("Доминирующая(-ие) вершина(-(ы) (инцидентности):")
for x in inc_max_dom:
    print(x)
print("Изолированная(-ые) вершина(-ы) (инцидентности):")
for x in inc_izo:
    print(x)
print("Концевая(-ые) вершина(-ы) (инцидентности)")
for x in inc_konc:
    print(x)
