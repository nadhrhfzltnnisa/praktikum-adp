print ("| Program Perulangan Kelipatan 4 = DOR dengan Total Angka 80 |")
print("==============================================================")
print()

for i in range (1,81) :
	if ( i%4 == 0 ) :
		print("DOR", end = " ")
	else :
		print(i, end = " ")
	if ( i%8 == 0 ) :
		print()