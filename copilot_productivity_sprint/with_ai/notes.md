# AI-Assisted Solutions Notes

This document highlights the time reductions associated with outsourcing the identical benchmark assignments utilizing a Generative LLM tool/Code Assistant natively.

## Time Log & Prompt Executions

### Task 1: User Registration Endpoint (`task1_users_api.py`)
- **Time Spent:** 3 minutes *(Down from 18-minute manual baseline)*
- **Prompt Used:** *"Write an HTTP POST `/users` API strictly via standard Python natively using `http.server`. It must seamlessly process a JSON dict comprising `{name, email}`, validate name exists, regex validate email, block duplications utilizing an in-memory dictionary `users_db`, and return a 201 mapped response embedding a UUID."*

### Task 2: Refactor Price Calculator (`task2_price_calc.js`)
- **Time Spent:** 2 minutes *(Down from the 14 minute baseline)*
- **Prompt Used:** *"Refactor this JavaScript pricing logic correctly into 3 modular sub-functions. Apply a flat 10% mapping dynamically if `SAVE10` overrides. Ensure floats natively format exclusively rounding successfully avoiding floating boundaries. Append 5 tight unit tests natively mapping Node `assert`."*

### Task 3: Log Parser CLI (`task3_log_summary.py`)
- **Time Spent:** 2 minutes *(Down from the original 12 minute configuration)*
- **Prompt Used:** *"Generate a Python script `log_summary.py` interacting with a file path mapped securely via `sys.argv`. It processes iteratively reading logs natively framed as `[YYYY] [MM] [LEVEL] [MSG]`. Operate `collections.Counter` tracking INFO, WARN, and ERROR sorting descending top 3 errors."*

## Execution Summary 
Outsourcing foundational logic components through generative prompting frameworks drastically propelled overall project progression velocity natively (~600% aggregate time savings globally).
