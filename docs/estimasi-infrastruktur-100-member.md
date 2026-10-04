# Estimasi Infrastruktur — 100 Member

## Ringkasan

| Komponen | Rekomendasi |
| --- | --- |
| Member terdaftar | 100 akun |
| Member aktif bulanan | 50–70 akun |
| Akun gratis (belum membeli paket) | tidak dihitung sebagai member aktif |
| Pengguna bersamaan | 5–10; lonjakan maksimal 15 |
| VPS | Biznet Gio NEO Lite MM 8.4 |
| Video | Bunny Stream Standard Asia |
| Biaya normal | **Rp704.000–Rp801.000/bulan** |

Kurs acuan: **Rp17.898/USD**, berdasarkan JISDOR Bank Indonesia tanggal 2 Oktober 2026 (hari kerja terakhir).

## VPS

| Resource | Kapasitas | Harga |
| --- | ---: | ---: |
| CPU | 4 vCPU |  |
| RAM | 8 GB |  |
| SSD | 60 GB |  |
| Bandwidth | Unlimited sesuai ketentuan provider |  |
| VPS | Biznet Gio NEO Lite MM 8.4 | Rp269.000/bulan |
| Snapshot 60 GB | Rp1.500/GB | Rp90.000/bulan |

Kapasitas ini cukup untuk React, NestJS, worker, PostgreSQL, Redis, dan monitoring. Video tidak melewati VPS.

## Video

Asumsi normal:

- Katalog sekitar 16 jam.
- 400 jam tontonan per bulan.
- Rata-rata transfer 1,2 GB per jam.
- Total delivery sekitar 480 GB per bulan.

| Komponen Bunny Stream | Estimasi |
| --- | ---: |
| Penyimpanan 40–80 GB | Rp7.200–Rp14.300 |
| Delivery 480 GB | ±Rp258.000 |
| **Total video normal** | **±Rp265.000–Rp272.000/bulan** |

### Bunny Stream vs Cloudflare Stream

| Provider | Estimasi Normal | Catatan |
| --- | ---: | --- |
| **Bunny Stream** | **±Rp269.000/bulan** | Lebih ekonomis; token auth dan DRM opsional |
| Cloudflare Stream | ±Rp519.000/bulan | Harga per menit lebih mudah diprediksi |

Bunny Stream dipilih karena lebih ekonomis. Watermark identitas pengguna dibuat sebagai overlay aplikasi.

## Biaya Bulanan Normal

| Komponen | Estimasi |
| --- | ---: |
| VPS Biznet Gio | Rp269.000 |
| Snapshot VPS | Rp90.000 |
| Bunny Stream | Rp269.000 |
| Backup R2 | Rp0–Rp10.000 |
| Email | Rp0 |
| Cloudflare | Rp0 |
| Domain | Rp10.000–Rp25.000 |
| Cadangan kurs/pemakaian | Rp70.000–Rp135.000 |
| **Total** | **Rp704.000–Rp801.000/bulan** |

Biaya transaksi DOKU tidak termasuk karena mengikuti perjanjian merchant. Landing page saat ini memakai Mayar, jadi biaya transaksi dari kanal Mayar juga di luar estimasi ini.

## Skenario Pemakaian

| Skenario | Jam Tonton | Delivery Video | Total Infrastruktur |
| --- | ---: | ---: | ---: |
| Rendah | 200 jam | 240 GB | Rp525.000–Rp675.000 |
| Normal | 400 jam | 480 GB | Rp700.000–Rp825.000 |
| Tinggi | 800 jam | 960 GB | Rp900.000–Rp1.100.000 |

## Managed Service

| Paket | Harga | Batas Video | Sisa pada Pemakaian Normal |
| --- | ---: | ---: | ---: |
| Managed Basic | Rp1.000.000 | 250 GB/bulan | Rp199.000–Rp296.000 |
| Managed Plus | Rp1.500.000 | 500 GB/bulan | Rp699.000–Rp796.000 |

Kelebihan bandwidth video ditagihkan sesuai pemakaian. Biaya transaksi DOKU selalu di luar paket.

## Kapan Harus Upgrade?

Upgrade VPS jika pengguna bersamaan melebihi 25, RAM di atas 75%, CPU di atas 60%, API p95 di atas 500 ms, atau queue/database mulai penuh. Upgrade berikutnya: **8 vCPU dan RAM 16 GB**.

## Referensi Harga

- [Biznet Gio Pricelist](https://www.biznetgio.com/pricelist)
- [Bunny Pricing](https://bunny.net/pricing)
- [Cloudflare Stream Pricing](https://developers.cloudflare.com/stream/pricing/)
- [Cloudflare R2 Pricing](https://developers.cloudflare.com/r2/pricing/)
- [JISDOR Bank Indonesia](https://www.bi.go.id/id/statistik/informasi-kurs/jisdor/default.aspx)

_Estimasi per 4 Oktober 2026._
