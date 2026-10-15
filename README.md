
# Asim Ali
### Backend Engineer | PHP, Laravel & Enterprise Systems

I build backend systems for complex business workflows, specializing in **PHP, Laravel, identity and access control, data processing, and workflow automation**. I also use **Python and FastAPI** for AI-powered features and automation services.

[Portfolio](https://asimali.online) · [LinkedIn](https://www.linkedin.com/in/the-asimali) · [Resume](https://asimali.online/Asim_Ali_Resume.pdf) · [Email](mailto:asimalipeerzada@gmail.com)

---

## About Me

I'm a Backend Engineer at **Surfiq Technologies**, working on production software that goes beyond conventional CRUD applications.

My work focuses on designing systems that handle complex business rules, fine-grained permissions, asynchronous processing, and large-scale data operations. I pay particular attention to security boundaries, concurrency, data consistency, failure recovery, and long-term maintainability.

I document selected projects, architecture decisions, and engineering practices on my [portfolio](https://asimali.online/#projects) and [engineering blog](https://asimali.online/blog).

## Selected Projects

Most of these systems are maintained in private enterprise repositories. The case studies below describe their architecture, key implementation decisions, and engineering challenges.

### 1. Close-Out Package (COP)
[View Case Study](https://asimali.online/projects/close-out-package-system)

A document-generation and delivery system for telecom infrastructure projects.

- Structured the application around **22 domain modules**, 26 authorization policies, and 107 database migrations.
- Developed a resumable upload pipeline using HMAC-SHA256 signatures, 5 MB chunks, and row-locked finalization.
- Implemented server-budgeted Headless Chromium rendering for deliverables containing 300+ images.
- Used 77 queued jobs to support asynchronous processing.

**Key areas:** Modular architecture, secure uploads, queue processing, PDF generation.

### 2. Enterprise Unified SSO
[View Case Study](https://asimali.online/projects/enterprise-single-sign-on)

A centralized identity service connecting seven internal applications.

- Implemented OAuth 2.0 authorization with PKCE (S256) and RS256-signed JWTs.
- Added TOTP-based two-factor authentication and JTI-based token revocation.
- Built approval-gated domain access and bidirectional user synchronization secured with HMAC-SHA256.

**Key areas:** Identity architecture, authentication security, token lifecycle management, cross-application integration.

### 3. CCMS — Enterprise CRM
[View Case Study](https://asimali.online/projects/ccms)

A CRM supporting a seven-tier sales organization, territory-based permissions, and multi-level financial workflows.

- Designed hierarchy-aware authorization and transactional territory-revocation logic.
- Implemented cascading budget calculations and concurrency-safe quote numbering with Laravel's `Cache::lock`.
- Built quote-to-order workflows and chunked imports processing more than 20,000 rows.

**Key areas:** Complex business rules, authorization hierarchies, concurrency control, data-intensive workflows.

### 4. Genealogy & Archival SaaS
[View Case Study](https://asimali.online/projects/genealogy-saas-platform)

A multi-service platform for family history research, archival discovery, and document extraction.

- Implemented five-level graph-aware access control using breadth-first search (BFS).
- Integrated NARA and OpenArch search sources.
- Built an idempotent document-extraction pipeline combining Tesseract OCR and Gemini.
- Integrated Stripe and PayPal billing.

**Key areas:** Graph traversal, service integration, idempotent processing, AI-assisted document workflows.

### 5. Omnichannel AI Assistant
[View Case Study](https://asimali.online/projects/ai-assistant-platform)

An AI assistant combining an operational API with a dedicated FastAPI intelligence service.

- Built workspace-scoped document ingestion and retrieval-augmented generation (RAG) with Pinecone.
- Connected speech-to-text, retrieval, and text-to-speech in a voice-processing pipeline.
- Integrated WhatsApp Cloud API webhooks for message routing.

**Key areas:** Python services, retrieval pipelines, AI integrations, automation workflows.

### 6. Samsung 5G Migration
[View Case Study](https://asimali.online/projects/samsung-network-migration)

A network-data migration tool for extracting circuit-path information from complex telecom records.

- Developed priority-ordered regex extraction with confidence scoring and field-level provenance.
- Supported 48 fields across a grid containing more than 60 columns.
- Integrated a .NET printing bridge using the Brother SDK.

**Key areas:** Data extraction, deterministic parsing, traceability, hardware integration.

### 7. Shipment Tracker & IMS
[View Case Study](https://asimali.online/projects/shipment-tracker-and-ims)

An email-driven shipment tracking and inventory management system.

- Built automated IMAP ingestion with Word and HTML parsers.
- Added message-ID deduplication and reconciliation for split or orphaned shipments.
- Implemented quantity ledgers and a guarded nine-state shipment lifecycle.

**Key areas:** Reliable ingestion, data reconciliation, deduplication, state-machine design.

### 8. Zametrix PropTech SaaS
[View Case Study](https://asimali.online/projects/zametrix)

A property research platform for comparing locations, managing partner input, and generating investor reports.

- Aggregated field survey data across 17 tables and multiple snapshots.
- Developed weighted location-comparison scoring on a 0–100 scale.
- Implemented four-role moderation, OTP-based partner governance, and automated PDF reports.

**Key areas:** Data aggregation, scoring systems, access control, reporting automation.

---

## Engineering Focus

### Backend Architecture
- Laravel modular monoliths and domain-oriented application design
- REST APIs, service boundaries, and maintainable business logic
- Queues, Laravel Horizon, and asynchronous workflows

### Security & Authorization
- OAuth 2.0, PKCE, JWT, TOTP, and token revocation
- Hierarchical role-based access control (RBAC)
- Graph-aware attribute-based access control (ABAC)
- HMAC-signed requests, scoped permissions, and access revocation

### Data & Reliability
- Transaction boundaries, locking, and concurrency control
- Chunked imports, query optimization, and N+1 remediation
- Idempotent pipelines, deduplication, and guarded state transitions

### Document Processing & Integrations
- Resumable uploads and PDF generation
- IMAP ingestion and structured data extraction
- AI-assisted OCR, RAG, and third-party API integrations

## Technology Stack

| Category | Technologies |
|---|---|
| **Backend** | PHP 8.2+, Laravel 11/12, Python, FastAPI, REST APIs |
| **Database & Caching** | MySQL 8, Redis, Pinecone, Eloquent ORM |
| **Queues & Processing** | Laravel Horizon, background jobs, chunked processing |
| **Security & Identity** | OAuth 2.0, PKCE, JWT (RS256), TOTP, HMAC-SHA256, Sanctum, RBAC, ABAC |
| **AI & Integrations** | Gemini API, Tesseract OCR, RAG, WhatsApp Cloud API, Microsoft Graph API, Stripe, PayPal |
| **Testing & Code Quality** | Pest, PHPUnit 11, PHPStan, Larastan, Laravel Telescope |
| **Frontend** | TypeScript, JavaScript, React, Inertia.js, Blade, Tailwind CSS |
| **Tools & Delivery** | Linux, GitHub Actions, Browsershot, Dompdf |

## Writing & Engineering Notes

I write about backend architecture, Laravel application structure, and maintainable engineering practices.

**[How I Structure a Laravel Application for Long-Term Maintenance](https://asimali.online/blog)**

More projects and architecture deep-dives are available on my [portfolio](https://asimali.online).

## Contact

I'm open to backend engineering opportunities, architecture discussions, and challenging workflow automation projects.

- **Portfolio:** [asimali.online](https://asimali.online)
- **LinkedIn:** [linkedin.com/in/the-asimali](https://www.linkedin.com/in/the-asimali)
- **Email:** [asimalipeerzada@gmail.com](mailto:asimalipeerzada@gmail.com)
