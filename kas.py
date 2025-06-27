from db import get_connection

def tambah_transaksi(tanggal, jenis, nominal, deskripsi):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO transaksi (tanggal, jenis, nominal, deskripsi) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (tanggal, jenis, nominal, deskripsi))
    conn.commit()
    conn.close()
    print("Transaksi berhasil ditambahkan.")

def lihat_transaksi():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, tanggal, jenis, nominal, deskripsi FROM transaksi ORDER BY tanggal DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def edit_transaksi(id, tanggal, jenis, nominal, deskripsi):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE transaksi SET tanggal=%s, jenis=%s, nominal=%s, deskripsi=%s WHERE id=%s"
    cursor.execute(sql, (tanggal, jenis, nominal, deskripsi, id))
    conn.commit()
    conn.close()
    print("Transaksi berhasil diupdate.")

def hapus_transaksi(id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM transaksi WHERE id=%s"
    cursor.execute(sql, (id,))
    conn.commit()
    conn.close()
    print("Transaksi berhasil dihapus.")