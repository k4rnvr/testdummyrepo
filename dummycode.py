import datetime

tasks = []

def add_task(title, due_date):
    task = {
        'title': title,
        'due_date': due_date,
        'created_at': datetime.datetime.now(),
        'done': False
    }
    tasks.append(task)
    print("Task added")

def list_tasks():
    for idx, task in enumerate(tasks):
        status = "✓" if task['done'] else "✗"
        print(f"{idx + 1}. {task['title']} - Due: {task['due_date']} - [{status}]")

def mark_done(index):
    try:
        tasks[index]['done'] = True
        print("Task marked as done")
    except:
        print("Invalid task index")

def delete_task(i):
    if i >= len(tasks):
        print("Index out of range")
    else:
        del tasks[i]
        print("Task deleted")

def overdue_tasks():
    today = datetime.datetime.now()
    for task in tasks:
        if not task['done'] and datetime.datetime.strptime(task['due_date'], '%Y-%m-%d') < today:
            print(f"Overdue: {task['title']}")