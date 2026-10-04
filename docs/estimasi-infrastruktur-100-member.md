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
| Biaya normal (tanggungan kami) | **Rp439.000–Rp529.000/bulan** |
| Biaya video (tanggungan klien) | **±Rp265.000–Rp272.000/bulan** |

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

Biaya video streaming selalu ditanggung klien dan ditagih terpisah dari managed service. Akun Bunny Stream dibuat atas nama klien sejak awal.

| Komponen | Estimasi | Ditanggung |
| --- | --- | --- |
| VPS Biznet Gio | Rp269.000 | Kami (lewat managed service) |
| Snapshot VPS | Rp90.000 | Kami (lewat managed service) |
| Backup R2 | Rp0–Rp10.000 | Kami (lewat managed service) |
| Email | Rp0 | Kami (lewat managed service) |
| Cloudflare | Rp0 | Kami (lewat managed service) |
| Domain | Rp10.000–Rp25.000 | Kami (lewat managed service) |
| Cadangan kurs/pemakaian | Rp70.000–Rp100.000 | Kami (lewat managed service) |
| **Total tanggungan kami** | **Rp439.000–Rp529.000/bulan** |  |
| Bunny Stream (video) | ±Rp265.000–Rp272.000 | **Klien, tagihan langsung** |

Biaya transaksi DOKU tidak termasuk karena mengikuti perjanjian merchant. Landing page saat ini memakai Mayar, jadi biaya transaksi dari kanal Mayar juga di luar estimasi ini.

## Skenario Pemakaian

| Skenario | Member Aktif (perkiraan) | Jam Tonton | Delivery Video | Biaya Video (klien) | Tanggungan Kami |
| --- | ---: | ---: | ---: | ---: | ---: |
| Rendah | 25–35 member | 200 jam | 240 GB | Rp135.000–Rp145.000 | Rp439.000–Rp529.000 |
| Normal | 50–70 member | 400 jam | 480 GB | Rp265.000–Rp272.000 | Rp439.000–Rp529.000 |
| Tinggi | 100 member | 800 jam | 960 GB | Rp520.000–Rp540.000 | Rp439.000–Rp529.000 |

Perkiraan member aktif mengasumsikan rata-rata 6–8 jam tonton per member per bulan; skenario Tinggi berarti seluruh 100 akun aktif dan menonton sekitar 8 jam/bulan.

## Managed Service

| Paket | Harga | Tanggungan Kami | Sisa pada Pemakaian Normal |
| --- | ---: | ---: | ---: |
| Managed Basic | Rp1.000.000 | Rp439.000–Rp529.000 | Rp471.000–Rp561.000 |
| Managed Plus | Rp1.500.000 | Rp439.000–Rp529.000 | Rp971.000–Rp1.061.000 |

Biaya video streaming selalu di luar paket dan ditagih langsung ke klien. Biaya transaksi DOKU juga selalu di luar paket.

## Kapan Harus Upgrade?

Upgrade VPS jika pengguna bersamaan melebihi 25, RAM di atas 75%, CPU di atas 60%, API p95 di atas 500 ms, atau queue/database mulai penuh. Upgrade berikutnya: **8 vCPU dan RAM 16 GB**.

## Referensi Harga

- [Biznet Gio Pricelist](https://www.biznetgio.com/pricelist)
- [Bunny Pricing](https://bunny.net/pricing)
- [Cloudflare Stream Pricing](https://developers.cloudflare.com/stream/pricing/)
- [Cloudflare R2 Pricing](https://developers.cloudflare.com/r2/pricing/)
- [JISDOR Bank Indonesia](https://www.bi.go.id/id/statistik/informasi-kurs/jisdor/default.aspx)

_Estimasi per 4 Oktober 2026._
