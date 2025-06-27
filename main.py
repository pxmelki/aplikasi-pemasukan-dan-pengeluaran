from kas import tambah_transaksi, lihat_transaksi, edit_transaksi, hapus_transaksi

def menu():
    while True:
        print("\n=== Buku Kas Keuangan Pribadi ===")
        print("1. Tambah Transaksi")
        print("2. Lihat Transaksi")
        print("3. Edit Transaksi")
        print("4. Hapus Transaksi")
        print("5. Keluar")
        pilih = input("Pilih menu (1-5): ")

        if pilih == "1":
            tanggal = input("Tanggal (YYYY-MM-DD): ")
            jenis = input("Jenis (pemasukan/pengeluaran): ")
            nominal = float(input("Nominal: "))
            deskripsi = input("Deskripsi: ")
            tambah_transaksi(tanggal, jenis, nominal, deskripsi)
        elif pilih == "2":
            rows = lihat_transaksi()
            print("\nID | Tanggal | Jenis | Nominal | Deskripsi")
            for row in rows:
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
        elif pilih == "3":
            id = int(input("ID transaksi yang akan diedit: "))
            tanggal = input("Tanggal baru (YYYY-MM-DD): ")
            jenis = input("Jenis baru (pemasukan/pengeluaran): ")
            nominal = float(input("Nominal baru: "))
            deskripsi = input("Deskripsi baru: ")
            edit_transaksi(id, tanggal, jenis, nominal, deskripsi)
        elif pilih == "4":
            id = int(input("ID transaksi yang akan dihapus: "))
            hapus_transaksi(id)
        elif pilih == "5":
            print("Terima kasih!")
            break
        else:
            print("Menu tidak valid!")

if __name__ == "__main__":
    menu()