from termcolor import colored
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class gameSOS :
    def __init__(game) :
        game.high_score = 0
        game.load_game_data()
        game.reset_papan()
        game.sekarang_giliran = 'S'

    def startgame(game) :
        game.reset_papan()

    def reset_papan(game) :
        game.papan = [
            ['' for _ in range(3)] 
            for _ in range(3)
        ]
        game.previous_sos = set()
        game.score_S = 0
        game.score_O = 0
        game.high_score = 0

    def cetak_papan(game) :
        for baris in game.papan:
            cetak_baris = []
            for kotak in baris:
                if kotak:
                    kotak = kotak.upper()
                else:
                    kotak = '   '
                if kotak == 'S':
                    cetak_baris.append(colored(f"  {kotak}  ", 'white', 'on_blue'))
                elif kotak == 'O':
                    cetak_baris.append(colored(f"  {kotak}  ", 'white', 'on_red'))
                else:
                    cetak_baris.append(colored(f" {kotak} ", 'white', 'on_white'))
            print(' | '.join(cetak_baris))
            print('-' * 22)

    def switch_giliran(game) :
        if game.sekarang_giliran == 'S' :
            game.sekarang_giliran = 'O'
        else :
            game.sekarang_giliran = 'S'

    def check_winner(game) :
        sos_positions = []
        for baris in range(3) :
            for kolom in range(3) :
                if game.papan[baris][kolom] == 'S' :
                    if (kolom <= 1) and (game.papan[baris][kolom + 1] == 'O') and (kolom + 2 <= 2) and (game.papan[baris][kolom + 2] == 'S') :
                        sos_positions.append(((baris, kolom), (baris, kolom + 1), (baris, kolom + 2)))
                    if (baris <= 1) and (game.papan[baris + 1][kolom] == 'O') and (baris + 2 <= 2) and (game.papan[baris + 2][kolom] == 'S') :
                        sos_positions.append(((baris, kolom), (baris + 1, kolom), (baris + 2, kolom)))
                    if (baris <= 1) and (kolom <= 1) and (game.papan[baris + 1][kolom + 1] == 'O') and (baris + 2 <= 2) and (kolom + 2 <= 2) and (game.papan[baris + 2][kolom + 2] == 'S') :
                        sos_positions.append(((baris, kolom), (baris + 1, kolom + 1), (baris + 2, kolom + 2)))
                    if (baris <= 1) and (kolom >= 2) and (game.papan[baris + 1][kolom - 1] == 'O') and (baris + 2 <= 2) and (kolom - 2 >= 0) and (game.papan[baris + 2][kolom - 2] == 'S') :
                        sos_positions.append(((baris, kolom), (baris + 1, kolom - 1), (baris + 2, kolom - 2)))
        new_sos = [pos for pos in sos_positions if tuple(pos) not in game.previous_sos]
        game.previous_sos.update(tuple(pos) for pos in new_sos)
        return new_sos

    def make_steps(game, baris, kolom) :
        if game.papan[baris][kolom] == '' :
            game.papan[baris][kolom] = game.sekarang_giliran
            sos_terbentuk = game.check_winner()
            if sos_terbentuk :
                if game.sekarang_giliran == 'S':
                    game.score_S += len(sos_terbentuk)
                    if game.score_S > game.high_score :
                        game.high_score = game.score_S
                else :
                    game.score_O += len(sos_terbentuk)
                    if game.score_O > game.high_score :
                        game.high_score = game.score_O
            else :
                game.switch_giliran()
        else:
            print("Kotak sudah terisi, coba di kotak lain!")

    def timelapse(game) :
        for i in range(3, 0, -1) :
            print(f" Mulai dalam {i} detik... ")
            time.sleep(1)
        print(" Mulai! ")

    def livegame(game) :
        game.timelapse()
        while True :
            clear_screen()
            print()
            game.cetak_papan()
            print()
            print(f" Giliran: {game.sekarang_giliran} ")
            print(f" Score S = {game.score_S} dan Score O = {game.score_O} ")
            print(f" High score: {game.high_score} ")
            print()
            print('_' *25)
            try :
                baris = int(input(" Input baris (0, 1, 2): "))
                kolom = int(input(" Input kolom (0, 1, 2): "))
                if baris not in [0, 1, 2] and kolom not in [0, 1, 2] :
                    raise ValueError("Baris dan kolom harus dalam 0, 1, atau 2!")
                game.make_steps(baris, kolom)
            except ValueError as e :
                print(f" Input tidak valid : {e}. Silahkan Coba lagi! ")

                if all(all(kotak != '' for kotak in baris) for baris in game.papan) :
                    game.announce_winner()
                    print()
                    game.reset_papan()
                    game.timelapse()

    def announce_winner(game) :
        if game.score_S > game.score_O :
            print(" Pemenang : S ")
        elif game.score_O > game.score_S :
            print(" Pemenang : O ")
        else :
            print(" Permainan seri! ")
        print(f" Skor akhir : S = {game.score_S} dan O = {game.score_O} ")
        print(f" High score: {game.high_score} ")

    def save_game_data(game) :
        with open('game_data.txt', 'w') as file :
            file.write(f"{game.high_score}\n")
            file.write(f"{game.score_S}\n")
            file.write(f"{game.score_O}\n")

    def load_game_data(game) :
        try :
            with open('game_data.txt', 'r') as file :
                data = file.readlines()
                game.high_score = int(data[0].strip())
                game.score_S = int(data[1].strip())
                game.score_O = int(data[2].strip())
        except FileNotFoundError :
            game.high_score = 0
            game.score_S = 0
            game.score_O = 0

if __name__ == "__main__" :
    clear_screen()
    sos = gameSOS()
    sos.livegame()