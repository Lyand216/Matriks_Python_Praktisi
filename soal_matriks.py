import numpy as np
# # NO 1
# Penjumlahan dan pengurangan

# penjumlahan
print("Penjumlahan")
matriks1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriks2 = np.array([[4, 8, 7], [6, 3, 4], [5, 2, 1]])

for i in range(0, len(matriks1)):
    for j in range(0, len(matriks2)):
        print(matriks1[i][j] + matriks2[i][j], end=" ")
print()

print("Pengurangan")
# pengurangan
for i in range(0, len(matriks1)):
    for j in range(0, len(matriks2)):
        print(matriks1[i][j] - matriks2[i][j], end=" ")
print()


# NO 2
# Perkalian matriks
print("Perkalian matriks")
matriks1 = np.array([[1, 3], [4, 6]])
matriks2 = np.array([[3, 2], [1, 4]])
print(np.dot(matriks1, matriks2))

# NO 3
# Transpose matriks
print("Transpose matriks")
matriks = np.array([[1, 2, 3], [4, 5, 6]])

print(np.transpose(matriks))

# NO 4
# Invers matriks
print("Invers matriks")
matriks1 = np.array([[4, -2, 1], [5, 0, 3], [-1, 2, 6]])

print(np.linalg.inv(matriks1))


# NO 5
# Matriks Identitas
print("Matriks Identitas")
matriks_identitas = np.eye(4)
print(matriks_identitas)


# NO 6
# Reshape Matriks
print("Reshape Matriks")
matriks = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2], [3, 4, 5, 6]])
matriks_reshape = np.reshape(matriks, (2, 8))

print(matriks_reshape)
