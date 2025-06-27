import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Ganti sesuai user MySQL kamu
        password="",  # Ganti sesuai password MySQL kamu
        database="buku_kas"  # Pastikan sudah membuat database ini di MySQL
    )