def hitung_mobil(asal_mobil):
    solo = []
    jogja = []
    surabaya = []
    magelang = []
    asal_mobil = ""
    while asal_mobil != "done":
        if asal_mobil == "solo" or asal_mobil == "jogja" or asal_mobil == "surabaya" or asal_mobil == "magelang":
            jumlahSol = solo.append(solo)

            # jogja.append(jogja)
            # surabaya.append(surabaya)
            # magelang.append(magelang)
            print(f"Jumlah Mobil Solo : {jumlahSol}\nJumlah Mobil Jogja : {jumlahJog}\nJumlah Mobil Surabaya : {jumlahSur}\nJumlah Mobil Magelang : {jumlahMag}")
        elif asal_mobil == "jogja":
            jumlahJog = jogja.append(jogja)
       
        elif asal_mobil == "surabaya":
            jumlahSur = surabaya.append(surabaya)
        
        elif asal_mobil == "magelang":
            jumlahMag = magelang.append(magelang)
        
        else:
            break
    # print(f"Jumlah Mobil Solo : {len(solo)}\nJumlah Mobil Jogja : {len(jogja)}\nJumlah Mobil Surabaya : {len(surabaya)}\nJumlah Mobil Magelang : {len(magelang)}")

asal_mobil = str(input("masukkan asal mobil (ketik done untuk keluar) : ")).lower()

hitung_mobil(asal_mobil)
