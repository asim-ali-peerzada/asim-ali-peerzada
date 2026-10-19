<div align="center">

# Asim Ali
**Backend Engineer — PHP & Laravel · Enterprise Systems · Identity & Workflow Automation**

<p>
  <a href="https://asimali.is-a.dev/"><img src="https://img.shields.io/badge/Portfolio-asimali.is--a.dev-EA580C?style=flat-square&logo=safari&logoColor=white" alt="Portfolio" /></a>
  <a href="https://www.linkedin.com/in/the-asimali"><img src="https://img.shields.io/badge/LinkedIn-the--asimali-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://asimali.online/Asim_Ali_Resume.pdf"><img src="https://img.shields.io/badge/Resume-PDF-262626?style=flat-square&logo=adobeacrobatreader&logoColor=white" alt="Resume" /></a>
  <a href="mailto:asimalipeerzada@gmail.com"><img src="https://img.shields.io/badge/Email-asimalipeerzada%40gmail.com-262626?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
</p>

</div>

### About

**Backend Engineer** with 3 years of production experience specializing in **PHP and Laravel** (alongside **Python and FastAPI** for AI and automation services). I build the server-side architecture behind business-critical software: modular monoliths, centralized OAuth 2.0 / PKCE identity hubs, hierarchical RBAC & graph-aware ABAC engines, state machines, and high-throughput data pipelines.

