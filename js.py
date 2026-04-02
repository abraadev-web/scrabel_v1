password = "69"

def menu():
    print(">======menu======<")
    print("1. kosong")
    print("2. kosong")
    print("3. kuasol")
    print(">=================<")
    
    pilihan = input("pilih menu: ")

    if pilihan == "1":
        print("kamu pilih 1")
    elif pilihan == "2":
        print("kamu pilih 2")
    elif pilihan == "3":
        print("kamu pilih 3")
    else:
        print("pilihan tidak ada")

for i in range(3):
    psw = input("masukkan password: ")

    if psw == password:
        print("akses benar")
        menu()
        break
    else:
        print("akses ditolak")

if i == 2 and psw != password:
    print("kamu gagal 3x, akses dikunci")