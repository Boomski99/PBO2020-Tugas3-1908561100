from NamaStorage import masukanNama, hapusNama, cetakNama

def mainProgram():
    print("Selamat datang di Program Nama Target")
    print("Menu :\n 1. Ubah Nama\n 2. Cetak Nama\n 3. Hapus Nama \n 4. Quit")
    pil = (int(input("Pil : ")))

    if pil == 1:
        masukanNama()
    elif pil == 2:
        cetakNama()
    elif pil == 3:
        hapusNama()
    elif pil == 4:
        exit()
    else :
        print("Maaf, pilihan anda tidak tersedia, silahkan coba memasukan kembali")

    input("Tekan enter untuk melanjutkan")
if __name__ == "__main__":

    while(True):
        mainProgram()
