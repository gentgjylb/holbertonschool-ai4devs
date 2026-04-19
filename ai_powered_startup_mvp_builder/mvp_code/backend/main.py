from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import database
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DB on startup
@app.on_event("startup")
def startup_event():
    database.init_db()

# --- Pydantic Models ---
class IdeaInput(BaseModel):
    title: str
    raw_idea: str
    constraints: Optional[str] = "No budget, 1 month time."

class Feature(BaseModel):
    title: str
    description: str
    priority: str
    in_scope: bool

class FeatureGenerateRequest(BaseModel):
    project_id: str

# --- Mock AI Functions ---
def mock_ai_intake(idea: str):
    return {
        "problem_statement": f"Users need a way to achieve their goals outlined in: '{idea[:50]}...'",
        "target_users": "Founders, Small Business Owners, Students"
    }

def mock_ai_features(idea: str):
    return [
        {"title": "User Authentication", "description": "Login/Signup functionality", "priority": "must_have", "in_scope": True},
        {"title": "Dashboard", "description": "Main view for the app", "priority": "must_have", "in_scope": True},
        {"title": "Payment Gateway", "description": "Stripe integration", "priority": "should_have", "in_scope": True},
        {"title": "Mobile App", "description": "Native iOS/Android app", "priority": "wont_have", "in_scope": False}
    ]

def mock_ai_stories(features: list):
    stories = []
    for f in features:
        if f['in_scope'] and f['priority'] != 'wont_have':
            stories.append({
                "feature_id": f['id'],
                "role": "User",
                "action": f"access {f['title']}",
                "benefit": f"use {f['description']}",
                "full_text": f"As a User, I want to access {f['title']} so that I can use {f['description']}."
            })
    return stories

# --- Routes ---
@app.post("/api/projects")
def create_project(data: IdeaInput):
    ai_result = mock_ai_intake(data.raw_idea)
    pid = database.create_project(
        data.title, 
        data.raw_idea, 
        ai_result['problem_statement'], 
        ai_result['target_users'], 
        data.constraints
    )
    return {"project_id": pid}

@app.get("/api/projects/{project_id}")
def get_project(project_id: str):
    p = database.get_project(project_id)
    if not p:
        raise HTTPException(status_code=404, detail="Project not found")
    return p

@app.post("/api/projects/{project_id}/features/generate")
def generate_features(project_id: str):
    p = database.get_project(project_id)
    if not p:
        raise HTTPException(status_code=404, detail="Project not found")
    
    # Mock generating 4 features
    ai_features = mock_ai_features(p['raw_idea'])
    database.save_features(project_id, ai_features)
    
    return database.get_features(project_id)

@app.get("/api/projects/{project_id}/features")
def list_features(project_id: str):
    return database.get_features(project_id)

@app.post("/api/projects/{project_id}/stories/generate")
def generate_stories(project_id: str):
    features = database.get_features(project_id)
    if not features:
        raise HTTPException(status_code=400, detail="No features found to generate stories from")
        
    ai_stories = mock_ai_stories(features)
    database.save_stories(project_id, ai_stories)
    return database.get_stories(project_id)

@app.get("/api/projects/{project_id}/stories")
def list_stories(project_id: str):
    return database.get_stories(project_id)

@app.get("/api/export/{project_id}")
def export_mvp_concept(project_id: str):
    p = database.get_project(project_id)
    features = database.get_features(project_id)
    stories = database.get_stories(project_id)
    
    md_content = f"# MVP Concept - {p['title']}\n\n"
    md_content += f"## Problem Statement\n{p['problem_statement']}\n\n"
    md_content += f"## Target Users\n{p['target_users']}\n\n"
    
    md_content += "## Core Features\n"
    for f in features:
        if f['in_scope']:
            md_content += f"### {f['title']} ({f['priority']})\n{f['description']}\n\n"
            
    md_content += "## User Stories\n"
    for s in stories:
        md_content += f"- {s['full_text']}\n"

    md_content += f"\n## Constraints\n{p['constraints']}\n"
    
    return {"markdown": md_content}
