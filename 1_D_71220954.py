def ganti_kata(kalimat):
    for i in kalimat :
        if i == cari_kata:
            continue
            if i == kata_baru:
                break
            print(i, end = " ")
        print(i, end = " ")
    # print(i, kata_baru)
    # n = cari_kata
    # tambah = list(i)
    # tambah.insert(n, kata_baru)
    # tambah = ''.join(tambah)
    # print(str(tambah))



kalimat = str(input("Masukkan kalimat : ")).split()
cari_kata = str(input("Kata yang dicari : "))
kata_baru = str(input("Diganti menjadi : "))
ganti_kata(kalimat)