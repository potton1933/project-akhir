database = []

# membuat fungsi authentifikasi sederhana
def get_login():
    print('=' * 50)
    print('halaman login kasir')
    username = input('masukan username kasir anda: ')
    password = input('masukan password: ')
 
    if username == 'admin' and password == 'admin':
        print('login berhasil...\n\n')
        main_menu()
    else:
        print('login gagal coba lagi..')
        get_login()
def counter_kasir():
    counter = input('hitung lagi: (y/n)')
    if counter == 'y':
         
        kasir()
     
    elif counter == 'n':
        print('ingin hitung lagi..?')
        tanya()
     
    else:
        print('input program salah harap ulangi')
def kasir():
    # masukan input dari user
    nama_barang = input('masukan pesanan anda: ')
    harga = int(input('masukan harga barang: '))
    jumlah_beli = int(input('masukan jumlah barang yang anda beli: '))
 
    # mengitung jumlah harga
    total = harga * jumlah_beli
     
    # cetak total harga
    print(f'harga total: {nama_barang}, = {total}')
 
    # input pembayaran dari user
    bayar = int(input('masukan pembayaran: '))
 
    # mengecek apakah pembayaran kurang atau ada kembalian
    kurang = total - bayar
    kembalian = bayar - total
 
    sementara = {
        'nama barang' : nama_barang,
        'harga' : harga,
        'jmlh beli' : jumlah_beli,
        'total' : total,
        'bayar' : bayar
    }

    database.append(sementara)

    if bayar > total:
        print(f'jumlah kembalian anda adalah {kembalian}')
        tanya()
     
    elif bayar == total:
        print('uang anda pas, terimakasih telah berbelanja ')
        a = (input("apakah ingin mengulang? y/n "))
        if a  == "y" :

            main_menu()
    else:
        print(f'maaf uang anda tidak cukup, uang anda kurang {kurang}')
        counter_kasir()
    

def kelola_pesanan():
    print('[1] tampil data')
    print('[2] edit data')
    print('[3] hapus data')

    kode=input('masukkan kode : ')
    if kode =='1':
            tampil()
    elif kode =='2':
            edit()
    elif kode =='3':
            hapus()
    else :
        print("kode salah")

def tampil():
    z = len(database)
    for i in range(z):
        a=i
        a+=1
        print( a, " ",database[i])
    kelola_pesanan()

def edit():
    print("edit")
    for i in range(len(database)):
        print(f'baris {i+1} =', database[i])
    index = int(input('masukkan baris data yang ingin diedit : '))
    print ( "a. edit nama barang\n"
            "b. edit harga\n"
            "c. edit jmlh beli\n"
            "d. edit bayar\n"
    )
    tanya=input("masukkan data yang akan diubah : ")
    if tanya=="a":
        nama=input("input nama barang : ")
        database[index-1]["nama barang"]= nama
    elif tanya=="b":
        variabel=int(input("input harga baru: "))
        database[index-1]["harga"]= variabel
        total=database[index-1]["jmlh beli"]*variabel
        database[index-1]["total"]=total
    elif tanya=="c":
        nama=int(input("input jumlah pembelian : "))
        database[index-1]["jmlh beli"]= nama
        total=database[index-1]["harga"]*nama
        database[index-1]["total"]=total
    elif tanya=="d":
        nama=int(input("input pembayaran : "))
        database[index-1]["bayar"]= nama
    else: 
        print("sudah diperbarui")
    index -= 1
    kelola_pesanan()

def hapus():
    # print(database)
    for i in range(len(database)):
        print(f'baris {i+1} =', database[i])
    index = int(input('masukkan baris data yang ingin dihapus '))
    index -= 1
    del database[index]
    kelola_pesanan()
    

def main_menu():
    # membuat daftar menu pada kasir
    print('=' * 10, 'MAIN MENU APLIKASI KASIR RESTO', '=' * 10)
    print('selamat datang di aplikasi kasir resto mamamia')
    print('=' * 20, 'masukan input aplikasi', '=' * 20)
    print('1. Program kasir')
    print('2. Program kalkulator')
    print('3. Kelola pesanan')
    print('4. Exit program')
 
    # input pilihan
    pilihan = input('pilih menu: ')
 
    # pilihan menu
    if pilihan == '1':
        kasir()
    elif pilihan == '2':
        kalkulator()
    elif pilihan == '3':
        kelola_pesanan()
    else:
        print('program exit')
        exit()
 
def tanya():
    tanya = input('kembali ke menu..? (y/n)')
    if tanya == 'y':
        main_menu()
    elif tanya == 'n':
        exit()
    else:
        print('input salah')
        print('masukan input dengan benar')
def kalkulator():
    print('=' * 20)
    print('Program Kalukator')
 
    print()
    print('Operator')
    print('=' * 10)
    print('1. tambah')
    print('2. kurang ')
    print('3. bagi')
    print('4. kali')
    print('5. sisa bagi/modulus')
 
    a = int(input('masukan bilangan pertama: '))
    b = int(input('masukan bilangan ke-dua: '))
 
    operator = input('masukan operator: ')
 
    if operator == '1':
        print('hasil dari {} + {} = {}'.format(a, b, a + b))
    elif operator == '2':
        print('hasil dari {} - {} adalah {}'.format(a, b, a - b))
    elif operator == '3':
        print('hasil dari {} / {} = {}'.format(a, b, a / b))
    elif operator == '4':
        print('hasil dari {} * {} = {}'.format(a, b, a * b))
    elif operator == '5':
        print('hasil dari {} % {} = {}'.format(a, b, a % b))
    else:
        print('masukan input yang benar sesuai menu diatas')