# Buku Kas Keuangan Pribadi

Aplikasi sederhana untuk mencatat pemasukan dan pengeluaran, baik melalui web (Flask) maupun CLI (terminal).

## Instalasi

1. Clone repo ini:
   ```
   git clone https://github.com/pxmelki/aplikasi-pemasukan-dan-pengeluaran.git
   cd buku-kas
   ```

2. Install dependensi:
   ```
   pip install -r requirements.txt
   ```

3. Setup database MySQL:
   - Buat database `buku_kas`
   - Jalankan SQL berikut:
     ```sql
     CREATE TABLE transaksi (
         id INT AUTO_INCREMENT PRIMARY KEY,
         tanggal DATE,
         jenis VARCHAR(20),
         nominal FLOAT,
         deskripsi VARCHAR(255)
     );
     ```
   - Pastikan user/password database di `db.py` sudah sesuai.

## Menjalankan aplikasi

### Mode Web (Flask):
```
python app.py
```
Akses di browser: http://localhost:5000

### Mode CLI:
```
python main.py
```

## Struktur Folder

- `app.py` : aplikasi web
- `main.py` : aplikasi CLI
- `kas.py` : logic transaksi
- `db.py` : koneksi DB
- `templates/` : file HTML
- `static/` : file CSS (dan JS bila ada)

---

Author: MelkiCode
