def hitung_mobil():
    jumlahSol = 0
    jumlahJog = 0
    jumlahSur = 0
    jumlahMag = 0
    while True:
        asal_mobil = str(input("masukkan asal mobil (ketik done untuk keluar) : ")).lower()
        if asal_mobil == "solo" or asal_mobil == "jogja" or asal_mobil == "surabaya" or asal_mobil == "magelang":
            jumlahSol = jumlahSol + 1
        elif asal_mobil == "jogja":
            jumlahJog = jumlahJog + 1
        elif asal_mobil == "surabaya":
            jumlahSur = jumlahSur + 1
        elif asal_mobil == "magelang":
            jumlahMag = jumlahMag + 1
        elif asal_mobil == "done":
            break
    
    print(f"Jumlah Mobil Solo : {jumlahSol}\nJumlah Mobil Surabaya : {jumlahSur}\nJumlah Mobil Jogja : {jumlahJog}\nJumlah Mobil Magelang : {jumlahMag}")


hitung_mobil()