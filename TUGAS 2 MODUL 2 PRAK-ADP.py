print("Program Pesan-Antar Makanan Online")
print()

print("Selamat Datang di Restoran Naadhirah")
print()

print("Wah, keranjang anda masih kosong, silahkan memilih paket, dan selamat berbelanja!")
print()

makanan = 0
print("1. Paket A = Rp 25.000,00")
print("2. Paket B = Rp 30.000,00")
print("3. Paket C = Rp 45.000,00")
print()

mau_pesan = input("Apakah anda ingin memesan makanan (y/n) ? ").lower()

if mau_pesan != "y" and mau_pesan != "n" :
	print("Note : ketik huruf Y, y, N, atau n saja. Y/y = yes dan N/n = no !")
	mau_pesan = input("Apakah anda ingin memesan makanan (y/n) ? ").lower()

while (mau_pesan == "y") :
	paket = input("tulis paket makanan yang anda beli : ").upper()
	if (paket == "A") :
		harga = 25000
	if (paket == "B") :
		harga = 30000
	if (paket == "C") :
		harga = 45000
	makanan = makanan + harga
	mau_pesan = input("Apakah anda ingin memesan makanan (y/n) ? ").lower()
	
if (mau_pesan == "n") :
	print("total harga makanan anda adalah : Rp " + str(makanan))
	
print()

x = int(input("Berapakah jarak dari rumah anda ke restoran (meter) ? "))

if (x<0) :
	print("Jarak tidak valid")
if (x < 500) :
	biaya = 0
if (500 <= x <= 1500) :
	biaya = 10000
if (x > 1500) :
	biaya = 20000
ongkir = biaya
print("total biaya ongkir anda adalah : Rp " + str(ongkir))
print()

print("total harga pesanan online anda adalah : Rp " + str (makanan+ongkir))
print()

print("Terimakasih telah berbelanja dan Selamat menikmati makanan anda")
