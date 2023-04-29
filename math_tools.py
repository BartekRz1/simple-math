import random


COLUMNS = 3
ROWS = 3

m_a =     [[1,2,3],
           [5,6,7],
           [9,9,9]]

m_b =      [[11,12,13],
            [66,65,44],
            [76.23,36]]

print(m_a)
print("\n\n")

random_matrix = [[random.randint(1,12) for _ in range(3)] for _ in range(3)]

# Wyświetlenie macierzy w układzie od góry do dołu
for row in random_matrix:
    print(row)
