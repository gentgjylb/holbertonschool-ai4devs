import uuid
from datetime import datetime, date
from typing import List, Optional, Dict, Any, Set

class Task:
    """Represents a single task in the system."""
    
    def __init__(self, title: str, description: str = "", due_date: Optional[date] = None):
        if not title:
            raise ValueError("Task title cannot be empty.")
            
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.status = "pending"
        self.due_date = due_date
        self.created_at = datetime.now()
        self.tags: Set[str] = set()
        
    def mark_completed(self) -> None:
        """Marks the task as completed."""
        self.status = "completed"
        
    def mark_pending(self) -> None:
        """Marks the task as pending."""
        self.status = "pending"
        
    def update_due_date(self, new_due_date: date) -> None:
        """Updates the due date for the task."""
        self.due_date = new_due_date
        
    def add_tag(self, tag: str) -> None:
        """Adds a tag to the task."""
        if tag:
            self.tags.add(tag.lower())
            
    def remove_tag(self, tag: str) -> None:
        """Removes a tag from the task."""
        self.tags.discard(tag.lower())
        
    def to_dict(self) -> Dict[str, Any]:
        """Serializes the task to a dictionary format."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "tags": list(self.tags),
            "created_at": self.created_at.isoformat()
        }


class TaskManager:
    """Manages a collection of tasks."""
    
    def __init__(self):
        self.tasks: List[Task] = []
        
    def add_task(self, title: str, description: str = "", due_date: Optional[date] = None) -> Task:
        """Creates and adds a new task to the manager."""
        task = Task(title, description, due_date)
        self.tasks.append(task)
        return task
        
    def get_task(self, task_id: str) -> Optional[Task]:
        """Retrieves a task by its unique ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
        
    def remove_task(self, task_id: str) -> bool:
        """Removes a task by its ID. Returns True if successful."""
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def get_all_tasks(self) -> List[Task]:
        """Returns a copy of all tasks."""
        return list(self.tasks)

    # NEW FEATURE: Task filtering
    def filter_tasks(self, 
                    status: Optional[str] = None, 
                    due_date: Optional[date] = None, 
                    overdue: bool = False,
                    tag: Optional[str] = None,
                    keyword: Optional[str] = None) -> List[Task]:
        """
        Filters tasks based on various criteria.
        This provides a highly flexible way to search and organize tasks.
        """
        filtered = self.tasks
        
        if status:
            filtered = [t for t in filtered if t.status == status]
            
        if due_date:
            filtered = [t for t in filtered if t.due_date == due_date]
            
        if tag:
            tag_lower = tag.lower()
            filtered = [t for t in filtered if tag_lower in t.tags]
            
        if keyword:
            kw = keyword.lower()
            filtered = [t for t in filtered if kw in t.title.lower() or kw in t.description.lower()]
            
        if overdue:
            today = date.today()
            filtered = [
                t for t in filtered 
                if t.due_date and t.due_date < today and t.status != "completed"
            ]
            
        return filtered
        
    def sort_tasks(self, by: str = "due_date", reverse: bool = False) -> List[Task]:
        """Sorts tasks depending on specified attribute."""
        if by == "due_date":
            # Handle None due dates by placing them at the end
            max_date = date.max
            return sorted(self.tasks, key=lambda t: t.due_date or max_date, reverse=reverse)
        elif by == "created_at":
            return sorted(self.tasks, key=lambda t: t.created_at, reverse=reverse)
        elif by == "title":
            return sorted(self.tasks, key=lambda t: t.title.lower(), reverse=reverse)
        elif by == "status":
            return sorted(self.tasks, key=lambda t: t.status, reverse=reverse)
        else:
            raise ValueError(f"Unsupported sort attribute: {by}")
            
    def summary(self) -> Dict[str, int]:
        """Generates a numerical summary of the tasks."""
        completed = sum(1 for t in self.tasks if t.status == "completed")
        pending = sum(1 for t in self.tasks if t.status == "pending")
        overdue = len(self.filter_tasks(overdue=True))
        
        return {
            "total": len(self.tasks),
            "completed": completed,
            "pending": pending,
            "overdue": overdue
        }
