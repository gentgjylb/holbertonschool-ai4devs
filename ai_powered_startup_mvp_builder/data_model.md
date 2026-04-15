# Data Model - AI-Powered Startup MVP Builder

## Overview

The data model is designed around a **session-scoped project** where no user
authentication is required. A session owns one active project. A project contains
features prioritized by the user, user stories generated from those features, and a
record of any exports produced. The three primary entities are **Project**, **Feature**,
and **UserStory**.

---

## Entities

### 1. Project

The central entity. Represents a single MVP concept created within a browser session.
All other entities belong to a project.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | UUID | PRIMARY KEY | Unique project identifier. |
| `session_id` | VARCHAR(128) | NOT NULL, INDEX | Anonymous browser session token that owns this project. |
| `title` | VARCHAR(255) | NOT NULL | Short name for the startup idea (e.g., "AI MVP Builder"). |
| `raw_idea` | TEXT | NOT NULL | Original plain-language description entered by the user. |
| `problem_statement` | TEXT | NULLABLE | AI-extracted problem statement; populated after intake. |
| `target_users` | TEXT | NULLABLE | AI-extracted description of the intended user audience. |
| `constraints` | TEXT | NULLABLE | User-defined constraints: time, budget, team size (free text). |
| `status` | ENUM | NOT NULL, DEFAULT `draft` | Lifecycle state: `draft`, `scoped`, `exported`. |
| `created_at` | TIMESTAMP | NOT NULL, DEFAULT NOW() | When the project was first created. |
| `updated_at` | TIMESTAMP | NOT NULL | Automatically updated on every write. |

**Acceptance criteria:** A project cannot transition to `scoped` until at least one
feature with priority `must_have` exists and `problem_statement` is non-null.

---

### 2. Feature

Represents a single product capability scoped to a project. Capped at 10 per project
to enforce the MVP constraint. Each feature carries a MoSCoW priority and an explicit
in-scope flag that reflects constraint validation results.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | UUID | PRIMARY KEY | Unique feature identifier. |
| `project_id` | UUID | NOT NULL, FOREIGN KEY → Project.id | Owning project. |
| `title` | VARCHAR(255) | NOT NULL | Short feature name (e.g., "AI-Guided Idea Intake"). |
| `description` | TEXT | NOT NULL | Full description of what the feature does and why it matters. |
| `priority` | ENUM | NOT NULL | MoSCoW value: `must_have`, `should_have`, `could_have`, `wont_have`. |
| `in_scope` | BOOLEAN | NOT NULL, DEFAULT TRUE | Set to `false` by the constraint checker if the feature exceeds limits. |
| `ai_suggested` | BOOLEAN | NOT NULL, DEFAULT TRUE | `true` = AI-generated; `false` = manually added by the user. |
| `position` | SMALLINT | NOT NULL | Display order within the project (1–10). |
| `created_at` | TIMESTAMP | NOT NULL, DEFAULT NOW() | When the feature was added to the project. |

**Constraints:** A `CHECK` constraint enforces that the total number of features per
`project_id` never exceeds 10.

---

### 3. UserStory

Represents a structured user story automatically derived from an in-scope feature.
Stored as discrete role/action/benefit fields so individual parts can be queried or
edited independently, as well as a pre-assembled full-text string for export.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | UUID | PRIMARY KEY | Unique user story identifier. |
| `feature_id` | UUID | NOT NULL, FOREIGN KEY → Feature.id | Source feature this story was derived from. |
| `project_id` | UUID | NOT NULL, FOREIGN KEY → Project.id | Owning project (denormalized for efficient querying). |
| `role` | VARCHAR(100) | NOT NULL | User role performing the action (e.g., "startup founder"). |
| `action` | TEXT | NOT NULL | The specific system action the user wants to perform. |
| `benefit` | TEXT | NOT NULL | The measurable outcome the user expects from the action. |
| `full_text` | TEXT | NOT NULL | Assembled story: "As a [role], I want to [action] so that [benefit]." |
| `approved` | BOOLEAN | NOT NULL, DEFAULT FALSE | Set to `true` once the user confirms the story before export. |
| `created_at` | TIMESTAMP | NOT NULL, DEFAULT NOW() | When the story was generated. |

**Acceptance criteria:** Only stories where `approved = true` are included in the
exported backlog document.

---

### 4. ExportRecord

Tracks each ZIP export snapshot generated for a project. Allows the user to re-download
an earlier export within the same session without regenerating files.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | UUID | PRIMARY KEY | Unique export identifier. |
| `project_id` | UUID | NOT NULL, FOREIGN KEY → Project.id | Owning project. |
| `file_key` | VARCHAR(512) | NOT NULL, UNIQUE | Storage path or object key for the generated ZIP archive. |
| `file_size_bytes` | INTEGER | NULLABLE | Size of the archive in bytes; populated after generation. |
| `document_count` | SMALLINT | NOT NULL, DEFAULT 0 | Number of `.md` files bundled in the export. |
| `created_at` | TIMESTAMP | NOT NULL, DEFAULT NOW() | When the export was generated. |
| `downloaded_at` | TIMESTAMP | NULLABLE | Timestamp of the most recent download by the user. |

---

## Entity Relationship Diagram

```
Project
  │
  │ 1 : N  (max 10 features)
  ├──────────────────► Feature
  │                       │
  │                       │ 1 : N
  │                       └──────► UserStory
  │
  │ 1 : N
  └──────────────────► ExportRecord
```

---

## Relationships Summary

| From | To | Cardinality | Notes |
|---|---|---|---|
| Project | Feature | 1 : N (max 10) | Only features where `in_scope = true` are acted upon. |
| Project | ExportRecord | 1 : N | Unlimited exports; each is a point-in-time snapshot. |
| Feature | UserStory | 1 : N | One story generated per in-scope feature by default; user can add more. |
