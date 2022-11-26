import os
import mysql.connector
from prettytable import PrettyTable

def koneksi():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "perpustakaan"
    )

def hapusTampilan():
    os.system('cls' if os.name == 'nt' else 'clear')

#Buku
def tampilkanBuku():
    db = koneksi()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM buku")
    results = cursor.fetchall()
    
    table = PrettyTable()
    table.field_names = ["ID", "Judul Buku", "Penulis", "Penerbit", "Tahun Terbit"]
    for data in results:
        table.add_row(data)

    print(table)

def tambahBuku(judul, penulis, penerbit, tahunterbit):
    db = koneksi()
    cursor = db.cursor()
    sql = "INSERT INTO buku(judul, penulis, penerbit, tahun_terbit) VALUES (%s, %s, %s, %s);"
    val = (judul, penulis, penerbit, tahunterbit)
    cursor.execute(sql,val)
    db.commit()

    return cursor.rowcount

def editBuku(idbuku, judul, penulis, penerbit, tahunterbit):
    db = koneksi()
    cursor = db.cursor()
    sql = "UPDATE buku SET judul = %s, penulis = %s, penerbit = %s, tahun_terbit = %s where id_buku = %s"
    val = (judul, penulis, penerbit, tahunterbit, idbuku)
    cursor.execute(sql,val)
    db.commit()

    return cursor.rowcount

def hapusBuku(id):
    db = koneksi()
    cursor = db.cursor()
    sql = "DELETE FROM buku where id_buku = %s"
    val = (id,)
    cursor.execute(sql,val)
    db.commit()
    return cursor.rowcount

def cariBuku(nama):
    db = koneksi()
    cursor = db.cursor()
    sql = "SELECT * FROM buku WHERE judul Like %s"
    val = ("%" + nama + "%",)
    cursor.execute(sql,val)
    results = cursor.fetchall()
    
    table = PrettyTable()
    table.field_names = ["ID", "Judul Buku", "Penulis", "Penerbit", "Tahun Terbit"]
    for data in results:
        table.add_row(data)

    print(table)

