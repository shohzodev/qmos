# O'zgarishlar tarixi

## 1.2 — 2026-11-02

Faqat qo'shimchalar: 1.0 va 1.1 yuboruvchilari o'zgarishsiz ishlayveradi.

- Yangi hodisa turi `site.supervisors`: obyektning texnik nazoratchilari ro'yxati (to'liq nusxa, eng so'nggisi
  amal qiladi). Har biri: `supervisor_id`, `role` (`customer_supervisor` / `state_inspector`), `full_name`,
  `phone`, ixtiyoriy `position`, `organization`. Ro'yxatda `supervisor_id` va `phone` noyob (mazmun tekshiruvi).
- Nazoratchi markazga telefon va o'zi o'rnatgan PIN bilan kiradi; `state_inspector` markaz tasdiqlagunicha
  baho qo'ya olmaydi.

## 1.1 — 2026-11-02

Faqat qo'shimchalar: 1.0 yuboruvchilari o'zgarishsiz ishlayveradi (`spec_version` "1.0" ham qabul qilinadi).

- Yangi hodisa turi `site.daily_report_retracted`: yuboruvchi tizimda butunlay o'chirilgan kunlik hisobotni
  bekor qilish. `data`: `date`, majburiy `reason`; `supersedes` majburiy va joriy hisobotga havola qiladi.
  Kunlik hisobot oilasi (`site.daily_report`, `site.daily_report_retracted`) `supersedes` orqali bir-birini
  almashtira oladi; boshqa turlar uchun qoida o'zgarmagan (bir xil `event_type`).
- `site.daily_report` ga ixtiyoriy `attachments`: dalillar (rasm, yashirin ishlar akti, laboratoriya xulosasi,
  geodezik s'yomka, sertifikat) `media_id` + `sha256` bilan, ixtiyoriy `item_id`, `captured_at`, `location`, `note`.
- `POST /v1/media`: `application/pdf` qo'shildi.
- `GET /v1/approvals`: texnik nazoratchi baholari (`role`: `customer_supervisor` / `state_inspector`,
  `inspector_position`, `superseded`); javob sxemasi `approvals-result.json`.
- Kutubxona: `SPEC_VERSIONS`, `KUNLIK_HISOBOT_OILASI`; yangi mazmun tekshiruvlari (dalil takrori,
  dalil vaqti, bekor qilish sanasi).

## 1.0 — 2026-10-05

Birinchi versiya.

- Hodisa konverti: `event_id` (idempotentlik), `supersedes` (tuzatish),
  `organization.stir`, `site_id`.
- Hodisa turlari: `site.profile`, `site.status`, `site.work_plan`,
  `site.daily_report`, `site.photo`, `site.incident`.
- API: `POST /v1/events` (1–500 hodisa), `POST /v1/media`, `GET /v1/ping`.
- HMAC-SHA256 imzo, 300 soniyalik vaqt chegarasi.
- Python kutubxonasi: `hodisa_xatolari`, `sign_request`, `imzoni_tekshir`.
