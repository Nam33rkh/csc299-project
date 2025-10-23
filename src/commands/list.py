def list_tasks():
    import json
    import os

    tasks_file = os.path.join(os.path.dirname(__file__), '../../data/tasks.json')

    if not os.path.exists(tasks_file):
        print("No tasks found.")
        return

    with open(tasks_file, 'r') as file:
        tasks = json.load(file)

    if not tasks:
        print("No tasks available.")
        return

    for task in tasks:
        print(f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}")