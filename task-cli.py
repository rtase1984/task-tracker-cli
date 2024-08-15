import json
import sys
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'

# Initialize the JSON file if it doesn't exist
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w') as file:
        json.dump([], file)

def load_tasks():
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {
        'id': task_id,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
    print(f"Task {task_id} not found")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted successfully")

def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}")
            return
    print(f"Task {task_id} not found")

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    for task in tasks:
        print(f"{task['id']}. {task['description']} [{task['status']}]")

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        return
    
    command = sys.argv[1]

    if command == "add":
        description = sys.argv[2]
        add_task(description)
    elif command == "update":
        task_id = int(sys.argv[2])
        description = sys.argv[3]
        update_task(task_id, description)
    elif command == "delete":
        task_id = int(sys.argv[2])
        delete_task(task_id)
    elif command == "mark-in-progress":
        task_id = int(sys.argv[2])
        mark_task(task_id, "in-progress")
    elif command == "mark-done":
        task_id = int(sys.argv[2])
        mark_task(task_id, "done")
    elif command == "list":
        if len(sys.argv) > 2:
            status = sys.argv[2]
            list_tasks(status)
        else:
            list_tasks()
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
