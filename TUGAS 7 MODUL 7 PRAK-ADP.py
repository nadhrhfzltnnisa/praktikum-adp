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

def mean(s) :
    data1 = 0
    for i in range (s) :
    	data1 = data1 + data[ i ]
    rata2 = data1/s
    return rata2 
s = len(data)
print(" Mean data ini adalah = ", mean(s))
    
def modus(s) :
    data2 = { }
    for i in data:
        if i in data2 :
            data2[i] += 1
        else:
            data2[i] = 1
    maxnilai = max(data2.values())
    modus = [ ]
    for i, j in data2.items() :
        if j == maxnilai:
            modus.append(i)
    return modus
s = len(data)
print(" Modus data ini adalah = ", modus(s))
	
def variance(s) :
	rata2 = mean(s)
	sigmaselisihkuadrat = 0
	for nilai in data :
		selisih = nilai - rata2
		sigmaselisihkuadrat += selisih**2
	varians = sigmaselisihkuadrat / (s - 1)
	return varians
print(" Variance data ini adalah = ", variance(s))
