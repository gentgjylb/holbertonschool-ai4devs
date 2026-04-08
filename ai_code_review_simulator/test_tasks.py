import unittest
from datetime import date, timedelta
from tasks import Task, TaskManager

class TestTaskMethods(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Buy groceries", "Milk, Bread, Eggs")
        self.assertEqual(task.title, "Buy groceries")
        self.assertEqual(task.status, "pending")
        self.assertIsNone(task.due_date)
        
    def test_task_status_toggle(self):
        task = Task("Finish report")
        task.mark_completed()
        self.assertEqual(task.status, "completed")
        task.mark_pending()
        self.assertEqual(task.status, "pending")
        
    def test_task_tags(self):
        task = Task("Work duty")
        task.add_tag("urgent")
        task.add_tag("work")
        self.assertIn("urgent", task.tags)
        task.remove_tag("urgent")
        self.assertNotIn("urgent", task.tags)

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
        
    def test_add_and_remove(self):
        task = self.manager.add_task("Test task")
        self.assertEqual(len(self.manager.get_all_tasks()), 1)
        self.manager.remove_task(task.id)
        self.assertEqual(len(self.manager.get_all_tasks()), 0)

    # Test the newly added filter_tasks functionality
    def test_filter_by_status(self):
        t1 = self.manager.add_task("Task 1")
        t2 = self.manager.add_task("Task 2")
        t1.mark_completed()
        
        completed_tasks = self.manager.filter_tasks(status="completed")
        pending_tasks = self.manager.filter_tasks(status="pending")
        
        self.assertEqual(len(completed_tasks), 1)
        self.assertEqual(completed_tasks[0].id, t1.id)
        self.assertEqual(len(pending_tasks), 1)
        
    def test_filter_by_due_date(self):
        today = date.today()
        tomorrow = today + timedelta(days=1)
        self.manager.add_task("Task 1", due_date=today)
        self.manager.add_task("Task 2", due_date=tomorrow)
        
        due_today = self.manager.filter_tasks(due_date=today)
        self.assertEqual(len(due_today), 1)
        self.assertEqual(due_today[0].title, "Task 1")
        
    def test_filter_overdue(self):
        yesterday = date.today() - timedelta(days=1)
        today = date.today()
        
        t1 = self.manager.add_task("Overdue Task", due_date=yesterday)
        t2 = self.manager.add_task("Completed Overdue", due_date=yesterday)
        t2.mark_completed()
        self.manager.add_task("Future Task", due_date=today + timedelta(days=1))
        
        overdue_tasks = self.manager.filter_tasks(overdue=True)
        self.assertEqual(len(overdue_tasks), 1)
        self.assertEqual(overdue_tasks[0].title, "Overdue Task")

    def test_filter_by_keyword_and_tag(self):
        t1 = self.manager.add_task("Deploy server", "Production deployment")
        t1.add_tag("devops")
        
        results_keyword = self.manager.filter_tasks(keyword="deploy")
        self.assertEqual(len(results_keyword), 1)
        
        results_tag = self.manager.filter_tasks(tag="devops")
        self.assertEqual(len(results_tag), 1)

if __name__ == "__main__":
    unittest.main()
