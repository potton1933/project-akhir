data ={
    0:"Laptop ",
    1:"Mouse  ",
    2:"charger",
    3:"Monitor",
    4:"Key Board"
    }
harga_data=[
    200000,
    300000,
    400000,
    500000,
    600000
]
dict_trx = {}
metode_pembayaran = {
    1:"Transfer",
    2:"Virtual account",
    3:"kartu kredit",
    4:"COD"
    }
data_order={}
print("----------------------------------")
for i in data:
    print("id Product :",i,"\t Nama Product :",data[i],"\t Harga Product :",harga_data[i-5])
pilih_id =int(input("Pilih Id Product Yang ingin di beli : "))

if pilih_id in data :
    pilih_beli=input("ingin beli ?(Y/N)")
    if pilih_beli == "y" or pilih_beli =="Y":
        data_order={
            'nama' :(input("Masukkan Nama :")),
            'alamat'           : input("Masukkan alamat :"),
            'telepon'          : int(input("Masukkan NO.Telepon :")),
            'Kurir_pengiriman' : input("Kurir Pngiriman :")
        }
        dict_trx={
            "nama penerima ":data_order["nama"],
            "alamat penerima":data_order["alamat"],
            "NO HP":data_order["telepon"],
            "kurir pengiriman":data_order["Kurir_pengiriman"],
            "product id":data
        }
        rubah = str(input('Apakah anda ingin mengubah data diri (Y/N) : '))
        if rubah == "y" or rubah == "Y":
            data_order={
            'nama' :(input("Masukkan Nama :")),
            'alamat'           : input("Masukkan alamat :"),
            'telepon'          : int(input("Masukkan NO.Telepon :")),
            'Kurir_pengiriman' : input("Kurir Pngiriman :")
            }
            dict_trx={
                "nama penerima ":data_order["nama"],
                "alamat penerima":data_order["alamat"],
                "NO HP":data_order["telepon"],
                "kurir pengiriman":data_order["Kurir_pengiriman"],
                "product id":data
            }
        else:
            pass
        for i in metode_pembayaran:
            print("id  : ",i,metode_pembayaran[i])
        pilih_metode = int(input("Pilih ID Metode Pembayaran :"))
        if pilih_metode in metode_pembayaran:
                print("Nama Penerima : ",dict_trx["nama penerima "])
                print("Alamat Penerima : ",dict_trx["alamat penerima"])
                print("NO HP : ",dict_trx["NO HP"])
                print("Kurir Pengiriman : ",dict_trx["kurir pengiriman"])
                print("Product : ",data[pilih_id])
                print("Harga : ",(harga_data[pilih_id]))
                print("Metode Pembayaran : ",metode_pembayaran[pilih_metode])
        else:
            print("PEMBAYARAN TIDAK TERSEDIA")
        mau_diskon=input("APAKAH ANDA INGIN MENGGUNAKAN VOUCHER DISKON 10000?(Y/N)")
        if mau_diskon == "y" or mau_diskon == "Y":
            def diskon (b):
                sesudah_diskon = b - 10000
                return sesudah_diskon
            if pilih_metode in metode_pembayaran:
                print("Nama Penerima : ",dict_trx["nama penerima "])
                print("Alamat Penerima : ",dict_trx["alamat penerima"])
                print("NO HP : ",dict_trx["NO HP"])
                print("Kurir Pengiriman : ",dict_trx["kurir pengiriman"])
                print("Product : ",data[pilih_id])
                print("Harga : ",(diskon(harga_data[pilih_id])))
                print("Metode Pembayaran : ",metode_pembayaran[pilih_metode])
        else:
            print("Nama Penerima : ",dict_trx["nama penerima "])
            print("Alamat Penerima : ",dict_trx["alamat penerima"])
            print("NO HP : ",dict_trx["NO HP"])
            print("Kurir Pengiriman : ",dict_trx["kurir pengiriman"])
            print("Product : ",data[pilih_id])
            print("Harga : ",harga_data[pilih_id])
            print("Metode Pembayaran : ",metode_pembayaran[pilih_metode])

        konfirmasi = input("Apakah anda ingin melakukan Pembayaran ?(Y/N)")
        if konfirmasi == "y" or konfirmasi == "Y":
            print("Anda Berhasil Melakukan Pembayaran")
        else:
            print("Metode pembayaran tidak tersedia")
else:
    print("ID Product tidak tersedia")