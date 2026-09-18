---
layout: default
title: Santhanasamy Arockiyasamy
---

## Professional Summary

Staff mobile engineer with 14+ years building Android applications at scale for fintech, healthcare, and consumer domains. Led engineering teams delivering apps with 10M–100M+ downloads across Capital One (50M+), Samsung (100M+), and Walgreens (10M+). Deep expertise in Kotlin/Compose, multi-module architecture, on-device AI/ML, and mobile security compliance (PCI-DSS, HIPAA, SOC 2). Designed and shipped Fiserv Connect Pay SDK — a white-label payment SDK adopted by major financial institutions with PCI-DSS Level 2 compliance. Actively building with Gen-AI and agentic systems — designing multi-agent orchestration patterns, MCP server integrations, and AI-augmented engineering workflows. Track record of reducing crash rates by 85%, cutting app launch times by 44%, and shipping SDKs adopted by major financial institutions.

---

## Core Competencies

<span class="chip">Mobile System Design</span>
<span class="chip">Kotlin / Jetpack Compose</span>
<span class="chip">KMP & Coroutines</span>
<span class="chip">iOS / Swift</span>
<span class="chip">Multi-Module Architecture</span>
<span class="chip">On-Device AI/ML</span>
<span class="chip">Agentic AI & LLM Integration</span>
<span class="chip">Server-Driven UI (SDUI)</span>
<span class="chip">Payment SDK Engineering</span>
<span class="chip">Performance Optimization</span>
<span class="chip">Mobile Security & Compliance</span>
<span class="chip">Claude API & MCP</span>
<span class="chip">New Relic & Observability</span>
<span class="chip">CI/CD & DevOps</span>

---

## Technical Skills

| Domain | Technologies |
|---|---|
| **Languages** | Kotlin (Expert), Java, Dart, TypeScript |
| **Android** | Jetpack Compose, Coroutines/Flow, KMP, Hilt, Room, Navigation |
| **Architecture** | MVVM, MVI, Clean Architecture, Multi-Module, Modularization |
| **AI/ML** | TensorFlow Lite, ML Kit, ONNX, Gemini Nano, LLM Integration, RAG |
| **Gen-AI & Agents** | Claude API, MCP (Model Context Protocol), Multi-Agent Orchestration, Prompt Engineering, Agentic Workflows |
| **Backend / APIs** | REST, GraphQL, gRPC, Firebase, AWS, Azure |
| **CI/CD & Quality** | GitHub Actions, Jenkins, Fastlane, Gradle (KTS/Catalogs) |
| **Testing** | JUnit, Mockk, Espresso, Compose Testing, Turbine |
| **Observability** | New Relic, Crashlytics, Sentry, Firebase Analytics, Mixpanel |
| **Security** | PCI-DSS, SOC 2, HIPAA, OWASP Mobile Top 10, OAuth 2.0/OIDC |
| **Security Testing** | MAST, SAST (Fortify), DAST, Penetration Testing, SCA |
| **Accessibility** | Level Access, WCAG 2.1 Compliance, Accessibility Auditing |
| **Cross-Platform** | Flutter, Kotlin Multiplatform, React Native |

---

## Professional Experience

### Technical Architect <span style="float:right; font-style:italic; font-weight:normal; font-size:0.9em;">Nov 2017 – Present</span>

**Photon InfoTech Inc.** — Atlanta, GA

#### Williams-Sonoma Retail Apps — Staff Level Engineer (Contractor)

*Multi-brand retail ecosystem • Platform modernization • Cross-platform strategy*

- Architected and led the Jetpack Compose migration, defining clean architecture boundaries (domain, data, presentation layers) that became the reference implementation adopted across mobile teams
- Engineered a brownfield React Native integration strategy, migrating feature modules into the existing native Android application while preserving runtime stability and release velocity
- Designed and built foundational React Native New Architecture infrastructure using TurboModules and Fabric Views, establishing the bridge layer for native-to-JS interop at scale
- Drove platform decisioning research, evaluating native vs cross-platform trade-offs with data-backed recommendations that informed the organization's multi-year mobile technology roadmap
- Optimized application performance by profiling and reducing frame drops, startup latency, and UI jank across critical user journeys — ensuring sub-second render times on Compose screens under production load
- Led memory management improvements, identifying and resolving leak patterns in lifecycle-aware components, bitmap handling, and RN bridge allocations — reducing OOM crash rates across release variants
- Managed multi-variant application delivery (brand-specific variants within a single codebase), architecting build flavors, shared modules, and variant-specific configurations while maintaining a single deployable pipeline
- Established observability and profiling practices, integrating Systrace, LeakCanary, and baseline profiles into CI to enforce performance budgets and prevent regressions before production
- Mentored junior and mid-level engineers through architecture reviews, pairing sessions, and internal tech talks — elevating team capability in Compose, modularization, and reactive patterns
- Operated as a cross-functional technical partner, aligning with product, QA, and backend teams on API contracts, feature rollout sequencing, and release risk assessment — translating technical constraints into stakeholder-ready trade-off analysis

