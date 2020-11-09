import os

def masukanNama():
    nama = input("Masukan Namamu : ")
    
    f = open("NamaStorage.txt","w")
    f.write(nama)
    print("Nama : " + nama + ", telah diedit")
    f.close()

def hapusNama():
    if os.path.exists("NamaStorage.txt"):
        os.remove("NamaStorage.txt")
    else:
        print("The file does not exist")

def cetakNama():
    f = open("NamaStorage.txt", "r")
    for x in f:
        print(x)
