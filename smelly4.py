def add_task(task_list, task_name, task_due_date):
    task = {'name': task_name, 'due_date': task_due_date, 'completed': False}
    task_list.append(task)

def remove_task(task_list, task_name):
    return [task for task in task_list if task['name'] != task_name]

def display_tasks(task_list):
    print("All Tasks:")
    for task in task_list:
        print(f"Task: {task['name']}, Due: {task['due_date']}, Completed: {task['completed']}")

def mark_task_completed(task_list, task_name):
    try:
        task_index = next(i for i, task in enumerate(task_list) if task['name'] == task_name)
        task_list[task_index]['completed'] = True
    except StopIteration:
        print("Task not found.")
tasks = []

add_task(tasks, "Fix bug in code", "2024-02-21")
add_task(tasks, "Update documentation", "2024-02-22")
display_tasks(tasks)

mark_task_completed(tasks, "Fix bug in code")
tasks = remove_task(tasks, "Update documentation")

display_tasks(tasks)