---

#### Capital One Banking Android — Staff Level Engineer (Contractor via Subvendor)

*Flagship banking app • 50M+ users • Led cross-functional engineering team*

- Owned architecture and delivery of Rewards Center and Document Management features across 15+ feature modules in a multi-module codebase
- Migrated legacy views to Jetpack Compose, increasing UI development velocity by 40% and reducing view-layer defects
- Architected offline-first data layer with Room + Kotlin Flow, reducing redundant API calls by 35%
- Reduced cold-start time from 3.2s to 1.8s (44% improvement) through startup profiling, lazy initialization, and baseline profiles
- Decreased memory footprint by 25% via systematic leak detection and profiling with LeakCanary and Android Profiler
- Integrated ML Kit for document scanning or OCR in Document Center, improving recognition accuracy by 45%
- Deployed on-device TensorFlow Lite models for personalized rewards with less than 100ms inference via quantization and GPU delegation
- Drove crash rate down from 0.8% to 0.12% through stability analysis, ANR resolution, and automated regression testing (200+ journeys)
- Led PCI-DSS compliance for payment card features; implemented certificate pinning, biometric auth, and encrypted storage
- Increased test coverage from 45% to 95% with JUnit, Mockk, Espresso, and Compose UI testing

---

#### Fiserv — Principal Engineer (Contractor)

**Connect PaySDK**

*White-label payment SDK • Major financial institution clients • PCI-DSS Level 2*

- Architected plugin-based SDK enabling client customization without source modification; reduced integration time from 6 weeks to 2 weeks
- Implemented end-to-end encryption and tokenization achieving PCI-DSS Level 2 compliance
- Built receipt scanning and expense categorization using custom on-device ML models
- Developed fraud detection algorithms achieving <5% false positive rate
- Implemented Server-Driven UI (SDUI) architecture rendering screen layouts and content from backend API responses, enabling dynamic feature updates without app releases
- Integrated conversational AI assistant for banking queries using LLM APIs

**Money Network**

*Prepaid card & payroll disbursement platform • Millions of cardholders • PCI-DSS compliant*

- Architected mobile-first card management experience for prepaid payroll cards, enabling real-time balance inquiries, transaction history, and fund transfers
- Designed secure card activation and PIN management flows with end-to-end encryption and hardware-backed keystore integration
- Led migration from legacy REST APIs to a modern GraphQL layer, reducing payload sizes by 40% and improving screen load times
- Implemented push notification framework for real-time transaction alerts, low-balance warnings, and direct deposit confirmations
- Built ATM and branch locator with geofencing capabilities, driving a 25% increase in fee-free ATM usage among cardholders
- Owned PCI-DSS compliance for card data handling; implemented tokenization, certificate pinning, and runtime tamper detection

**AuthentiCare**

*Healthcare authentication platform • HIPAA-compliant • Multi-tenant SaaS*

- Defined end-to-end mobile architecture for a HIPAA-compliant authentication platform, establishing security patterns adopted across all Fiserv healthcare products
- Designed multi-factor authentication framework supporting biometric, OTP, and device-trust flows with configurable policy enforcement per tenant
- Led technical strategy for PHI-compliant communication layer, ensuring data encryption at rest and in transit with FIPS 140-2 validated cryptographic modules
- Drove cross-team alignment between mobile, backend, and compliance teams to deliver SOC 2 Type II audit readiness within a single release cycle
- Architected session management and token lifecycle with adaptive timeout policies, reducing unauthorized access incidents by 60%
- Mentored engineering team on secure coding practices and OWASP Mobile Top 10 mitigations; established automated security scanning in CI pipeline

---

#### Key Responsibilities & Initiatives

**Gen-AI & Agentic Development**

*AI-augmented engineering workflows • Multi-agent systems • MCP integrations*

- Designed and built multi-agent orchestration systems using Planner–Executor coordination patterns with context isolation and parallel subagent dispatch
- Architected 5 specialized AI agents for mobile development workflows: architecture planning, feature building, debugging, test generation, and codebase analysis (spiker)
- Built custom MCP server integrations for tool-augmented AI workflows, implementing stdio and HTTP transports with structured tool schemas
- Developed AI-powered React component generator (UIGen) using Claude API with Vercel AI SDK, tool use, and live Babel-compiled preview
- Applied agentic architecture patterns in production: automated code spike audits, feature planning with AI-assisted decomposition, and AI-driven test coverage analysis
- Implemented prompt engineering best practices for structured output, evaluation pipelines, and context management with caching optimization

