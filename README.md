# flowtrader-lms

Dokumentasi perencanaan LMS FlowTrader.

| Dokumen | Isi |
| --- | --- |
| `docs/company-context.md` | Analisis landing page FlowTrader: produk, harga, kurikulum, funnel, kebijakan, dan celah yang perlu dibereskan |
| `docs/feature-list.md` | Daftar fitur MVP dan pembagian fitur wajib atau tambahan |
| `docs/user-flow.md` | Alur member, skenario free tier dan pembeli, serta alur owner. Diagram ada di `docs/user-flow.drawio` |
| `docs/tech-stack.md` | Pilihan teknologi, arsitektur, keamanan, dan pengujian |
| `docs/daftar-modul-dan-harga.md` | Halaman penawaran untuk client: 14 modul, total proyek, dan paket managed service |
| `docs/estimasi-infrastruktur-100-member.md` | Estimasi biaya server, video, dan bandwidth |

## Dokumen untuk Client

`docs/daftar-modul-dan-harga.md` adalah satu-satunya dokumen yang diserahkan ke client. Versi PDF dibuat dari markdown itu:

```bash
python3 tools/md-to-pdf.py docs/daftar-modul-dan-harga.md docs/daftar-modul-dan-harga.pdf
```

Butuh Google Chrome atau Chromium. Tidak ada dependency Python tambahan.

## Keputusan yang Masih Menunggu Client

- Kanal pembayaran tunggal. Landing page sekarang memakai Mayar, LMS memakai DOKU.
- Kelengkapan materi video dan durasi kurikulum BAB 1–2 Flow Basic.
- Perbaikan landing page: gambar placeholder, testimoni dobel, dan catatan internal yang bocor ke halaman publik.