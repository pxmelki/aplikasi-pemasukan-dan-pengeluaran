from flask import Flask, render_template, request, redirect, url_for
from db import get_connection

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, tanggal, jenis, nominal, deskripsi FROM transaksi ORDER BY tanggal DESC")
    rows = cursor.fetchall()
    conn.close()
    return render_template('index.html', rows=rows)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        tanggal = request.form['tanggal']
        jenis = request.form['jenis']
        nominal = request.form['nominal']
        deskripsi = request.form['deskripsi']
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO transaksi (tanggal, jenis, nominal, deskripsi) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (tanggal, jenis, nominal, deskripsi))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('tambah.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        tanggal = request.form['tanggal']
        jenis = request.form['jenis']
        nominal = request.form['nominal']
        deskripsi = request.form['deskripsi']
        sql = "UPDATE transaksi SET tanggal=%s, jenis=%s, nominal=%s, deskripsi=%s WHERE id=%s"
        cursor.execute(sql, (tanggal, jenis, nominal, deskripsi, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        cursor.execute("SELECT * FROM transaksi WHERE id=%s", (id,))
        data = cursor.fetchone()
        conn.close()
        return render_template('edit.html', data=data)

@app.route('/hapus/<int:id>', methods=['POST'])
def hapus(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transaksi WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)