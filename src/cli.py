import json
import os
import sys
from src.commands.add import add_task
from src.commands.list import list_tasks
from src.commands.search import search_tasks

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [options]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 4:
            print("Usage: task-cli add <title> <description>")
            return
        title = sys.argv[2]
        description = sys.argv[3]
        add_task(title, description)
        print(f"Task '{title}' added.")
    
    elif command == "list":
        tasks = list_tasks()
        if tasks:
            for task in tasks:
                print(f"[{task['id']}] {task['title']}: {task['description']}")
        else:
            print("No tasks found.")
    
    elif command == "search":
        if len(sys.argv) < 3:
            print("Usage: task-cli search <term>")
            return
        term = sys.argv[2]
        results = search_tasks(term)
        if results:
            for task in results:
                print(f"[{task['id']}] {task['title']}: {task['description']}")
        else:
            print("No tasks found matching the search term.")
    
    else:
        print("Unknown command. Available commands: add, list, search.")

if __name__ == "__main__":
    main()