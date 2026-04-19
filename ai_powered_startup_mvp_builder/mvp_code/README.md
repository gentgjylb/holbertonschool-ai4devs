# MVP Code - AI-Powered Startup MVP Builder

This directory contains the fully functional Minimum Viable Product (MVP) of the AI-Powered Startup MVP Builder. It follows a Python backend and Vanilla HTML/JS frontend architecture.

## Requirements

- Python 3.8+
- Node.js (Optional, but useful for serving the frontend `http-server`)

## Quickstart Guide

### 1. Start the Backend

1. Navigate to the `backend` folder:
   ```bash
   cd mvp_code/backend
   ```
2. Install the required Python packages (we recommend using a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```
3. Run the FastAPI development server:
   ```bash
   uvicorn main:app --reload --port 8000
   ```
   *The mock AI backend is now running at `http://localhost:8000`.*

### 2. Start the Frontend

1. Open a new terminal window.
2. Navigate to the `frontend` folder:
   ```bash
   cd mvp_code/frontend
   ```
3. Serve the directory using any HTTP server. For example:
   ```bash
   python -m http.server 3000
   ```
4. Open your browser and navigate to `http://localhost:3000`.

### Usage
- Start by typing an idea in the **Idea Intake** section and click "Analyze Idea".
- Proceed through the steps to generate Features, User Stories, and finally the Markdown Export document.
