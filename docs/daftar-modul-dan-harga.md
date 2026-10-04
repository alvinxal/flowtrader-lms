# Daftar Modul dan Estimasi Harga — Flow Trader LMS

> **Total proyek: Rp14.500.000 (sekali bayar). Pengerjaan 4–8 minggu setelah brief dan materi siap.**

Platform LMS untuk 3 tier — **Free**, **Flow Basic**, dan **Flow Trader Mastery**. Video seumur hidup untuk paket berbayar, akses Discord berbatas waktu sesuai kebijakan, lengkap dengan checkout, progres belajar, sertifikat, dan panel admin. Harga di bawah adalah total proyek, bukan harga satuan jika modul dikerjakan terpisah.

## Daftar Modul

| No. | Modul | Ruang Lingkup | Harga |
| ---: | --- | --- | ---: |
| 1 | Katalog dan Penawaran Paket | Halaman publik Free, Basic & Mastery, detail manfaat dan kurikulum, harga dan tombol beli, pengaturan paket tayang/tidak tayang | Rp700.000 |
| 2 | Autentikasi dan Profil | Daftar dan login manual serta login Google, profil (nama, email, no HP, akun Discord), lupa password, pengaturan sesi, Free Plan (bisa login dan melihat kurikulum terkunci), hak akses member dan admin | Rp1.100.000 |
| 3 | Checkout, Pembayaran, dan Pesanan | Checkout via DOKU, pencatatan pesanan dan status transaksi, akses aktif otomatis setelah bayar, email konfirmasi + link ke platform | Rp1.400.000 |
| 4 | Membership dan Hak Akses | Cek akses member panel, Free terkunci dari materi dan link Discord dengan prompt upgrade, halaman Paket Saya dan riwayat pembelian, video seumur hidup, atur/buka-tutup akses oleh admin, materi Mastery terkunci untuk Basic, upgrade Free ke Basic/Mastery dan Basic ke Mastery | Rp1.200.000 |
| 5 | LMS dan Progres Belajar | Dashboard belajar, struktur paket → kelas → bab → video, navigasi materi, progres dan status selesai, lanjut dari video terakhir | Rp1.400.000 |
| 6 | Video Aman | Video streaming aman anti-download, link sementara yang kedaluwarsa, akses sesuai paket, watermark nama member di player | Rp1.500.000 |
| 7 | Sertifikat Digital | Sertifikat terbit otomatis setelah semua materi selesai, tercantum nama member dan paket, nomor sertifikat, bisa diunduh, template diatur admin | Rp700.000 |
| 8 | Komunitas dan Masa Berlaku | Pengaturan link Discord, link hanya muncul untuk member paket aktif, pelacakan masa berlaku akses sesuai kebijakan | Rp700.000 |
| 9 | Notifikasi dan Onboarding | Welcome screen setelah pembelian, notifikasi di dalam platform, pusat notifikasi dengan status baca/belum, admin bisa buat dan kirim notifikasi | Rp700.000 |
| 10 | Admin Konten dan Produk | Atur paket dan harga, kelola kelas/bab/video dan urutannya, atur tayang/tidak tayang, atur materi terkunci, kelola link komunitas dan template sertifikat | Rp1.400.000 |
| 11 | Admin Member dan Transaksi | Daftar dan cari member, lihat kepemilikan paket, daftar pembelian dan status transaksi, beri/cabut akses, filter data, ekspor CSV/Excel | Rp1.100.000 |
| 12 | Promosi dan Ringkasan Penjualan | Atur popup promo dan jadwal tayangnya, ringkasan jumlah transaksi dan omzet per paket, filter laporan per periode | Rp700.000 |
| 13 | Setup Aplikasi, Keamanan, dan Pengujian | Setup database dan API, konfigurasi aplikasi dan environment, keamanan dasar dan validasi input, audit log, penanganan error, testing alur utama, dokumentasi | Rp900.000 |
| 14 | Infrastruktur dan Deployment | Server Biznet Gio NEO Lite (4 CPU, 8 GB RAM, 60 GB SSD), setup seluruh aplikasi di server dengan Docker, domain + SSL + Cloudflare, database PostgreSQL + Redis, backup ke Cloudflare R2, monitoring uptime dan error tracking | Rp1.000.000 |
|  | **Total 14 modul — sudah mencakup semua fitur MVP** |  | **Rp14.500.000** |

