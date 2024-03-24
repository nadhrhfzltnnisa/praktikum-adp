print ("| Program Perulangan Kelipatan 4 = DOR dengan Total Angka 80 |")
print ("==============================================================")
print()

i = 1
for i in range (i,81) :
	if ( i%4 == 0 ) :
		print("DOR", end = " ")
	else :
		print(i, end = " ")
	if ( i%8 == 0 ) :
		print()
