from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql.cursors, os

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


conn = cursor = None

def bukaDB():
   global conn, cursor
   conn = pymysql.connect(host='localhost',
        user='root',
        password='',
        db='data_barang',
        charset='utf8mb4')
   cursor = conn.cursor()	

def tutupDB():
   global conn, cursor
   cursor.close()
   conn.close()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/barang')
def barang():
    bukaDB()
    container = []
    sql = "SELECT * FROM barang"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        container.append(data)
    tutupDB()
    return render_template('barang.html', container=container)

@app.route('/tambah', methods=['GET','POST'])
def tambah():
    if request.method == 'POST':
        nama_barang = request.form['nama_barang']
        jumlah_barang = request.form['jumlah_barang']
        lokasi_barang = request.form['lokasi_barang']
        harga = request.form['harga']
        keterangan = request.form['keterangan']
        bukaDB()
        sql = "INSERT INTO barang (nama_barang, jumlah_barang, lokasi_barang, harga, keterangan) VALUES(%s, %s, %s, %s, %s)"
        val = (nama_barang, jumlah_barang, lokasi_barang, harga, keterangan)
        cursor.execute(sql, val)
        conn.commit()
        tutupDB()
        flash('Berhasil Menambahkan Data')
        return redirect(url_for('barang'))
    else:
        return render_template('tambah.html')
        
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    bukaDB()
    if request.method == 'POST':
        nama_barang = request.form['nama_barang']
        jumlah_barang = request.form['jumlah_barang']
        lokasi_barang = request.form['lokasi_barang']
        harga = request.form['harga']
        keterangan = request.form['keterangan']
        no = request.form['no']
        sql = "UPDATE barang SET nama_barang=%s, jumlah_barang=%s, lokasi_barang=%s, harga=%s, keterangan=%s WHERE no=%s"
        val = (nama_barang, jumlah_barang, lokasi_barang, harga, keterangan, no)
        cursor.execute(sql, val)
        conn.commit()
        tutupDB()
        flash('Berhasil Mengedit Data')
        return redirect(url_for('barang'))
    else:
        return render_template('barang.html')

@app.route('/hapus/<no>', methods=['GET', 'POST'])
def hapus(no):
    bukaDB()
    cursor.execute("DELETE FROM barang WHERE no=%s",(no))
    conn.commit()
    tutupDB()
    flash('Berhasil Menghapus Data')
    return redirect(url_for('barang'))


@app.route('/karyawan')
def karyawan():
    bukaDB()
    container = []
    sql = "SELECT * FROM karyawan"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        container.append(data)
    tutupDB()
    return render_template('karyawan.html', container=container)

@app.route('/tambah1', methods=['GET','POST'])
def tambah1():
    if request.method == 'POST':
        nama = request.form['nama']
        gender = request.form['gender']
        tanggal_lahir = request.form['tanggal_lahir']
        telp = request.form['telp']
        alamat = request.form['alamat']
        bukaDB()
        sql = "INSERT INTO karyawan (nama, gender, tanggal_lahir, telp, alamat) VALUES(%s, %s, %s, %s, %s)"
        val = (nama, gender, tanggal_lahir, telp, alamat)
        cursor.execute(sql, val)
        conn.commit()
        tutupDB()
        flash('Berhasil Menambahkan Data')
        return redirect(url_for('karyawan'))
    else:
        return render_template('tambah1.html')
        
@app.route('/edit1', methods=['GET', 'POST'])
def edit1():
    bukaDB()
    if request.method == 'POST':
        nama = request.form['nama']
        gender = request.form['gender']
        tanggal_lahir = request.form['tanggal_lahir']
        telp = request.form['telp']
        alamat = request.form['alamat']
        no = request.form['no']
        sql = "UPDATE karyawan SET nama=%s, gender=%s, tanggal_lahir=%s, telp=%s, alamat=%s WHERE no=%s"
        val = (nama, gender, tanggal_lahir, telp, alamat, no)
        cursor.execute(sql, val)
        conn.commit()
        tutupDB()
        flash('Berhasil Mengedit Data')
        return redirect(url_for('karyawan'))
    else:
        return render_template('karyawan.html')

@app.route('/hapus1/<no>', methods=['GET', 'POST'])
def hapus1(no):
    bukaDB()
    cursor.execute("DELETE FROM karyawan WHERE no=%s",(no))
    conn.commit()
    tutupDB()
    flash('Berhasil Menghapus Data')
    return redirect(url_for('karyawan'))

if __name__ == '__main__':
   app.run(debug=True)