import json
import os


class Task:
    def __init__(self):
        self.FILENAME = "todo.json"

        if not os.path.exists(self.FILENAME):
            with open(self.FILENAME, "w") as f:
                json.dump([], f)

    def add_task(self, task_summary):
        task_summary = task_summary.strip()
        if not task_summary:
            return "Give some valid task"
        with open(self.FILENAME, "r") as f:
            data = json.load(f)
        l = []
        for i in data:
            l.append(int(i['id']))
        new_task = {
            "id": max(l) + 1,
            "task": task_summary,
            "status": "todo"
        }
        data.append(new_task)
        with open(self.FILENAME, "w") as f:
            json.dump(data, f, indent=4)
        print("Task added Successfully with id: {}".format(new_task['id']))

    def remove_task(self, id):
        with open(self.FILENAME, "r") as f:
            data = json.load(f)
            j = 0
            for i in data:
                j += 1
                if int(i["id"]) == id:
                    data.pop(j - 1)
                    with open(self.FILENAME, "w") as f:
                        json.dump(data, f, indent=4)
                    print("Task Removed Successfully for ID: {}".format(id))
                else:
                    print("No data with ID: {}".format(id))

    def run(self):
        run_app = True
        while run_app:
            print(" 1. Add task \n 2. Remove task \n 3. View tasks \n 4. Save \n 5. Exit")
            try:
                task = int(input("enter your choice"))
                if task <= 0 or task > 5:
                    print("Invalid Selection")
                    return "Invalid selection"
                elif task == 1:
                    Add_task = input("Enter the task")
                    self.add_task(Add_task)
                elif task == 2:
                    remove_task_id = int(input("Enter the id for the task to be deleted"))
                    self.remove_task(remove_task_id)
                elif task == 3:
                    with open(self.FILENAME, "r") as f:
                        data = json.load(f)
                        j = 1
                    for i in data:
                        print("Task{}: {}".format(j, i['task']))
                        j += 1
                elif task == 4:
                    print("All task are saved successfully")
                elif task == 5:
                    print("Exited")
                    run_app = False
            except ValueError:
                raise ValueError


t = Task()
t.run()
