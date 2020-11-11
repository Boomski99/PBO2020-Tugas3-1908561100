import os
class user():
    def __init__(self):
        self.nama = nama

def masukanNama():
    user.nama = input("Masukan Namamu : ")
    
    f = open("NamaStorage.txt","w")
    f.write(user.nama)
    print("Nama : " + user.nama + ", telah diedit")
    f.close()

def hapusNama():
    if os.path.exists("NamaStorage.txt"):
        os.remove("NamaStorage.txt")
    else:
        print("The file does not exist")

def cetakNama():
    try:
        f = open("NamaStorage.txt", "r")
        print("Nama : ")
        for x in f:
            print(x)
    except:
        print("Maaf Nama = Kosong")
