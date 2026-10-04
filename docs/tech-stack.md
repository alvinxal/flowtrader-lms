# Tech Stack — Flow Trader LMS

## Stack Utama

| Area | Teknologi | Fungsi |
| --- | --- | --- |
| Frontend | React + Vite + TypeScript | Member, pembelajaran, checkout, dan admin |
| Routing dan data | TanStack Router + TanStack Query | Routing type-safe dan cache API |
| UI dan form | Tailwind, shadcn/ui, React Hook Form, Zod | Tampilan dan validasi |
| Backend | NestJS + Fastify | REST API modular |
| API contract | OpenAPI/Swagger | Dokumentasi dan client frontend |
| Database | PostgreSQL + Drizzle ORM | Data utama dan migration |
| Cache dan queue | Redis + BullMQ | Cache dan background job |
| Authentication | Session cookie + Google OAuth | Login manual dan Google |
| Payment | DOKU Checkout | Checkout dan HTTP Notification |
| Video | Bunny Stream | CDN video, token URL, dan DRM opsional |
| File dan backup | Cloudflare R2 | Sertifikat, gambar, dan backup |
| Email | Resend atau Brevo | Email transaksional |
| Server | Biznet Gio NEO Lite | VPS production Indonesia |
| Deployment | Docker Compose + Caddy + Cloudflare | Container, HTTPS, DNS, dan CDN |
| Monitoring | Uptime Kuma + Sentry | Uptime dan error tracking |

Gunakan versi stabil terbaru. Hindari versi beta, RC, atau canary untuk production.

## Arsitektur

```text
Pengguna
   ↓
Cloudflare
   ↓
Caddy
   ├── React/Vite
   └── NestJS/Fastify API
          ├── PostgreSQL
          ├── Redis/BullMQ
          ├── DOKU
          ├── Bunny Stream
          ├── Cloudflare R2
          └── Email provider
```

Video dikirim langsung oleh Bunny Stream. VPS hanya memeriksa hak akses dan menghasilkan temporary token.

## Struktur Project

```text
flowtrader-lms/
├── apps/
│   ├── web/            # React + Vite
│   └── api/            # NestJS + Fastify
├── packages/
│   ├── contracts/      # Zod dan tipe bersama
│   ├── api-client/     # Client dari OpenAPI
│   ├── database/       # Drizzle schema dan migration
│   ├── ui/
│   └── config/
├── infra/
└── docs/
```

Backend menggunakan modular monolith dengan modul:

- Auth dan users.
- Packages dan courses.
- Orders, payments, dan entitlements.
- Videos dan learning progress.
- Certificates dan communities.
- Notifications, promotions, dan reports.

Controller hanya menangani HTTP. Business rule berada di service dan query database tidak ditulis langsung di controller.

## Keamanan

- Password menggunakan Argon2id.
- Session disimpan dalam cookie `HttpOnly` dan `Secure`.
- Role: `member`, `admin`, dan `owner`.
- Hak akses materi berdasarkan entitlement paket.
- Request perubahan data dilindungi CSRF dan rate limit.
- HTTP Notification DOKU wajib diverifikasi dan idempotent.
- Temporary video token memiliki masa berlaku pendek.
- Watermark identitas member ditampilkan pada player.
- Perubahan penting masuk audit log.

## Infrastruktur Awal

| Resource | Rekomendasi |
| --- | --- |
| VPS | Biznet Gio NEO Lite MM 8.4 |
| CPU | 4 vCPU |
| RAM | 8 GB |
| SSD | 60 GB |
| OS | Ubuntu LTS |
| Lokasi | Indonesia |

Container production:

```text
caddy · web · api · worker · postgres · redis · uptime-kuma
```

Database tidak diekspos ke internet. Backup PostgreSQL dikirim ke R2 dan migration dijalankan sebelum deployment.

## Testing Wajib

- Unit: Vitest untuk frontend dan Jest untuk backend.
- Integration: Jest + Supertest.
- End-to-end: Playwright.
- Contract: validasi OpenAPI.

Alur utama: login, pembayaran DOKU, entitlement, upgrade paket, video token, progress, sertifikat, dan akses admin.

## Tidak Digunakan pada MVP

- Next.js atau TanStack Start.
- Microservices dan Kubernetes.
- Kafka, GraphQL, dan event sourcing.
- Video streaming dari VPS.
- Aplikasi mobile native.

## Referensi

- [NestJS Fastify](https://docs.nestjs.com/techniques/performance)
- [TanStack Router](https://tanstack.com/router/latest/docs/overview)
- [Drizzle PostgreSQL](https://orm.drizzle.team/docs/get-started/postgresql-new)
- [DOKU Checkout](https://developers.doku.com/accept-payments/doku-checkout)
- [Bunny Stream](https://bunny.net/stream-lp/)
- [Biznet Gio Pricelist](https://www.biznetgio.com/pricelist)

_Disusun pada 4 Oktober 2026._
