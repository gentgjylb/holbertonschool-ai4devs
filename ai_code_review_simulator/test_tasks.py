import unittest
from datetime import date, timedelta, timezone
from tasks import Task, TaskManager, SortAttribute

class TestTaskMethods(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Buy groceries", "Milk, Bread, Eggs")
        self.assertEqual(task.title, "Buy groceries")
        self.assertEqual(task.status, "pending")
        self.assertIsNone(task.due_date)
        # Validation: Verify timezone-aware date markers applied
        self.assertEqual(task.created_at.tzinfo, timezone.utc)
        
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

    def test_task_tags_formatted_lowercase(self):
        # Validation: Ensure add_tag lowercase formatting logic applies successfully
        task = Task("Code review")
        task.add_tag("PYTHON")
        task.add_tag("JavaScript")
        self.assertIn("python", task.tags)
        self.assertIn("javascript", task.tags)
        self.assertNotIn("PYTHON", task.tags)

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

    def test_sort_tasks_enum_logic(self):
        # Validation: Verify that sort_tasks strictly adheres to the SortAttribute Enum framework
        self.manager.add_task("Zeta Task")
        self.manager.add_task("Alpha Task")
        
        sorted_via_string = self.manager.sort_tasks(by="title")
        self.assertEqual(sorted_via_string[0].title, "Alpha Task")
        
        with self.assertRaises(ValueError):
            self.manager.sort_tasks(by="unsupported_sort_key")

    def test_count_overdue_and_summary(self):
        # Validation: Test the natively implemented summary mapping and custom count_overdue iterator
        yesterday = date.today() - timedelta(days=1)
        today = date.today()
        
        t1 = self.manager.add_task("Pending Overdue", due_date=yesterday)
        t2 = self.manager.add_task("Done Normal Task", due_date=today)
        t2.mark_completed()
        
        self.assertEqual(self.manager.count_overdue(), 1)
        
        summary = self.manager.summary()
        self.assertEqual(summary['total'], 2)
        self.assertEqual(summary['pending'], 1)
        self.assertEqual(summary['completed'], 1)
        self.assertEqual(summary['overdue'], 1)

if __name__ == "__main__":
    unittest.main()
