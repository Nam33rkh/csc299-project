import unittest
import json
import os
from src.commands.add import add_task
from src.commands.list import list_tasks
from src.commands.search import search_tasks

class TestTaskManagement(unittest.TestCase):

    def setUp(self):
        self.test_file = 'data/tasks.json'
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_task(self):
        add_task("Test Task 1", "This is a test task.")
        tasks = list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['title'], "Test Task 1")
        self.assertEqual(tasks[0]['description'], "This is a test task.")

    def test_list_tasks(self):
        add_task("Test Task 1", "This is a test task.")
        add_task("Test Task 2", "This is another test task.")
        tasks = list_tasks()
        self.assertEqual(len(tasks), 2)

    def test_search_tasks(self):
        add_task("Test Task 1", "This is a test task.")
        add_task("Test Task 2", "This is another test task.")
        results = search_tasks("another")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], "Test Task 2")

if __name__ == '__main__':
    unittest.main()