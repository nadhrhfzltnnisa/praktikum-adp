print("Program Menghitung Nilai Diskriminan dan Hasil Kali Akar")
print()

input('bentuk umum SPK = ax² + bx +c')
input('PK  = ')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

diskriminan = (b**2) - (4*a*c)
HKA = (c/a)
print('D = ' + str(diskriminan))
print('HKA = ' + str(HKA))