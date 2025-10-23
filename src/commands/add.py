def add_task(title, description):
    import json
    import os
    from uuid import uuid4

    tasks_file = 'data/tasks.json'

    # Ensure the tasks file exists
    if not os.path.exists(tasks_file):
        with open(tasks_file, 'w') as f:
            json.dump([], f)

    # Load existing tasks
    with open(tasks_file, 'r') as f:
        tasks = json.load(f)

    # Create a new task
    task = {
        'id': str(uuid4()),
        'title': title,
        'description': description
    }

    # Add the new task to the list
    tasks.append(task)

    # Save the updated tasks back to the file
    with open(tasks_file, 'w') as f:
        json.dump(tasks, f)