**Engineering Leadership & Mentorship**

- Scaled mobile engineering team from 4 to 10+ engineers across 2 scrum teams, setting the hiring bar and establishing technical onboarding standards
- Founded engineering excellence guild; led architectural reviews, design discussions, and tech talks on Compose, Coroutines, and mobile AI
- Drove technical design decisions across teams — API contracts, module boundaries, and technology selection — evaluating trade-offs for scalability and long-term maintainability
- Established code review standards and practices across teams, raising the engineering bar on performance, security, and architectural consistency
- Initiated CI/CD improvements reducing build times by 60% through Gradle optimization and pipeline redesign
- Mentored engineers in Android architecture, Kotlin best practices, and AI/ML integration through pairing, design reviews, and structured feedback
- Hands-on with cross-platform mobile development — iOS/SwiftUI for native composition and React Native brownfield integration using Turbo Modules and Fabric architecture

---

### Technical Architect, Mobile <span style="float:right; font-style:italic; font-weight:normal; font-size:0.9em;">Feb 2015 – Nov 2017</span>

**Photon InfoTech Inc.** — Chennai, India

- Designed reference mobile architecture adopted across 10+ enterprise projects; established mobile Center of Excellence
- Led evaluation and adoption of React Native for cross-platform development, reducing dev time by 40%

**Walgreens Mobile App**

*Retail pharmacy • 10M+ downloads*

- Architected prescription refill and photo printing features with location-based store finder and real-time inventory
- Integrated barcode scanning for prescription management using camera APIs

**AuthentiCare 2.0**

*Healthcare authentication platform • HIPAA-compliant*

- Led development of secure authentication platform with PHI-compliant communication layer and multi-factor auth

---

### Lead Engineer <span style="float:right; font-style:italic; font-weight:normal; font-size:0.9em;">Jun 2012 – Feb 2015</span>

**Samsung Research India (SRI-N)** — Noida, India

**Samsung Galaxy Wearable (Gear Manager)**

*Companion app • 100M+ downloads*

- Architected companion app for Samsung smartwatches; built Sync SDK for Bluetooth device pairing and health data sync
- Optimized battery consumption through intelligent sync scheduling and data compression via Samsung Accessory Protocol

**Samsung Core Apps & Innovation**

- Reduced launch times by 20–35% across Contacts, Calendar, Phone, and Notes; cut OOM crashes by 50% via memory optimization
- Developed Samsung ColorNote (50M+ downloads) with cloud sync; created cross-device transfer using Wi-Fi Direct and NFC

**Awards:** Samsung Innovator Award (2014) • Innovator of the Month (Jul 2014) • Employee of the Year (2013)

---

### Software Engineer <span style="float:right; font-style:italic; font-weight:normal; font-size:0.9em;">Aug 2010 – May 2012</span>

**Huawei Technologies India** — Bangalore, India

- Developed Android system applications and AOSP framework customizations for Huawei devices
- **Best Contribution Award** (Feb 2012)

---

### Software Engineer <span style="float:right; font-style:italic; font-weight:normal; font-size:0.9em;">Jan 2010 – Jul 2010</span>

**Impiger Technologies** — Chennai, India

- Full-stack development for enterprise mobile applications; contributed to requirements, design, and deployment

---

## Education

| Degree | Institution | Year |
|---|---|---|
| **Master of Computer Applications (MCA)** | St. Joseph's College, Tiruchirappalli, India | 2006 – 2009 |
| **Bachelor of Science (Physics, Mathematics)** | St. Xavier's College, Tirunelveli, India | 2003 – 2006 |

---

## Certifications

- **Claude Certified Architect – Foundations (CCA-F)** — Anthropic • 2026 (In Progress)
- **Claude Code in Action** — Anthropic • 2026
- **Introduction to Subagents** — Anthropic • 2026
- **Introduction to Model Context Protocol (MCP)** — Anthropic / LinkedIn Learning • 2026
- **Claude 101** — Anthropic • 2026
- **Certified SAFe® Agilist (SA)** — Scaled Agile, Inc • 2026
- **Kotlin Android SDK – Certified Security** — Secure Code Warrior • 2021
- **Functional Programming Principles in Scala** — EPFL • 2017
- **Sun Certified Java Programmer (SCJP)** — Sun Microsystems • 2009

---

## Notable Projects

- **Williams-Sonoma Retail Apps** — Multi-brand retail, platform modernization & cross-platform strategy
- **Capital One Mobile** — Banking app, 50M+ downloads
- **Samsung Galaxy Wearable** — Companion app, 100M+ downloads
- **Samsung ColorNote** — Note-taking app, 50M+ downloads
- **Fiserv Connect Pay SDK** — Payment SDK, major financial institution clients
- **Walgreens Mobile** — Retail pharmacy app, 10M+ downloads
