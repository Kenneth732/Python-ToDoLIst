class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Not Done"
        return f"Title: {self.title}\nDescription: {self.description}\nStatus: {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                print(f"{title} marked as completed.")
                return
        print(f"Task with title '{title}' not found.")

# Create a ToDoList object
todo_list = ToDoList()


