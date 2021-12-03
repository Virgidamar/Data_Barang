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
        id_user = request.form['id_user']
        nama_lengkap = request.form['nama_lengkap']
        password = request.form['password']
        no_telp = request.form['no_telp']
        email = request.form['email']
        tempat_lahir = request.form['tempat_lahir']
        tanggal_lahir = request.form['tanggal_lahir']
        jenis_kelamin = request.form['jenis_kelamin']
        alamat = request.form['alamat']
        provinsi = request.form['provinsi']
        kabupaten_kota = request.form['kabupaten_kota']
        id_jabatan = request.form['id_jabatan']
        id_projek = request.form['id_projek']
        bukaDB()
        sql = "INSERT INTO karyawan (id_user, nama_lengkap, password, no_telp, email, tempat_lahir, tanggal_lahir, jenis_kelamin, alamat, provinsi, kabupaten_kota, id_jabatan, id_projek) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (id_user, nama_lengkap, password, no_telp, email, tempat_lahir, tanggal_lahir, jenis_kelamin, alamat, provinsi, kabupaten_kota, id_jabatan, id_projek)
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
        id_user = request.form['id_user']
        nama_lengkap = request.form['nama_lengkap']
        password = request.form['password']
        no_telp = request.form['no_telp']
        email = request.form['email']
        tempat_lahir = request.form['tempat_lahir']
        tanggal_lahir = request.form['tanggal_lahir']
        jenis_kelamin = request.form['jenis_kelamin']
        alamat = request.form['alamat']
        provinsi = request.form['provinsi']
        kabupaten_kota = request.form['kabupaten_kota']
        id_jabatan = request.form['id_jabatan']
        id_projek = request.form['id_projek']
        no = request.form['no']
        sql = "UPDATE karyawan SET id_user=%s, nama_lengkap=%s, password=%s, no_telp=%s, email=%s, tempat_lahir=%s, tanggal_lahir=%s, jenis_kelamin=%s, alamat=%s, provinsi=%s, kabupaten_kota=%s, id_jabatan=%s, id_projek=%s WHERE no=%s"
        val = (id_user, nama_lengkap, password, no_telp, email, tempat_lahir, tanggal_lahir, jenis_kelamin, alamat, provinsi, kabupaten_kota, id_jabatan, id_projek, no)
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