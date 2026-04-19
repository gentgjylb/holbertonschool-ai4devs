import sqlite3
import uuid
import json

DB_PATH = "mvp.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE IF NOT EXISTS projects (
            id TEXT PRIMARY KEY,
            title TEXT,
            raw_idea TEXT,
            problem_statement TEXT,
            target_users TEXT,
            constraints TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS features (
            id TEXT PRIMARY KEY,
            project_id TEXT,
            title TEXT,
            description TEXT,
            priority TEXT,
            in_scope BOOLEAN,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS user_stories (
            id TEXT PRIMARY KEY,
            project_id TEXT,
            feature_id TEXT,
            role TEXT,
            action TEXT,
            benefit TEXT,
            full_text TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    conn.close()

def execute_query(query, args=(), fetchone=False, fetchall=False, commit=False):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute(query, args)
    
    res = None
    if fetchone:
        res = dict(c.fetchone()) if c.fetchone() else None
    elif fetchall:
        res = [dict(row) for row in c.fetchall()]
        
    if commit:
        conn.commit()
        
    conn.close()
    return res

def create_project(title, raw_idea, problem_statement, target_users, constraints):
    pid = str(uuid.uuid4())
    execute_query(
        "INSERT INTO projects (id, title, raw_idea, problem_statement, target_users, constraints) VALUES (?, ?, ?, ?, ?, ?)",
        (pid, title, raw_idea, problem_statement, target_users, constraints),
        commit=True
    )
    return pid

def get_project(pid):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM projects WHERE id = ?", (pid,))
    row = c.fetchone()
    conn.close()
    return dict(row) if row else None

def save_features(project_id, features):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    for f in features:
        fid = str(uuid.uuid4())
        c.execute(
            "INSERT INTO features (id, project_id, title, description, priority, in_scope) VALUES (?, ?, ?, ?, ?, ?)",
            (fid, project_id, f['title'], f['description'], f.get('priority', 'should_have'), f.get('in_scope', True))
        )
    conn.commit()
    conn.close()

def get_features(project_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM features WHERE project_id = ?", (project_id,))
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def save_stories(project_id, stories):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    for s in stories:
        sid = str(uuid.uuid4())
        c.execute(
            "INSERT INTO user_stories (id, project_id, feature_id, role, action, benefit, full_text) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (sid, project_id, s.get('feature_id', ''), s['role'], s['action'], s['benefit'], s['full_text'])
        )
    conn.commit()
    conn.close()

def get_stories(project_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM user_stories WHERE project_id = ?", (project_id,))
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]
