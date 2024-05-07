print(" Nama : Naadhirah Fazilatun Nisa")
print(" NIM  : 2310433021")
print()
print(" Program Penjumlahan dan Perkalian Matriks")
print()

n = int(input(" Input ukuran matriks (nxn) = "))
print(" ukuran matriks A & B adalah : ", n, " x ",n)
print()

# matriks A
A = [ ]
for i in range (n) :
	baris1 = [ ]
	for j in range (n) :
	       a = int(input(f" B{i+1} K{j+1} : "))
	       baris1.append(a)
	A.append(baris1)
print(" matriks A = ", A)
print()

# matriks B	
B = [ ]
for i in range (n) :
	baris2 = [ ]
	for j in range (n) :
	       b = int(input(f" B{i+1} K{j+1} : "))
	       baris2.append(b)
	B.append(baris2)
print(" matriks B = ", B)
print()

# matriks C [perkalian matriks A dan B]
C = [ ]		
for i in range (n) :
	baris3 = [ ]
	for j in range (n) :
		c = A[ i ][ 0 ]*B[ 0 ][ j ] + A[ i ][ 1 ]*B[ 1 ][ j ]
		baris3.append(c)
	C.append(baris3)
print(" hasil dari matriks A x B adalah : ")
print(" matriks C = ", C)
print()

# matriks A Transpose
AT = [ ]
for i in range (n):
    baris4 = [ ]
    for j in range (n):
       a = A[ j ][ i ]
       baris4.append(a)
    AT.append(baris4)
print(" matriks A Transpose : ")
print(" AT =", AT)

# matriks B Transpose
BT = [ ]
for i in range (n):
    baris5 = [ ]
    for j in range (n):
       b = B[ j ][ i ]
       baris5.append(b)
    BT.append(baris5)
print(" matriks B Transpose : ")
print(" BT =", BT)
print()

# matriks D [penjumlahan matriks AT dan BT]
D = [ ]
for i in range (n) :
	baris6 = [ ]
	for j in range (n) :
		d = AT[ i ][ j ] + BT[ i ][ j ]
		baris6.append(d)
	D.append(baris6)
print(" hasil dari matriks AT + BT adalah : ")
print(" matriks D = ", D)
print()
