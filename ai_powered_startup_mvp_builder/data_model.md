# Data Model - AI-Powered Startup MVP Builder

## Overview

The data model consists of three core entities: Project, Feature, and UserStory. A Project holds the startup idea and generated metadata. Features belong to a Project and represent individual product capabilities. UserStories are generated from Features and form the project backlog.

## Entities

### Project

Stores the startup idea and AI-generated planning output for a session.

| Field | Type | Description |
|---|---|---|
| id | UUID | Primary key. |
| session_id | VARCHAR | Identifier of the anonymous browser session. |
| title | VARCHAR | Short name for the startup idea. |
| raw_idea | TEXT | Original plain-text idea entered by the user. |
| problem_statement | TEXT | AI-generated problem statement. |
| target_users | TEXT | AI-generated description of the target audience. |
| constraints | TEXT | User-defined constraints such as time and budget. |
| created_at | TIMESTAMP | When the project was created. |
| updated_at | TIMESTAMP | When the project was last modified. |

### Feature

Represents a single product feature within a Project. Limited to 10 per project.

| Field | Type | Description |
|---|---|---|
| id | UUID | Primary key. |
| project_id | UUID | Foreign key referencing Project. |
| title | VARCHAR | Short name of the feature. |
| description | TEXT | What the feature does. |
| priority | VARCHAR | MoSCoW value: must_have, should_have, could_have, or wont_have. |
| in_scope | BOOLEAN | Whether the feature is within the project constraints. |
| created_at | TIMESTAMP | When the feature was added. |

### UserStory

A user story generated from an in-scope Feature, stored for export and backlog use.

| Field | Type | Description |
|---|---|---|
| id | UUID | Primary key. |
| feature_id | UUID | Foreign key referencing Feature. |
| project_id | UUID | Foreign key referencing Project. |
| role | VARCHAR | The user role in the story (e.g. founder, developer). |
| action | TEXT | What the user wants to do. |
| benefit | TEXT | Why the user wants to do it. |
| full_text | TEXT | Complete story: As a [role], I want [action] so that [benefit]. |
| created_at | TIMESTAMP | When the story was generated. |

## Relationships

```
Project
  |
  |-- (1 to many) --> Feature
                        |
                        |-- (1 to many) --> UserStory
```

| Relationship | Cardinality | Description |
|---|---|---|
| Project to Feature | 1 to many | A project contains up to 10 features. |
| Feature to UserStory | 1 to many | Each feature generates one or more user stories. |
