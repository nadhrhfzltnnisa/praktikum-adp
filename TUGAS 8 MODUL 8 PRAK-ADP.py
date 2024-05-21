print(" Nama : Naadhirah Fazilatun Nisa")
print(" NIM  : 2310433021")
print()
print(" Program Pendataan Film")
print()

def input_films() :
    favfilms = {}

    try :
        with open("data_films.txt", "a") as file :
            pass
        with open("data_films.txt", "r") as file :
            for baris in file :
                judul, penulis, sutradara, tahun, genre = baris.strip().split(" | ")
                favfilms[judul] = {
                    "Penulis" : penulis,
                    "Sutradara" : sutradara,
                    "Tahun rilis" : tahun,
                    "Genre" : genre
                }
    except FileNotFoundError :
        with open("data_films.txt", "w") as file :
            pass

    return favfilms

def save(favfilms) :
    with open("data_films.txt", "w") as file :
        for judul, rincian in favfilms.items() :
            file.write(f" {judul} | {rincian['Penulis']} | {rincian['Sutradara']} | {rincian['Tahun rilis']} | {rincian['Genre']}\n")

def add(favfilms) :
    print()
    judul = input(" Judul film : ")
    penulis = input(" Writer : ")
    sutradara = input(" Director : ")
    tahun = input(" Released in year : ")
    genre = input(" Genre : ")

    favfilms[judul] = {
        "Penulis" : penulis,
        "Sutradara" : sutradara,
        "Tahun rilis" : tahun,
        "Genre" : genre
    }
    save(favfilms)
    print(" Film baru berhasil di add!")

def delete(favfilms) :
    judul = input(" Judul film yang akan dihapus: ")
    if judul in favfilms :
        del favfilms[judul]
        save(favfilms)
        print(" Film berhasil di delete!")
    else :
        print(" Film tidak berhasil ditemukan!")

def edit(favfilms) :
    judul = input(" Judul film yang akan diedit : ")
    
    if judul in favfilms :
        penulis = input(" Writer yang benar : ")
        sutradara = input(" Director yang benar : ")
        tahun = input(" Release year yang benar : ")
        genre = input(" Genre yang benar : ")
        
        favfilms[judul] = {
            "Penulis" : penulis,
            "Sutradara" : sutradara,
            "Tahun rilis" : tahun,
            "Genre" : genre
        }
        save(favfilms)
        print(" Film berhasil di edit!")
    else :
        print(" Film tidak berhasil ditemukan!")

def show(favfilms) :
    if favfilms :
        for judul, rincian in favfilms.items() :
            print("=============================")
            print()
            print(f" Judul : {judul}")
            print(f" Writer : {rincian['Penulis']}")
            print(f" Director : {rincian['Sutradara']}")
            print(f" Released year : {rincian['Tahun rilis']}")
            print(f" Genre : {rincian['Genre']}")
            print()
            print("=============================")
    else:
        print(" Film belum berhasil tersimpan!")

def main() :
    favfilms = input_films()
    while True :
        print("\n +---------------------+")
        print(" | Menu - menu : |")
        print(" | [1]. Input Film |")
        print(" | [2]. Delete Film |")
        print(" | [3]. Edit Film|")
        print(" | [4]. Show Film|")
        print(" | [5]. Exit |")
        print(" +__________________+")
        print()

        pilihan = input(" Pilih menu (1/2/3/4/5): ")
        if pilihan == "1":
            add(favfilms)
        elif pilihan == "2":
            delete(favfilms)
        elif pilihan == "3":
            edit(favfilms)
        elif pilihan == "4":
            show(favfilms)
        elif pilihan == "5":
            break
        else:
            print(" Pilihan tidak ada, input pilihan yang valid!!!")

main()
