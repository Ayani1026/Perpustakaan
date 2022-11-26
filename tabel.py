import mysql.connector
import time

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

print("Loading...")

cursor = db.cursor()
cursor.execute("CREATE DATABASE perpustakaan")
cursor.close()

time.sleep(5)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "perpustakaan"
)

cursor = db.cursor()
sql = """
CREATE TABLE `buku` (
  `id_buku` int(11) NOT NULL AUTO_INCREMENT,
  `judul` varchar(255) NOT NULL,
  `penulis` varchar(255) NOT NULL,
  `penerbit` varchar(255) NOT NULL,
  `tahun_terbit` int(11) NOT NULL,
  PRIMARY KEY (`id_buku`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- OK

CREATE TABLE `pegawai` (
  `id_pegawai` int(11) NOT NULL AUTO_INCREMENT,
  `nama` varchar(255) NOT NULL,
  `jenis_kelamin` varchar(255) NOT NULL,
  `no_hp` int(15) NOT NULL,
  `jadwal` DATETIME NOT NULL,
  `alamat` text,
  PRIMARY KEY (`id_pegawai`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- OK

CREATE TABLE `jenis_denda` (
  `id_jenis_denda` int(11) NOT NULL AUTO_INCREMENT,
  `jenis_denda` varchar(255) NOT NULL,
  `harga_denda` int(15) NOT NULL,
  PRIMARY KEY (`id_jenis_denda`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- OK

CREATE TABLE `pengunjung` (
  `id_pengunjung` int(11) NOT NULL AUTO_INCREMENT,
  `nama` varchar(255) NOT NULL,
  `jenis_kelamin` varchar(255) NOT NULL,
  `no_hp` varchar(255) NOT NULL,
  `alamat` text NOT NULL,
  PRIMARY KEY (`id_pengunjung`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
--OK
"""
cursor.execute(sql)
cursor.close()

time.sleep(5)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "perpustakaan"
)

cursor = db.cursor()
sql = """
CREATE TABLE `denda` (
  `id_denda` int(11) NOT NULL AUTO_INCREMENT,
  `id_buku` int,
  `id_jenis_denda` int,
  `id_pengunjung` int,
  PRIMARY KEY (`id_denda`),
  
  KEY `FK_denda_id_buku` (`id_buku`),
  KEY `FK_denda_id_jenis_denda` (`id_jenis_denda`),
  KEY `FK_denda_id_pengunjung` (`id_pengunjung`),
  CONSTRAINT `FK_denda_id_buku` FOREIGN KEY (`id_buku`) REFERENCES `buku` (`id_buku`),
  CONSTRAINT `FK_denda_id_jenis_denda` FOREIGN KEY (`id_jenis_denda`) REFERENCES `jenis_denda` (`id_jenis_denda`),
  CONSTRAINT `FK_denda_id_pengunjung` FOREIGN KEY (`id_pengunjung`) REFERENCES `pengunjung` (`id_pengunjung`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- OK

CREATE TABLE `pengembalian` (
  `id_pengembalian` int(11) NOT NULL AUTO_INCREMENT,
  `id_buku` int(11) NOT NULL,
  `id_pegawai` int(11) NOT NULL,
  `id_pengunjung` int(11) NOT NULL,
  `tanggal_kembali` datetime NOT NULL,
  PRIMARY KEY (`id_pengembalian`),
  KEY `FK_pengembalian_id_buku` (`id_buku`),
  KEY `FK_pengembalian_id_pegawai` (`id_pegawai`),
  KEY `FK_pengembalian_id_pengunjung` (`id_pengunjung`),
  CONSTRAINT `FK_pengembalian_id_buku` FOREIGN KEY (`id_buku`) REFERENCES `buku` (`id_buku`),
  CONSTRAINT `FK_pengembalian_id_pegawai` FOREIGN KEY (`id_pegawai`) REFERENCES `pegawai` (`id_pegawai`),
  CONSTRAINT `FK_pengembalian_id_pengunjung` FOREIGN KEY (`id_pengunjung`) REFERENCES `pengunjung` (`id_pengunjung`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- OK


CREATE TABLE `peminjaman` (
  `id_peminjaman` int(11) NOT NULL AUTO_INCREMENT,
  `id_buku` int(11) NOT NULL,
  `id_pegawai` int(11) NOT NULL,
  `id_pengunjung` int(11) NOT NULL,
  `tanggal_pinjam` datetime NOT NULL,
  `tanggal_kembali` datetime NOT NULL,
  PRIMARY KEY (`id_peminjaman`),
  KEY `FK_peminjaman_id_buku` (`id_buku`),
  KEY `FK_peminjaman_id_pegawai` (`id_pegawai`),
  KEY `FK_peminjaman_id_pengunjung` (`id_pengunjung`),
  CONSTRAINT `FK_peminjaman_id_buku` FOREIGN KEY (`id_buku`) REFERENCES `buku` (`id_buku`),
  CONSTRAINT `FK_peminjaman_id_pegawai` FOREIGN KEY (`id_pegawai`) REFERENCES `pegawai` (`id_pegawai`),
  CONSTRAINT `FK_peminjaman_id_pengunjung` FOREIGN KEY (`id_pengunjung`) REFERENCES `pengunjung` (`id_pengunjung`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- OK

"""
cursor.execute(sql)
cursor.close()

print("OKE !")