VPS development gratis 1 bulan pertama (ditanggung kami). Setelah platform live, VPS ditanggung kami bila memakai managed service, atau ditanggung klien bila tidak.

Estimasi pengerjaan **4–8 minggu** tergantung kelengkapan materi video dan kecepatan feedback.

## Paket Managed Service (Opsional, Setelah Launch)

Penyiapan server dan sistem ada di Modul 14 (sekali bayar). Managed Service di bawah adalah biaya operasional bulanan setelah platform live. VPS ditanggung kami di kedua paket. Biaya video streaming selalu ditanggung klien dan ditagih terpisah.

| Paket Layanan | Managed Basic | Managed Plus |
| --- | --- | --- |
| Server aplikasi + database | ✓ | ✓ |
| SSL & domain | ✓ | ✓ |
| Monitoring uptime & resource | ✓ | ✓ |
| Update keamanan | ✓ | ✓ |
| Perbaikan bug fitur yang sudah ada | ✓ | ✓ |
| Bantuan kendala akses member (login, akses paket belum terbuka) | ✓ | ✓ |
| Backup | Database mingguan | Harian |
| Monitoring transaksi | - | ✓ |
| Bantuan kelola data member (koreksi data profil, akun ganda, beri/cabut akses manual) | - | ✓ |
| Update paket/harga/promo/notifikasi | - | ✓ |
| Laporan bulanan | Sistem | Sistem & transaksi |
| Prioritas penanganan | - | ✓ |
| Bantuan ringan | 3x/bulan | 8x/bulan |
| Waktu respon | Maksimal 1 hari kerja | 4–8 jam kerja |
| Jam dukungan | Hari & jam kerja | Hari & jam kerja |
| **Harga** | **Rp1.000.000/bulan** | **Rp1.500.000/bulan** |

**Rekomendasi untuk Flow Trader: Managed Plus** — lebih aman untuk transaksi harian dan pengelolaan data member.

### Termasuk di Managed Service

- 1 server production untuk aplikasi dan database (hingga 1.000 akun terdaftar, termasuk akun gratis)
- SSL, konfigurasi domain, monitoring uptime & error
- Backup otomatis (mingguan di Basic, harian di Plus)
- Update keamanan dan dependency

Jika pemakaian melebihi kapasitas (storage, member, atau bandwidth), upgrade server akan didiskusikan terpisah.

### Contoh Bantuan Ringan

Ganti harga/deskripsi paket, ganti link komunitas, ubah teks/gambar, atur popup promo dan notifikasi, bantu kendala akses member, penyesuaian kecil tampilan.

## Belum Termasuk

### Infrastruktur

- Biaya video streaming (Bunny Stream) mengikuti pemakaian: pemakaian normal sekitar **Rp265.000–Rp272.000/bulan** (kira-kira 50–70 member aktif yang menonton rata-rata 6–8 jam/bulan), selalu ditanggung klien. Akun Bunny Stream dibuat atas nama klien sejak awal, jadi tagihannya langsung ke klien tanpa lewat kami
- Biaya pihak ketiga: domain, payment gateway (DOKU untuk LMS dan Mayar untuk landing page), email transaksional
- Upgrade server bila pemakaian melebihi kapasitas (storage, member, atau bandwidth), didiskusikan terpisah

### Selain Infrastruktur

- Fitur atau modul baru di luar daftar di atas
- Desain ulang atau perubahan alur besar
- Integrasi layanan pihak ketiga baru
- Migrasi data dalam jumlah besar
- Aplikasi Android/iOS
- Sinkronisasi role Discord otomatis

Pekerjaan di luar kuota: **Rp150.000 per jam** setelah ada persetujuan.

## Ketentuan

- Biaya implementasi: **Rp14.500.000**
- Managed service: **Rp1.000.000/bulan (Basic)** atau **Rp1.500.000/bulan (Plus)**, minimum kontrak **12 bulan**, tagihan per 3 bulan atau tahunan di muka
- Platform berupa aplikasi web responsif (bisa diakses di HP & desktop), bukan aplikasi native
