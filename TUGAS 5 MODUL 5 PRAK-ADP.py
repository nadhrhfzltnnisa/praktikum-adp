print("Nama    : Naadhirah Fazilatun Nisa")
print("NIM     : 2310433021")
print()

print("Program Array Nilai x dan Fungsi f(x)")
print()

import numpy as np

nilai_x = np.arange( -10, 11 )
fungsi_f = [ ]

for x in nilai_x :
	if (x > 0) :
		fungsi_f.append(x**2 + 2*x)
	elif (x < 0) :
		fungsi_f.append(1/x)
	elif (x == 0) :
		fungsi_f.append(10)
	else :
		print("terjadi kesalahan input")

column_width = 10		
print(f" |{'----------':<{column_width}}|{'----------':<{column_width}}|")
print(f" |{'    x':<{column_width}}|{'   f(x)':<{column_width}}|")
print(f" |{'----------':<{column_width}}|{'----------':<{column_width}}|")

for i in range(len(nilai_x)) :
	x = nilai_x[ i ]
	f = fungsi_f[ i ]
	print(f" |{x:<{column_width}}|{f:<{column_width}.3f}| ")

print(f" |{'__________':<{column_width}}|{'__________':<{column_width}}|")
