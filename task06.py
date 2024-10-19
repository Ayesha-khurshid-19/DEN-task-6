# todo_list of tasks

# Importing required modules
import os
import json

# Task Manager class
class TaskManager:
    def _init_(self, file_name="tasks.json"):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    # Load tasks from file
    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                return json.load(file)
        else:
            return []

    # Save tasks to file
    def save_tasks(self):
        with open(self.file_name, "w") as file:
            json.dump(self.tasks, file)

    # Add task
    def add_task(self):
        task_id = len(self.tasks) + 1
        description = input("Enter task description: ")
        self.tasks.append({"id": task_id, "description": description, "status": "pending"})
        self.save_tasks()
        print("Task added successfully!")

    # View tasks
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for task in self.tasks:
                print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

    # Remove task
    def remove_task(self):
        task_id = int(input("Enter task ID to remove: "))
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print("Task removed successfully!")
                return
        print("Task not found.")

    # Mark task as completed
    def mark_completed(self):
        task_id = int(input("Enter task ID to mark completed: "))
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "completed"
                self.save_tasks()
                print("Task marked completed!")
                return
        print("Task not found.")

    # Edit task
    def edit_task(self):
        task_id = int(input("Enter task ID to edit: "))
        for task in self.tasks:
            if task["id"] == task_id:
                task["description"] = input("Enter new description: ")
                self.save_tasks()
                print("Task edited successfully!")
                return
        print("Task not found.")

    # Search task
    def search_task(self):
        keyword = input("Enter keyword to search: ")
        found = False
        for task in self.tasks:
            if keyword.lower() in task["description"].lower():
                print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
                found = True
        if not found:
            print("No tasks found.")

    # Filter tasks
    def filter_tasks(self):
        status = input("Enter status (pending/completed): ")
        found = False
        for task in self.tasks:
            if task["status"] == status:
                print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
                found = True
        if not found:
            print("No tasks found.")

    # Clear all tasks
    def clear_tasks(self):
        confirm = input("Are you sure? (yes/no): ")
        if confirm.lower() == "yes":
            self.tasks = []
            self.save_tasks()
            print("All tasks cleared!")
        else:
            print("Operation cancelled.")

    # Sort tasks
    def sort_tasks(self):
        option = input("Sort by (id/status): ")
        if option == "id":
            self.tasks.sort(key=lambda x: x["id"])
        elif option == "status":
            self.tasks.sort(key=lambda x: x["status"])
        self.save_tasks()
        print("Tasks sorted successfully!")

# Main function
def main():
    task_manager = TaskManager()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task Completed")
        print("5. Edit Task")
        print("6. Search Task")
        print("7. Filter Tasks")
        print("8. Clear All Tasks")
        print("9. Sort Tasks")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_manager.add_task()
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_manager.remove_task()
        elif choice == "4":
            task_manager.mark_completed()
        elif choice == "5":
            task_manager.edit_task()
        elif choice == "6":
            task_manager.search_task()
        elif choice == "7":
            task_manager.filter_tasks()
        elif choice == "8":
            task_manager.clear_tasks()
        elif choice == "9":
            task_manager.sort_tasks()
        elif choice == "10":     
            os._exit(0)          

if __name__ == "__main__":
    main()