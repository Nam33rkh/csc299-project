def search_tasks(search_term):
    import json
    from src.storage import load_tasks

    tasks = load_tasks()
    matching_tasks = [
        task for task in tasks if search_term.lower() in task['title'].lower() or search_term.lower() in task['description'].lower()
    ]
    return matching_tasks