# System Architecture - AI-Powered Startup MVP Builder

## Overview

The application uses a three-tier architecture: a browser-based frontend, a REST API backend, and an AI service layer that communicates with an external LLM API. Data is stored in a relational database and generated files are saved to local or cloud storage.

## High-Level System Diagram

```
+-------------------+
|   User (Browser)  |
|  Single-Page App  |
+--------+----------+
         |
         | HTTP / REST
         v
+--------+----------+
|   Backend API     |
|  (Node / Python)  |
+--+-------------+--+
   |             |
   v             v
+--+------+ +----+--------+
|   DB    | | AI Service  |
|(SQLite/ | | (Prompt +   |
|Postgres)| |  LLM API)   |
+---------+ +-------------+
                  |
                  v
          +-------+-------+
          | External LLM  |
          |  (e.g. GPT-4) |
          +---------------+
```

## Components

| Component | Responsibility |
|---|---|
| Single-Page App | Renders the idea intake form, feature review UI, and document export panel. |
| Backend API | Handles HTTP requests, enforces business rules, and coordinates the AI service. |
| AI Service | Builds prompts from user input, calls the LLM, and parses structured responses. |
| External LLM API | Generates problem statements, feature suggestions, user stories, and documents. |
| Database | Stores project data, features, and generated user stories. |
| File Storage | Holds generated Markdown files and ZIP archives for download. |

## Request Flow

1. User submits a startup idea via the intake form.
2. The frontend sends a POST request to the backend API.
3. The backend passes the input to the AI Service.
4. The AI Service calls the external LLM API and parses the response.
5. Results are saved to the database and returned to the frontend.
6. The user reviews, edits, and confirms the feature list.
7. The backend generates Markdown documents and stores them in file storage.
8. The user downloads the complete plan as a ZIP archive.
