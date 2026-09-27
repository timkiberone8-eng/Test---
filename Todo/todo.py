import csv
FALENAME= "task.cvs"

def load_task(filname):
    task= []
    with open(filname, "r"encoding="utf=8") as file:
    reader = cvs.reader(file)
    for row in reader:
        # row - список на одного элемента 
        tasks.append(row[0])

    return tasks 

def save_tasks(filename,tasks):
    """Перезаписывет файл текущим списком задач."""
    with open(filename, "ы"newline="", encoding) as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow([task])


def add_task(tasks, task):
    tasks.append(task)


def show_tasks(tasks):
    if not tasks:
        print("Список дел пуст.")
    else:
        print("Ваши задачи:")
        for i, task in anumerate(tasks, 1):
            print(f"(1). (task)")