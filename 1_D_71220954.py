def ganti_kata(kalimat, cari_kata, kata_baru):
    for kalbaru in kalimat :
        data_baru = ""
        if kalbaru == cari_kata:
            kalbaru = kata_baru
        data_baru = data_baru + kalbaru
        print(data_baru, end = " ")
        continue
    return data_baru
    
kalimat = str(input("Masukkan kalimat : ")).split()
cari_kata = str(input("Kata yang dicari : "))
kata_baru = str(input("Diganti menjadi : "))
ganti_kata(kalimat, cari_kata, kata_baru)