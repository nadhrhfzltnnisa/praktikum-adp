print(" Nama : Naadhirah Fazilatun Nisa")
print(" NIM  : 2310433021")
print()
print(" Program Mean, Modus, dan Variance")
print()

def input_data(n):
    data = [ ]
    for i in range(n):
        a = int(input(" Input data-data: "))
        data.append(a)
    return data
n = int(input(" Input jumlah data = "))
data = input_data(n)

print()
print(" +------------------------------+")
print(" | {:<10} | {:<15} |".format(" Statistik", " Hasil"))
print(" +------------------------------+")


def mean(s) :
    data1 = 0
    for i in range (s) :
    	data1 = data1 + data[ i ]
    rata2 = data1/s
    return rata2 
s = len(data)
hasil_mean = mean(s)
print(" | {:<10} | {:<15} |".format("Mean", hasil_mean))
    
def modus(s) :
    data2 = [ 0 ] * (max(data) + 1)
    for i in data :
        data2[ i ] += 1
    maxnilai = max(data2)
    modus = [ ]
    for i in data :
        if data2[ i ] == maxnilai :
            if i not in modus :
                modus.append(i)
    return modus
s = len(data)
hasil_modus = modus(s)
print(" | {:<10} | {:<15} |".format("Modus", ', '.join(map(str, hasil_modus))))
	
def variance(s) :
	rata2 = mean(s)
	sigmaselisihkuadrat = 0
	for nilai in data :
		selisih = nilai - rata2
		sigmaselisihkuadrat += selisih**2
	varians = sigmaselisihkuadrat / (s - 1)
	return varians
hasil_variance = variance(s)
print(" | {:<10} | {:<15} |".format("Variance", hasil_variance))

print(" +______________________________+")