def menuBuku():
    while True:
        hapusTampilan()
        print("Sub Menu Buku")

        table = PrettyTable()
        table.field_names = ["No.", "Menu Buku"]
        menu = [
            "Tambah Buku",
            "Tampil Buku",
            "Edit Buku",
            "Hapus Buku",
            "Cari Buku",
            "Exit"
        ]
        i = 1
        for v in menu:
            table.add_row([i, v])
            i = i + 1

        print(table)

        pilih = input("Masukan pilihan anda : ")

        if pilih == "1":
            hapusTampilan()
            print("Tambah Buku dalam Perpustakaan ini")

            judul = input("Masukan Judul: ")
            penulis = input("Masukan Penulis: ")
            penerbit = input("Masukan Penerbit: ")
            tahunterbit = input("Masukan Tahun Terbit: ")
            jumlah = tambahBuku(judul, penulis, penerbit, tahunterbit)
            print("{} Buku Berhasil Ditambahkan".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "2":
            hapusTampilan()
            print("Buku dalam Perpustakaan ini")
            tampilkanBuku()
            while True:
                back = input("kembali [y/n]")
                if back == "y" or back == "Y":
                    break
                else:
                    hapusTampilan()
                    print("Buku dalam Perpustakaan ini")
                    tampilkanBuku()

        elif pilih == "3":
            hapusTampilan()
            print("Buku dalam Perpustakaan ini")
            tampilkanBuku()
            idbuku = int(input("ID buku berapa yang akan diubah : "))
            judul = input("Masukan Judul: ")
            penulis = input("Masukan Penulis: ")
            penerbit = input("Masukan Penerbit: ")
            tahunterbit = input("Masukan Tahun Terbit: ")
            jumlah = editBuku(idbuku, judul, penulis, penerbit, tahunterbit)
            print("{} Buku Berhasil Diubah".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "4":
            hapusTampilan()
            print("Buku dalam Perpustakaan ini")
            tampilkanBuku()
            idbuku = int(input("ID buku berapa yang akan dihapus : "))
            jumlah = hapusBuku(idbuku)
            print("{} Buku Berhasil Dihapus".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "5":
            hapusTampilan()
            cari = input("Nama buku yang dicari: ")
            cariBuku(cari)
            input("Tekan apa saja untuk kembali")

        elif pilih == "6":
            break
        else:
            continue
#Pengunjung
        
def tampilkanPengunjung():
    db = koneksi()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM pengunjung")
    results = cursor.fetchall()
    
    table = PrettyTable()
    table.field_names = ["ID", "Nama", "Jenis Kelamin", "No HP", "Alamat"]
    for data in results:
        table.add_row(data)

    print(table)

def tambahPengunjung(nama, kelamin, nohp, alamat):
    db = koneksi()
    cursor = db.cursor()
    sql = "INSERT INTO pengunjung(nama, jenis_kelamin, no_hp, alamat) VALUES (%s, %s, %s, %s);"
    val = (nama, kelamin, nohp, alamat)
    cursor.execute(sql,val)
    db.commit()

    return cursor.rowcount

def editPengunjung(idpengunjung, nama, kelamin, nohp, alamat):
    db = koneksi()
    cursor = db.cursor()
    sql = "UPDATE pengunjung SET nama = %s, jenis_kelamin = %s, no_hp = %s, alamat = %s where id_pengunjung = %s"
    val = (nama, kelamin, nohp, alamat, idpengunjung)
    cursor.execute(sql,val)
    db.commit()

    return cursor.rowcount

def hapusPengunjung(id):
    db = koneksi()
    cursor = db.cursor()
    sql = "DELETE FROM pengunjung where id_pengunjung = %s"
    val = (id,)
    cursor.execute(sql,val)
    db.commit()
    return cursor.rowcount

def cariPengunjung(nama):
    db = koneksi()
    cursor = db.cursor()
    sql = "SELECT * FROM pengunjung WHERE nama Like %s"
    val = ("%" + nama + "%",)
    cursor.execute(sql,val)
    results = cursor.fetchall()
    
    table = PrettyTable()
    table.field_names = ["ID", "Nama", "Jenis Kelamin", "No HP", "Alamat"]
    for data in results:
        table.add_row(data)

    print(table)

def menuPengunjung():
    while True:
        hapusTampilan()
        print("Sub Menu Pengunjung")

        table = PrettyTable()
        table.field_names = ["No.", "Menu Pengunjung"]
        menu = [
            "Tambah Pengunjung",
            "Tampil Pengunjung",
            "Edit Pengunjung",
            "Hapus Pengunjung",
            "Cari Pengunjung",
            "Exit"
        ]
        i = 1
        for v in menu:
            table.add_row([i, v])
            i = i + 1

        print(table)

        pilih = input("Masukan pilihan anda : ")

        if pilih == "1":
            hapusTampilan()
            print("Tambah Pengunjung dalam Perpustakaan ini")

            nama = input("Masukan nama: ")
            print("Jenis Kelamin")
            print("1. Laki laki")
            print("2. Perempuan")
            kelamin = int(input("Masukan jenis kelamin: "))
            kelamin = "Laki laki" if kelamin == 1 else "Perempuan"
            nohp = input("Masukan no hp : ")
            alamat = input("Masukan alamat : ")
            jumlah = tambahPengunjung(nama, kelamin, nohp, alamat)
            print("{} Pengunjung Berhasil Ditambahkan".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "2":
            hapusTampilan()
            print("Pengunjung dalam Perpustakaan ini")
            tampilkanPengunjung()
            while True:
                back = input("kembali [y/n]")
                if back == "y" or back == "Y":
                    break
                else:
                    hapusTampilan()
                    print("Pengunjung dalam Perpustakaan ini")
                    tampilkanPengunjung()

        elif pilih == "3":
            hapusTampilan()
            print("Pengunjung dalam Perpustakaan ini")
            tampilkanPengunjung()
            idpengunjung = int(input("ID pengunjung berapa yang akan diubah : "))
            nama = input("Masukan nama: ")
            print("Jenis Kelamin")
            print("1. Laki laki")
            print("2. Perempuan")
            kelamin = int(input("Masukan jenis kelamin: "))
            kelamin = "Laki laki" if kelamin == 1 else "Perempuan"
            nohp = input("Masukan no hp : ")
            alamat = input("Masukan alamat : ")
            jumlah = editPengunjung(idpengunjung, nama, kelamin, nohp, alamat)
            print("{} Pengunjung Berhasil Diubah".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "4":
            hapusTampilan()
            print("Pengunjung dalam Perpustakaan ini")
            tampilkanPengunjung()
            idpengunjung = int(input("ID Pengunjung berapa yang akan dihapus : "))
            jumlah = hapusPengunjung(idpengunjung)
            print("{} Pengunjung Berhasil Dihapus".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "5":
            hapusTampilan()
            cari = input("Nama Pengunjung yang dicari: ")
            cariPengunjung(cari)
            input("Tekan apa saja untuk kembali")

        elif pilih == "6":
            break
        else:
            continue
#Pegawai
        
def tampilkanPegawai():
    db = koneksi()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM pegawai")
    results = cursor.fetchall()
    
    table = PrettyTable()
    table.field_names = ["ID", "Nama", "Jenis Kelamin", "No HP", "Jadwal", "Alamat"]
    for data in results:
        table.add_row(data)

    print(table)

def tambahPegawai(nama, kelamin, nohp, jadwal, alamat):
    db = koneksi()
    cursor = db.cursor()
    sql = "INSERT INTO pegawai(nama, jenis_kelamin, no_hp, jadwal, alamat) VALUES (%s, %s, %s, %s, %s);"
    val = (nama, kelamin, nohp, jadwal, alamat)
    cursor.execute(sql,val)
    db.commit()

    return cursor.rowcount

def editPegawai(idpegawai, nama, kelamin, nohp, jadwal, alamat):
    db = koneksi()
    cursor = db.cursor()
    sql = "UPDATE pegawai SET nama = %s, jenis_kelamin = %s, no_hp = %s, jadwal = %s, alamat = %s where id_pegawai = %s"
    val = (nama, kelamin, nohp, jadwal, alamat, idpegawai)
    cursor.execute(sql,val)
    db.commit()

    return cursor.rowcount

def hapusPegawai(id):
    db = koneksi()
    cursor = db.cursor()
    sql = "DELETE FROM pegawai where id_pegawai = %s"
    val = (id,)
    cursor.execute(sql,val)
    db.commit()
    return cursor.rowcount

def cariPegawai(nama):
    db = koneksi()
    cursor = db.cursor()
    sql = "SELECT * FROM pegawai WHERE nama Like %s"
    val = ("%" + nama + "%",)
    cursor.execute(sql,val)
    results = cursor.fetchall()
    
    table = PrettyTable()
    table.field_names = ["ID", "Nama", "Jenis Kelamin", "No HP", "Jadwal", "Alamat"]
    for data in results:
        table.add_row(data)

    print(table)

def menuPegawai():
    while True:
        hapusTampilan()
        print("Sub Menu Pegawai")

        table = PrettyTable()
        table.field_names = ["No.", "Menu Pegawai"]
        menu = [
            "Tambah Pegawai",
            "Tampil Pegawai",
            "Edit Pegawai",
            "Hapus Pegawai",
            "Cari Pegawai",
            "Exit"
        ]
        i = 1
        for v in menu:
            table.add_row([i, v])
            i = i + 1

        print(table)

        pilih = input("Masukan pilihan anda : ")

        if pilih == "1":
            hapusTampilan()
            print("Tambah Pegawai dalam Perpustakaan ini")

            nama = input("Masukan nama: ")
            print("Jenis Kelamin")
            print("1. Laki laki")
            print("2. Perempuan")
            kelamin = int(input("Masukan jenis kelamin: "))
            kelamin = "Laki laki" if kelamin == 1 else "Perempuan"
            nohp = input("Masukan no hp : ")
            jadwal = input("Masukan jadwal : ")
            alamat = input("Masukan alamat : ")
            jumlah = tambahPegawai(nama, kelamin, nohp, jadwal, alamat)
            print("{} Pegawai Berhasil Ditambahkan".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "2":
            hapusTampilan()
            print("Pegawai dalam Perpustakaan ini")
            tampilkanPegawai()
            while True:
                back = input("kembali [y/n]")
                if back == "y" or back == "Y":
                    break
                else:
                    hapusTampilan()
                    print("Pegawai dalam Perpustakaan ini")
                    tampilkanPegawai()

        elif pilih == "3":
            hapusTampilan()
            print("Pegawai dalam Perpustakaan ini")
            tampilkanPegawai()
            idpegawai = int(input("ID pegawai berapa yang akan diubah : "))
            nama = input("Masukan nama: ")
            print("Jenis Kelamin")
            print("1. Laki laki")
            print("2. Perempuan")
            kelamin = int(input("Masukan jenis kelamin: "))
            kelamin = "Laki laki" if kelamin == 1 else "Perempuan"
            nohp = input("Masukan no hp : ")
            jadwal = input("Masukan jadwal : ")
            alamat = input("Masukan alamat : ")
            jumlah = editPegawai(idpegawai, nama, kelamin, nohp, jadwal, alamat)
            print("{} Pegawai Berhasil Diubah".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "4":
            hapusTampilan()
            print("Pegawai dalam Perpustakaan ini")
            tampilkanPegawai()
            idpegawai = int(input("ID Pegawai berapa yang akan dihapus : "))
            jumlah = hapusPegawai(idpegawai)
            print("{} Pegawai Berhasil Dihapus".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "5":
            hapusTampilan()
            cari = input("Nama Pegawai yang dicari: ")
            cariPegawai(cari)
            input("Tekan apa saja untuk kembali")

        elif pilih == "6":
            break
        else:
            continue
#Jenis Denda
        
def tampilkanJenisDenda():
    db = koneksi()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM jenis_denda")
    results = cursor.fetchall()
    
    table = PrettyTable()
    table.field_names = ["ID", "Jenis Denda", "Harga"]
    for data in results:
        table.add_row(data)

    print(table)

def tambahJenisDenda(jenis, harga):
    db = koneksi()
    cursor = db.cursor()
    sql = "INSERT INTO jenis_denda(jenis_denda, harga_denda) VALUES (%s, %s);"
    val = (jenis, harga)
    cursor.execute(sql,val)
    db.commit()

    return cursor.rowcount

def editJenisDenda(idjenisdenda, jenis, harga):
    db = koneksi()
    cursor = db.cursor()
    sql = "UPDATE jenis_denda SET jenis_denda = %s, harga_denda = %s where id_jenis_denda = %s"
    val = (jenis, harga, idjenisdenda)
    cursor.execute(sql,val)
    db.commit()

    return cursor.rowcount

def hapusJenisDenda(id):
    db = koneksi()
    cursor = db.cursor()
    sql = "DELETE FROM jenis_denda where id_jenis_denda = %s"
    val = (id,)
    cursor.execute(sql,val)
    db.commit()
    return cursor.rowcount

def cariJenisDenda(nama):
    db = koneksi()
    cursor = db.cursor()
    sql = "SELECT * FROM jenis_denda WHERE jenis_denda Like %s"
    val = ("%" + nama + "%",)
    cursor.execute(sql,val)
    results = cursor.fetchall()
    
    table = PrettyTable()
    table.field_names = ["ID", "Jenis Denda", "Harga"]
    for data in results:
        table.add_row(data)

    print(table)

def menuJenisDenda():
    while True:
        hapusTampilan()
        print("Sub Menu Jenis Denda")

        table = PrettyTable()
        table.field_names = ["No.", "Menu Jenis Denda"]
        menu = [
            "Tambah Jenis Denda",
            "Tampil Jenis Denda",
            "Edit Jenis Denda",
            "Hapus Jenis Denda",
            "Cari Jenis Denda",
            "Exit"
        ]
        i = 1
        for v in menu:
            table.add_row([i, v])
            i = i + 1

        print(table)

        pilih = input("Masukan pilihan anda : ")

        if pilih == "1":
            hapusTampilan()
            print("Tambah Jenis Denda dalam Perpustakaan ini")

            jenis = input("Masukan jenis denda : ")
            harga = input("Masukan harga : ")

            jumlah = tambahJenisDenda(jenis, harga)
            print("{} Jenis Denda Berhasil Ditambahkan".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "2":
            hapusTampilan()
            print("Jenis Denda dalam Perpustakaan ini")
            tampilkanJenisDenda()
            while True:
                back = input("kembali [y/n]")
                if back == "y" or back == "Y":
                    break
                else:
                    hapusTampilan()
                    print("Jenis Denda dalam Perpustakaan ini")
                    tampilkanJenisDenda()

        elif pilih == "3":
            hapusTampilan()
            print("Jenis Denda dalam Perpustakaan ini")
            tampilkanJenisDenda()
            idjenisdenda = int(input("ID jenis denda berapa yang akan diubah : "))
            
            jenis = input("Masukan jenis denda : ")
            harga = input("Masukan harga : ")

            jumlah = editJenisDenda(idjenisdenda, jenis, harga)
            print("{} Jenis Denda Berhasil Diubah".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "4":
            hapusTampilan()
            print("Jenis Denda dalam Perpustakaan ini")
            tampilkanJenisDenda()
            idjenisdenda = int(input("ID jenis denda berapa yang akan dihapus : "))
            jumlah = hapusJenisDenda(idjenisdenda)
            print("{} Jenis Denda Berhasil Dihapus".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "5":
            hapusTampilan()
            cari = input("Nama Jenis Denda yang dicari: ")
            cariJenisDenda(cari)
            input("Tekan apa saja untuk kembali")

        elif pilih == "6":
            break
        else:
            continue

#Denda
def tampilkanDenda():
    db = koneksi()
    cursor = db.cursor()
    cursor.execute("SELECT pengunjung.nama, jenis_denda.jenis_denda, jenis_denda.harga_denda, buku.judul from denda JOIN pengunjung ON denda.id_pengunjung = pengunjung.id_pengunjung JOIN buku ON denda.id_buku = buku.id_buku JOIN jenis_denda ON denda.id_jenis_denda = jenis_denda.id_jenis_denda")
    results = cursor.fetchall()
    
    table = PrettyTable()
    table.field_names = ["Nama", "Jenis Denda", "Harga", "Judul Buku"]
    for data in results:
        table.add_row(data)

    print(table)

def tambahDenda(buku, jenis, pengunjung):
    db = koneksi()
    cursor = db.cursor()
    sql = "INSERT INTO denda(id_buku, id_jenis_denda, id_pengunjung) VALUES (%s, %s, %s);"
    val = (buku, jenis, pengunjung)
    cursor.execute(sql,val)
    db.commit()

    return cursor.rowcount

def editDenda(iddenda, buku, jenis, pengunjung):
    db = koneksi()
    cursor = db.cursor()
    sql = "UPDATE denda SET id_buku = %s, id_jenis_denda = %s, id_pengunjung = %s where id_denda = %s"
    val = (buku, jenis, pengunjung, iddenda)
    cursor.execute(sql,val)
    db.commit()

    return cursor.rowcount

def hapusDenda(id):
    db = koneksi()
    cursor = db.cursor()
    sql = "DELETE FROM denda where id_denda = %s"
    val = (id,)
    cursor.execute(sql,val)
    db.commit()
    return cursor.rowcount

def menuDenda():
    while True:
        hapusTampilan()
        print("Sub Menu Denda")

        table = PrettyTable()
        table.field_names = ["No.", "Menu Denda"]
        menu = [
            "Tambah Denda",
            "Tampil Denda",
            "Edit Denda",
            "Hapus Denda",
            "Exit"
        ]
        i = 1
        for v in menu:
            table.add_row([i, v])
            i = i + 1

        print(table)

        pilih = input("Masukan pilihan anda : ")

        if pilih == "1":
            hapusTampilan()
            print("Tambah Denda dalam Perpustakaan ini")

            tampilkanPengunjung()
            pengunjung = input("Masukan ID pengunjung : ")
            
            hapusTampilan()
            tampilkanBuku()
            buku = input("Masukan ID buku : ")

            hapusTampilan()
            tampilkanJenisDenda()
            jenis = input("Masukan ID jenis denda : ")

            jumlah = tambahDenda(buku, jenis, pengunjung)
            print("{} Denda Berhasil Ditambahkan".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "2":
            hapusTampilan()
            print("Denda dalam Perpustakaan ini")
            tampilkanDenda()
            while True:
                back = input("kembali [y/n]")
                if back == "y" or back == "Y":
                    break
                else:
                    hapusTampilan()
                    print("Denda dalam Perpustakaan ini")
                    tampilkanDenda()

        elif pilih == "3":
            hapusTampilan()
            print("Denda dalam Perpustakaan ini")
            tampilkanDenda()
            iddenda = int(input("ID denda berapa yang akan diubah : "))
            
            tampilkanPengunjung()
            pengunjung = input("Masukan ID pengunjung : ")
            
            hapusTampilan()
            tampilkanBuku()
            buku = input("Masukan ID buku : ")

            hapusTampilan()
            tampilkanDenda()
            jenis = input("Masukan ID jenis denda : ")

            jumlah = editDenda(iddenda, buku, jenis, pengunjung)
            print("{} Denda Berhasil Diubah".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "4":
            hapusTampilan()
            print("Denda dalam Perpustakaan ini")
            tampilkanDenda()

            iddenda = int(input("ID denda berapa yang akan dihapus : "))
            jumlah = hapusDenda(iddenda)

            print("{} Denda Berhasil Dihapus".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "5":
            break
        else:
            continue

# Peminjaman
def tampilkanPeminjaman():
    db = koneksi()
    cursor = db.cursor()
    cursor.execute("SELECT pengunjung.nama as nama_pengunjung, pegawai.nama as nama_pegawai, buku.judul, peminjaman.tanggal_kembali, peminjaman.tanggal_pinjam from peminjaman JOIN buku ON peminjaman.id_buku = buku.id_buku JOIN pegawai ON peminjaman.id_pegawai = pegawai.id_pegawai JOIN pengunjung ON peminjaman.id_pengunjung = pengunjung.id_pengunjung")
    results = cursor.fetchall()
    
    table = PrettyTable()
    table.field_names = ["Nama Pengunjung", "Nama Pegawai", "Judul Buku", "Tanggal Kembali", "Tanggal Pinjam"]
    for data in results:
        table.add_row(data)

    print(table)

def tambahPeminjaman(buku, pegawai, pengunjung, pinjam, kembali):
    db = koneksi()
    cursor = db.cursor()
    sql = "INSERT INTO peminjaman(id_buku, id_pegawai, id_pengunjung, tanggal_pinjam, tanggal_kembali) VALUES (%s, %s, %s, %s, %s);"
    val = (buku, pegawai, pengunjung, pinjam, kembali)
    cursor.execute(sql,val)
    db.commit()

    return cursor.rowcount

def editPeminjaman(idpeminjaman, pegawai, pengunjung, pinjam, kembali):
    db = koneksi()
    cursor = db.cursor()
    sql = "UPDATE peminjaman SET id_buku = %s, id_pegawai = %s, id_pengunjung = %s, tanggal_pinjam = %s, tanggal_kembali = %s where id_peminjaman = %s"
    val = (pegawai, pengunjung, pinjam, kembali, idpeminjaman)
    cursor.execute(sql,val)
    db.commit()

    return cursor.rowcount

def hapusPeminjaman(id):
    db = koneksi()
    cursor = db.cursor()
    sql = "DELETE FROM peminjaman where id_peminjaman = %s"
    val = (id,)
    cursor.execute(sql,val)
    db.commit()
    return cursor.rowcount

def menuPeminjaman():
    while True:
        hapusTampilan()
        print("Sub Menu Peminjaman")

        table = PrettyTable()
        table.field_names = ["No.", "Menu Peminjaman"]
        menu = [
            "Tambah Peminjaman",
            "Tampil Peminjaman",
            "Edit Peminjaman",
            "Hapus Peminjaman",
            "Exit"
        ]
        i = 1
        for v in menu:
            table.add_row([i, v])
            i = i + 1

        print(table)

        pilih = input("Masukan pilihan anda : ")

        if pilih == "1":
            hapusTampilan()
            print("Tambah Peminjaman dalam Perpustakaan ini")

            tampilkanPengunjung()
            pengunjung = input("Masukan ID pengunjung : ")
            
            hapusTampilan()
            tampilkanBuku()
            buku = input("Masukan ID buku : ")

            hapusTampilan()
            tampilkanPegawai()
            pegawai = input("Masukan ID pegawai : ")

            hapusTampilan()
            pinjam = input("Masukan tanggal pinjam : ")
            kembali = input("Masukan tanggal kembali : ")

            jumlah = tambahPeminjaman(buku, pegawai, pengunjung, pinjam, kembali)
            print("{} Peminjaman Berhasil Ditambahkan".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "2":
            hapusTampilan()
            print("Peminjaman dalam Perpustakaan ini")
            tampilkanPeminjaman()
            while True:
                back = input("kembali [y/n]")
                if back == "y" or back == "Y":
                    break
                else:
                    hapusTampilan()
                    print("Peminjaman dalam Perpustakaan ini")
                    tampilkanPeminjaman()

        elif pilih == "3":
            hapusTampilan()
            print("Peminjaman dalam Perpustakaan ini")
            tampilkanPeminjaman()
            idpeminjaman = int(input("ID peminjaman berapa yang akan diubah : "))
            
            tampilkanPengunjung()
            pengunjung = input("Masukan ID pengunjung : ")
            
            hapusTampilan()
            tampilkanBuku()
            buku = input("Masukan ID buku : ")

            hapusTampilan()
            tampilkanPegawai()
            pegawai = input("Masukan ID pegawai : ")

            hapusTampilan()
            pinjam = input("Masukan tanggal pinjam : ")
            kembali = input("Masukan tanggal kembali : ")

            jumlah = editPeminjaman(idpeminjaman, pegawai, pengunjung, pinjam, kembali)
            print("{} Peminjaman Berhasil Diubah".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "4":
            hapusTampilan()
            print("Peminjaman dalam Perpustakaan ini")
            tampilkanPeminjaman()

            idpeminjaman = int(input("ID peminjaman berapa yang akan dihapus : "))
            jumlah = hapusPeminjaman(idpeminjaman)

            print("{} Peminjaman Berhasil Dihapus".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "5":
            break
        else:
            continue

#Pengembalian
def tampilkanPengembalian():
    db = koneksi()
    cursor = db.cursor()
    cursor.execute("SELECT pengunjung.nama as nama_pengunjung, pegawai.nama as nama_pegawai, buku.judul, pengembalian.tanggal_kembali from pengembalian JOIN buku ON pengembalian.id_buku = buku.id_buku JOIN pegawai ON pengembalian.id_pegawai = pegawai.id_pegawai JOIN pengunjung ON pengembalian.id_pengunjung = pengunjung.id_pengunjung")
    results = cursor.fetchall()
    
    table = PrettyTable()
    table.field_names = ["Nama Pengunjung", "Nama Pegawai", "Judul Buku", "Tanggal Kembali"]
    for data in results:
        table.add_row(data)

    print(table)

def tambahPengembalian(buku, pegawai, pengunjung, kembali):
    db = koneksi()
    cursor = db.cursor()
    sql = "INSERT INTO pengembalian(id_buku, id_pegawai, id_pengunjung, tanggal_kembali) VALUES (%s, %s, %s, %s);"
    val = (buku, pegawai, pengunjung, kembali)
    cursor.execute(sql,val)
    db.commit()

    return cursor.rowcount

def editPengembalian(idpengembalian, pegawai, pengunjung, kembali):
    db = koneksi()
    cursor = db.cursor()
    sql = "UPDATE pengembalian SET id_buku = %s, id_pegawai = %s, id_pengunjung = %s, tanggal_kembali = %s where id_pengembalian = %s"
    val = (pegawai, pengunjung, kembali, idpengembalian)
    cursor.execute(sql,val)
    db.commit()

    return cursor.rowcount

def hapusPengembalian(id):
    db = koneksi()
    cursor = db.cursor()
    sql = "DELETE FROM pengembalian where id_pengembalian = %s"
    val = (id,)
    cursor.execute(sql,val)
    db.commit()
    return cursor.rowcount

def menuPengembalian():
    while True:
        hapusTampilan()
        print("Sub Menu Pengembalian")

        table = PrettyTable()
        table.field_names = ["No.", "Menu Pengembalian"]
        menu = [
            "Tambah Pengembalian",
            "Tampil Pengembalian",
            "Edit Pengembalian",
            "Hapus Pengembalian",
            "Exit"
        ]
        i = 1
        for v in menu:
            table.add_row([i, v])
            i = i + 1

        print(table)

        pilih = input("Masukan pilihan anda : ")

        if pilih == "1":
            hapusTampilan()
            print("Tambah Pengembalian dalam Perpustakaan ini")

            tampilkanPengunjung()
            pengunjung = input("Masukan ID pengunjung : ")
            
            hapusTampilan()
            tampilkanBuku()
            buku = input("Masukan ID buku : ")

            hapusTampilan()
            tampilkanPegawai()
            pegawai = input("Masukan ID pegawai : ")

            hapusTampilan()
            kembali = input("Masukan tanggak kembali : ")

            jumlah = tambahPengembalian(buku, pegawai, pengunjung, kembali)
            print("{} Pengembalian Berhasil Ditambahkan".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "2":
            hapusTampilan()
            print("Pengembalian dalam Perpustakaan ini")
            tampilkanPengembalian()
            while True:
                back = input("kembali [y/n]")
                if back == "y" or back == "Y":
                    break
                else:
                    hapusTampilan()
                    print("Pengembalian dalam Perpustakaan ini")
                    tampilkanPengembalian()

        elif pilih == "3":
            hapusTampilan()
            print("Pengembalian dalam Perpustakaan ini")
            tampilkanPengembalian()
            idpengembalian = int(input("ID pengembalian berapa yang akan diubah : "))
            
            tampilkanPengunjung()
            pengunjung = input("Masukan ID pengunjung : ")
            
            hapusTampilan()
            tampilkanBuku()
            buku = input("Masukan ID buku : ")

            hapusTampilan()
            tampilkanPegawai()
            pegawai = input("Masukan ID pegawai : ")

            hapusTampilan()
            kembali = input("Masukan tanggak kembali : ")

            jumlah = editPengembalian(idpengembalian, pegawai, pengunjung, kembali)
            print("{} Pengembalian Berhasil Diubah".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "4":
            hapusTampilan()
            print("Pengembalian dalam Perpustakaan ini")
            tampilkanPengembalian()

            idpengembalian = int(input("ID pengembalian berapa yang akan dihapus : "))
            jumlah = hapusPengembalian(idpengembalian)

            print("{} Pengembalian Berhasil Dihapus".format(jumlah))
            input("Tekan apa saja untuk kembali")

        elif pilih == "5":
            break
        else:
            continue

if __name__ == "__main__":
    while True:
        hapusTampilan()
        print("Aplikasi Peminjaman Perpustakaan".upper())

        table = PrettyTable()
        table.field_names = ["No.", "Daftar Menu"]
        menu = [
            "Buku",
            "Pengunjung",
            "Pegawai",
            "Denda",
            "Jenis Denda",
            "Peminjaman",
            "Pengembalian",
            "Exit"
        ]
        i = 1
        for v in menu:
            table.add_row([i, v])
            i = i + 1

#Main Menu
        print(table)

        pilih = input("Masukan pilihan kamu : ")

        if pilih == "1":
            menuBuku()

        elif pilih == "2":
            menuPengunjung()

        elif pilih == "3":
            menuPegawai()

        elif pilih == "4":
            menuDenda()

        elif pilih == "5":
            menuJenisDenda()

        elif pilih == "6":
            menuPeminjaman()

        elif pilih == "7":
            menuPengembalian()

        elif pilih == "8":
            print("Aplikasi berhenti")
            break

        else:
            continue