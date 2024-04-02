print("Nama    : Naadhirah Fazilatun Nisa")
print("NIM     : 2310433021")
print()

print("Program Daftar Belanja")
print()

print("                ==============================")
print("                     SELAMAT DATANG DI TOKO")
print("                     NAARA JAPANESE BAKERY")
print("                     TOKO ROTI KHAS JEPANG")
print("                ==============================")
print()

print("Yah, keranjang belanja anda masih kosong :(")
print("Silahkan memilih sesuai selera dan Selamat berbelanja!")
print()

roti = 0
print("  >>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("  #  Menu Roti Naara Bakery  #")
print("  <<<<<<<<<<<<<<<<<<<<<<<<<<<")
print("  +------------------------------------+")
print("  | NO |   JENIS ROTI   |     HARGA    |")
print("  +------------------------------------+")
print("  | 1. | Cheesecake     = Rp 65.000,00 |")
print("  | 2. | Shokupan       = Rp 50.000,00 |")
print("  | 3. | ChocoCornet    = Rp 30.000,00 |")
print("  | 4. | Melonpan       = Rp 25.000,00 |")
print("  | 5. | Karepan        = Rp 15.000,00 |")
print("  +------------------------------------+")
print()

print(" !!! SPESIAL PROMO RAMADHAN !!!")
print(" a. Untuk setiap pembelian CheeseCake lebih dari 3 pcs akan mendapat DISKON 25%")
print(" b. Jika costumer berbelanja lebih dari Rp 200.000,00, maka akan mendapat DISKON 10%")
print()

mau_pesan = input("Apakah anda ingin memesan (y/n) ? ").lower()

while mau_pesan not in ["y", "n"]:
    print("Note : ketik huruf Y, y, N, atau n saja. Y/y = yes dan N/n = no !")
    mau_pesan = input("Apakah anda ingin memesan (y/n) ? ").lower()

if mau_pesan == "y":
    while mau_pesan == "y":
        jenis = input("Tulis nomor jenis roti yang ingin anda beli : ").upper()
        if jenis == "1":
            jrc = int(input("Jumlah Cheesecake yang di pesan : "))
            if jrc > 3:
                harga = (jrc * 65000) - (jrc * 65000 * 0.25)
                print("Anda mendapatkan diskon 25% untuk Cheesecake !")
            else:
                harga = jrc * 65000
        elif jenis == "2":
            jrs = int(input("Jumlah Shokupan yang di pesan : "))
            harga = jrs * 50000
        elif jenis == "3":
            jrcc = int(input("Jumlah ChocoCornet yang di pesan : "))
            harga = jrcc * 30000
        elif jenis == "4":
            jrm = int(input("Jumlah Melonpan yang di pesan : "))
            harga = jrm * 25000
        elif jenis == "5":
            jrk = int(input("Jumlah Karepan yang di pesan : "))
            harga = jrk * 15000
        else:
            print("Jenis roti yang anda masukkan tidak tersedia")
        roti += harga
        mau_pesan = input("Apakah anda ingin memesan lagi (y/n) ? ").lower()

if mau_pesan == "n":
    if roti > 200000:
        diskon_total = roti * 0.1
        roti -= diskon_total
        print("Anda mendapatkan diskon 10% karena berbelanja lebih dari Rp200.000 !")
    if roti == 0:
        print("Anda tidak memesan roti apapun.")

print("Total harga pesanan roti anda adalah : Rp " + str(roti))
print()
print()
print()
print()

print("      ==================================================")
print("          	$ STRUK BELANJA CUSTOMER $")
print("             	NAARA JAPANESE BAKERY")
print("             	TOKO ROTI KHAS JEPANG")
print("      ==================================================")
print()

if 'jrc' in locals():
    print("    	CHEESECAKE        " + str(jrc))
if 'jrs' in locals():
    print("    	SHOKUPAN          " + str(jrs))
if 'jrcc' in locals():
    print("    	CHOCOCORNET       " + str(jrcc))
if 'jrm' in locals():
    print("    	MELONPAN          " + str(jrm))
if 'jrk' in locals():
    print("    	KAREPAN           " + str(jrk))
print("    	TOTAL HARGA       RP " + str(roti))
print()
print("        	==============================")
print("       TERIMAKASIH TELAH MEMILIH NAARAA JAPANESE BAKERY")
print("       SEBAGAI ROTI PILIHAN ANDA!")
