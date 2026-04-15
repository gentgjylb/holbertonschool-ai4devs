# System Architecture - AI-Powered Startup MVP Builder

## Overview

The system follows a lightweight **client-server architecture** with a dedicated AI
orchestration layer. The frontend is a single-page application that communicates with a
REST API backend. The backend delegates natural-language processing tasks to a third-party
LLM API and persists session data in a relational database.

---

## High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER (Browser)                           │
│              Single-Page Application (HTML/JS)                  │
│                                                                 │
│   [Idea Intake Form] → [Feature Review UI] → [Export Panel]    │
└───────────────────────────────┬─────────────────────────────────┘
                                │ HTTPS / REST
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                       BACKEND (REST API)                        │
│                    Node.js / Express  or  Python / FastAPI      │
│                                                                 │
│  ┌──────────────┐  ┌──────────────────┐  ┌──────────────────┐  │
│  │  /api/intake │  │ /api/features    │  │ /api/export      │  │
│  │  (idea →     │  │ (prioritize &    │  │ (zip all docs)   │  │
│  │   concept)   │  │  user stories)   │  │                  │  │
│  └──────┬───────┘  └────────┬─────────┘  └──────────────────┘  │
│         │                   │                                   │
│  ┌──────▼───────────────────▼─────────────────────────────────┐ │
│  │               AI Orchestration Service                      │ │
│  │  - Prompt builder                                           │ │
│  │  - Response parser                                          │ │
│  │  - Constraint validator                                     │ │
│  └──────────────────────────┬──────────────────────────────────┘ │
└─────────────────────────────┼───────────────────────────────────┘
                              │ HTTPS
                              ▼
              ┌───────────────────────────────┐
              │   Third-Party LLM API         │
              │   (e.g., OpenAI GPT-4o)       │
              └───────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                      DATA LAYER                                 │
│                                                                 │
│   ┌──────────────────────┐    ┌──────────────────────────────┐  │
│   │  Relational DB       │    │  File / Object Storage       │  │
│   │  (PostgreSQL / SQLite│    │  (local disk or S3-compat.)  │  │
│   │   - Sessions         │    │  - Generated .md files       │  │
│   │   - Projects         │    │  - Exported ZIP archives     │  │
│   │   - Features         │    │                              │  │
│   │   - User Stories)    │    │                              │  │
│   └──────────────────────┘    └──────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Component Descriptions

| Component | Responsibility |
|---|---|
| **SPA (Frontend)** | Renders the intake form, feature review UI, and export panel. Communicates with the backend via REST. |
| **REST API (Backend)** | Routes requests, enforces business rules (e.g., 10-feature cap), and coordinates the AI service. |
| **AI Orchestration Service** | Builds prompts from user input, calls the LLM API, parses structured responses, and validates against constraints. |
| **LLM API** | Provides natural-language understanding and generation (problem extraction, feature suggestions, user story generation). |
| **Relational Database** | Stores session state, project metadata, features, and user stories for the duration of a session. |
| **File / Object Storage** | Holds generated Markdown documents and ZIP exports ready for download. |

---

## Data Flow (Happy Path)

1. User submits idea text via the **Intake Form**.
2. Backend receives the request and forwards the raw text to the **AI Orchestration Service**.
3. Orchestration service constructs a prompt and calls the **LLM API**.
4. LLM response is parsed into structured data (problem statement, target users, features).
5. Structured data is saved to the **Database** and returned to the **SPA**.
6. User reviews and adjusts features in the **Feature Review UI**.
7. Final features are converted into user stories and all documents are generated as `.md` files stored in **File Storage**.
8. User downloads the complete plan as a **ZIP archive** via the Export Panel.