- **Current Role:** Backend Engineer (PHP / Laravel) at **Surfiq Technologies** *(2024 – Present)*
- **Engineering Blog:** [How I Structure a Laravel Application for Long-Term Maintenance →](https://asimali.online/blog)

### Selected Production Systems

*Most of my production engineering lives inside private enterprise repositories. Full architecture diagrams and implementation deep-dives are published on **[asimali.online](https://asimali.online/#projects)**.*

| System | Backend Architecture & Production Scope | Deep Dive |
| :--- | :--- | :---: |
| **Close-Out Package (COP)** | **22 domain modules**, **26 policies**, **107 migrations**, and **77 queued jobs**. Stateless **HMAC-SHA256 chunked upload pipeline** (5 MB chunks, row-locked finalization) and server-budgeted **Headless Chromium** PDF rendering for 300+ image telecom deliverables. | [Case&nbsp;Study&nbsp;↗](https://asimali.online/projects/close-out-package-system) |
| **Enterprise Unified SSO** | Centralized IAM hub across **7 internal applications**. Custom **OAuth 2.0 + PKCE (S256)** server, asymmetric **RS256 JWTs**, **TOTP 2FA**, MySQL **JTI token blacklisting**, approval-gated domain access, and **HMAC-SHA256** bidirectional user sync. | [Case&nbsp;Study&nbsp;↗](https://asimali.online/projects/enterprise-single-sign-on) |
| **CCMS — Enterprise CRM** | **117 migrations** and **5 hierarchy-aware policies** across a 7-tier sales org. Transactional **set-diff territory cascade revocation**, multi-tier budget cascade math, **`Cache::lock`** sequential quote numbering, Dompdf quote-to-order flows, and **20K+ row chunked imports**. | [Case&nbsp;Study&nbsp;↗](https://asimali.online/projects/ccms) |
| **Genealogy & Archival SaaS** | **135 migrations** across a multi-service monorepo (`ft-server` + `chat-service`). **5-tier graph-aware ABAC** via **BFS traversal** (`GraphContextService`), unified **NARA & OpenArch** search, idempotent **Tesseract OCR + Gemini** extraction, and Stripe/PayPal billing. | [Case&nbsp;Study&nbsp;↗](https://asimali.online/projects/genealogy-saas-platform) |
| **Omnichannel AI Assistant** | Hybrid operational API + **FastAPI** intelligence engine. Workspace-scoped **Pinecone vector RAG** ingestion, **Whisper STT → RAG → TTS** voice pipelines, and **Meta WhatsApp Cloud API** webhook routing. | [Case&nbsp;Study&nbsp;↗](https://asimali.online/projects/ai-assistant-platform) |
| **Samsung 5G Migration** | Priority-ordered **regex circuit-path extraction engine** with confidence scoring and field provenance tracking across a **48-field / 60+ column** virtualized grid, paired with a **.NET + Brother SDK** hardware label-printing bridge. | [Case&nbsp;Study&nbsp;↗](https://asimali.online/projects/samsung-network-migration) |
| **Shipment Tracker & IMS** | Unattended **IMAP email ingestion** with dual Word/HTML layout parsers, message-ID deduplication, orphan/split shipment reconciliation, 10-column quantity ledgers, and a guarded **9-state shipment lifecycle machine**. | [Case&nbsp;Study&nbsp;↗](https://asimali.online/projects/shipment-tracker-and-ims) |
| **Zametrix PropTech SaaS** | **17-table multi-snapshot field survey aggregation**, weighted 0–100 side-by-side location comparison scoring, 4-role moderation with OTP partner governance, and automated investor PDF dossiers. | [Case&nbsp;Study&nbsp;↗](https://asimali.online/projects/zametrix) |

### Core Engineering Patterns

- **Identity & Access Control:** Custom OAuth 2.0 + PKCE (S256) providers, RS256 JWT guards with JTI blacklist revocation, TOTP 2FA, hierarchical RBAC with subtree cascade revocation, and BFS graph-traversal ABAC (`FamilyAccessMatrix`).
- **Resilient Media & Document Pipelines:** Stateless HMAC-signed resumable chunked uploads (`initiate → chunk → finalize → abort`), server-budgeted Headless Chromium (Browsershot) and Dompdf rendering, and Konva canvas-to-SVG overlay pipelines.
- **High-Throughput Data & Ingestion:** 20K+ row chunked Excel/CSV pipelines with in-memory pre-fetch caches to eliminate per-row N+1 queries, unattended IMAP email parsing, and priority-ranked regex extraction with provenance logging.
- **Concurrency & Stateful Workflows:** Finite state machines with rank-guarded transitions, distributed mutex locks (`Cache::lock`) for race-free sequential numbering, and multi-supervisor Laravel Horizon queue isolation.

### Technology Stack

| Layer | Technologies & Architectural Patterns |
| :--- | :--- |
| **Back-End** | `PHP` · `Laravel` · `Python` · `FastAPI` · `REST APIs` · `Eloquent ORM` · `Queues & Horizon` · `Modular Monoliths` · `State Machines` |
| **Database & Performance** | `MySQL 8` · `Redis` · `Pinecone Vector DB` · `Query Optimization` · `Chunked & Cursor Processing` · `Tagged Caching` · `N+1 Remediation` |
| **Security & Auth** | `OAuth 2.0 / SSO` · `PKCE (S256)` · `JWT (RS256)` · `TOTP 2FA` · `HMAC-SHA256` · `Sanctum` · `Spatie Permission` · `RBAC & Graph ABAC` |
| **AI & Integrations** | `RAG Pipelines` · `Google Gemini API` · `Tesseract OCR` · `WhatsApp Cloud API` · `Microsoft Graph API` · `Stripe & PayPal` · `IMAP Parsing` · `Pusher / SSE` |
| **Testing & DevOps** | `Pest PHP` · `PHPUnit 11` · `PHPStan / Larastan` · `Laravel Telescope` · `Headless Chromium (Browsershot)` · `GitHub Actions (CI/CD)` · `Linux` |
| **Front-End** | `TypeScript` · `JavaScript` · `React 18/19` · `Inertia.js v2` · `Laravel Blade` · `Tailwind CSS` · `TanStack Query / Table / Virtual` |

### Get in Touch

Open to **Backend Engineering roles**, system architecture consulting, and complex workflow automation projects:

- **Portfolio & Case Studies:** [asimali.online](https://asimali.online) · **Blog:** [asimali.online/blog](https://asimali.online/blog)
- **LinkedIn:** [linkedin.com/in/the-asimali](https://www.linkedin.com/in/the-asimali) · **Email:** [asimalipeerzada@gmail.com](mailto:asimalipeerzada@gmail.com)
