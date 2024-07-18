class Task:
    def __init__(self, task_id, name, profile, gender):
        self.task_id = task_id
        self.name = name
        self.profile = profile
        self.gender = gender

    def __str__(self):
        return f"ID : {self.task_id}, Name : {self.name}, Profile : {self.profile}, Gender : {self.gender}"

def create_task(task_list):
    task_id = len(task_list) + 1
    name = input("Enter task name : ")
    profile = input("Enter task profile : ")
    gender = input("Enter task gender : ")
    new_task = Task(task_id, name, profile, gender)
    task_list.append(new_task)
    print("Task created successfully.")

def display_tasks(task_list):
    if not task_list:
        print("No tasks to display.")
    else:
        for task in task_list:
            print(task)

def update_task(task_list):
    task_id = int(input("Enter task ID to update : "))
    for task in task_list:
        if task.task_id == task_id:
            task.name = input("Enter new task name : ")
            task.profile = input("Enter new task profile : ")
            task.gender = input("Enter new task gender : ")
            print("Task updated successfully.")
            return
    print("Task not found.")

def delete_task(task_list):
    task_id = int(input("Enter task ID to delete : "))
    for task in task_list:
        if task.task_id == task_id:
            task_list.remove(task)
            print("Task deleted successfully.")
            return
    print("Task not found.")

def main():
    task_list = []
    
    while True:
        print("\nTask Manager")
        print("1. Create Task")
        print("2. Display Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice : ")
        
        if choice == '1':
            create_task(task_list)
        elif choice == '2':
            display_tasks(task_list)
        elif choice == '3':
            update_task(task_list)
        elif choice == '4':
            delete_task(task_list)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__" :
    main()