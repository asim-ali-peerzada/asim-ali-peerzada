<div align="center">

# Asim Ali
### Backend Engineer — PHP & Laravel · Enterprise Systems · Identity & Workflow Automation

[![Portfolio](https://img.shields.io/badge/Portfolio-asimali.online-EA580C?style=flat-square&logo=safari&logoColor=white)](https://asimali.online)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-the--asimali-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/the-asimali)
[![Resume](https://img.shields.io/badge/Resume-PDF-262626?style=flat-square&logo=adobeacrobatreader&logoColor=white)](https://asimali.online/Asim_Ali_Resume.pdf)
[![Email](https://img.shields.io/badge/Email-asimalipeerzada%40gmail.com-262626?style=flat-square&logo=gmail&logoColor=white)](mailto:asimalipeerzada@gmail.com)

</div>

---

### About

I am a **Backend Engineer** with 3 years of production experience specializing in **PHP and Laravel** (alongside **Python and FastAPI** for AI and automation services). I focus on the server side of operational software: domain modeling, identity and access control, background job pipelines, state machines, and high-throughput data ingestion across telecom, CRM, logistics, workforce, and SaaS domains.

- **Current Role:** Backend Engineer (PHP / Laravel) at **Surfiq Technologies** *(2024 – Present)*
- **Core Focus:** Modular monoliths, centralized OAuth 2.0 / PKCE SSO, hierarchical RBAC & graph-aware ABAC, and resilient background processing.
- **Writing:** [How I Structure a Laravel Application for Long-Term Maintenance](https://asimali.online/blog)

---

### Selected Production Systems & Case Studies

*Most of my production engineering lives inside private enterprise repositories. Full architectural diagrams, database modeling decisions, and implementation deep-dives are documented on [asimali.online](https://asimali.online/#projects).*

| System | Domain & Scale | Core Backend Architecture | Case Study |
| :--- | :--- | :--- | :--- |
| **Close-Out Package (COP) System** | Telecom Field Operations *(Laravel 12 · React 18 · Inertia v2)* | **22 domain modules**, **26 policy classes**, **107 migrations**, and **77 queued jobs** under Laravel Horizon. Stateless **HMAC-SHA256 chunked upload protocol** (5 MB chunks, row-locked finalization) and server-budgeted **Headless Chromium (Browsershot)** PDF rendering for 300+ image telecom deliverables. | [Read Case Study →](https://asimali.online/projects/close-out-package-system) |
| **Enterprise Unified SSO (AuthCenter)** | Centralized IAM & OAuth 2.0 Hub *(Laravel 12 · React 18/19)* | Custom **OAuth 2.0 + PKCE (S256)** authorization server with **RS256 JWT** guards, **TOTP 2FA**, MySQL **JTI token blacklisting**, approval-gated domain access, and **HMAC-SHA256** bidirectional user sync across **7 internal applications**. | [Read Case Study →](https://asimali.online/projects/enterprise-single-sign-on) |
| **CCMS — Enterprise Sales & CRM** | B2B Sales & Territory CRM *(Laravel 11 · React 18)* | **117 migrations** and **5 hierarchy-aware policies** across a 7-tier sales org. Transactional **set-diff territory cascade revocation**, multi-tier revenue target allocation, **`Cache::lock`** sequential quote numbering, Dompdf quote-to-order flows, and **20K+ row chunked Excel imports**. | [Read Case Study →](https://asimali.online/projects/ccms) |
| **Genealogy & Archival SaaS** | Collaborative Family History *(Laravel 12 · React 19)* | **135 migrations** across a multi-service monorepo (`ft-server` + `chat-service`). **5-tier graph-aware ABAC** resolved via **BFS traversal** (`GraphContextService`), unified **NARA & OpenArch** archival search, idempotent **Tesseract OCR + Google Gemini** entity extraction, and Stripe/PayPal billing. | [Read Case Study →](https://asimali.online/projects/genealogy-saas-platform) |
| **Omnichannel AI Assistant** | AI Support & Voice Automation *(FastAPI · Python · React 19)* | Hybrid administrative API + **FastAPI** compute engine. Workspace-scoped **Pinecone vector RAG** ingestion, **Whisper STT → RAG → TTS** voice pipelines, and **Meta WhatsApp Cloud API** webhook routing. | [Read Case Study →](https://asimali.online/projects/ai-assistant-platform) |
| **Samsung 5G Network Migration** | Telecom Provisioning & Hardware *(Laravel 12 · React 19 · .NET)* | Priority-ordered **regex circuit-path extraction engine** with confidence scoring and field provenance tracking across a **48-field / 60+ column** virtualized grid, paired with a **.NET + Brother b-PAC SDK** hardware label-printing bridge. | [Read Case Study →](https://asimali.online/projects/samsung-network-migration) |
| **Shipment Tracker & IMS** | Telecom Supply-Chain Logistics *(Laravel 12 · Blade)* | Unattended **IMAP email ingestion** (`webklex/laravel-imap`) with dual Word/HTML layout parsers, message-ID deduplication, orphan/split shipment reconciliation, per-line quantity ledgers, and a guarded **9-state shipment lifecycle machine**. | [Read Case Study →](https://asimali.online/projects/shipment-tracker-and-ims) |
| **Zametrix Property Intelligence** | Real Estate Analytics SaaS *(Laravel 12 · React 19)* | **17-table multi-snapshot field survey aggregation**, weighted 0–100 side-by-side location comparison scoring, 4-role moderation with OTP partner governance, and automated Dompdf investor dossiers. | [Read Case Study →](https://asimali.online/projects/zametrix) |

---

### Core Engineering Highlights

- **Identity & Access Control:** Custom OAuth 2.0 + PKCE (S256) providers, asymmetric RS256 JWT guards with JTI blacklist revocation, Google Authenticator TOTP 2FA, hierarchical RBAC with subtree cascade revocation, and BFS graph-traversal ABAC (`FamilyAccessMatrix`).
- **Resilient Media & Document Pipelines:** Stateless HMAC-signed resumable chunked uploads (`initiate → chunk → finalize → abort`), server-budgeted Headless Chromium (Browsershot) and Dompdf rendering, and Konva canvas-to-SVG overlay pipelines.
- **High-Throughput Data & Ingestion:** 20K+ row chunked Excel/CSV pipelines with in-memory pre-fetch caches to eliminate per-row N+1 queries, unattended IMAP email parsing, and priority-ranked regex extraction with provenance logging.
- **Concurrency & Stateful Workflows:** Multi-stage finite state machines with rank-guarded transitions, distributed mutex locks (`Cache::lock`) for race-free sequential numbering, and multi-supervisor Laravel Horizon queue isolation.

---

### Technology Stack

| Layer | Technologies & Patterns |
| :--- | :--- |
| **Back-End** | PHP 8.2+, Laravel (11/12), Python, FastAPI, RESTful APIs, Eloquent ORM, Queues & Laravel Horizon, Modular Monoliths, Action / Service / DTO Architecture, State Machines |
| **Database & Caching** | MySQL 8, Redis, Pinecone Vector DB, Schema Design, Query Optimization, Chunked & Cursor Processing, Tagged Cache Invalidation, N+1 Remediation |
| **Security & Auth** | OAuth 2.0 / SSO, PKCE (S256), JWT (RS256), TOTP 2FA, HMAC-SHA256 Webhook Signing, Laravel Sanctum, Spatie Permission, Hierarchical RBAC & Graph ABAC, Gates & Policies |
| **AI & Integrations** | RAG Pipelines, Google Gemini API, Tesseract OCR, Meta WhatsApp Cloud API, Microsoft Graph API, Stripe (Cashier) & PayPal Webhooks, IMAP Parsing, Pusher / WebSockets, Brevo API |
| **Testing & DevOps** | Pest PHP, PHPUnit 11, PHPStan / Larastan, Laravel Pint, Laravel Telescope, Headless Chromium (Browsershot), GitHub Actions (CI/CD), Laravel Sail (Docker), Linux |
| **Front-End** | TypeScript, JavaScript, React (18/19), Inertia.js v2, Laravel Blade, Tailwind CSS, TanStack Query / Table / Virtual, Bootstrap |

---

### Get in Touch

Whether you are hiring for a **Backend Engineering role**, architecting a multi-system SaaS platform, or automating complex operational workflows:

- **Portfolio & Case Studies:** [asimali.online](https://asimali.online)
- **Technical Blog:** [asimali.online/blog](https://asimali.online/blog)
- **LinkedIn:** [linkedin.com/in/the-asimali](https://www.linkedin.com/in/the-asimali)
- **Email:** [asimalipeerzada@gmail.com](mailto:asimalipeerzada@gmail.com)
