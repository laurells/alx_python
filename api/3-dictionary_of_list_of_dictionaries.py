import requests
import json

def get_employee_info(employee_id):
    try:
        # Fetch employee details
        employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        response = requests.get(employee_url)
        employee_data = response.json()
        employee_name = employee_data["name"]

        # Fetch employee's TODO list
        todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        response = requests.get(todos_url)
        todos_data = response.json()

        # Create a dictionary for the employee's tasks
        employee_tasks = {
            "username": employee_name,
            "tasks": []
        }

        # Populate the tasks list
        for todo in todos_data:
            task_completed_status = "Completed" if todo["completed"] else "Not Completed"
            task_entry = {
                "task": todo["title"],
                "completed": task_completed_status,
                "username": employee_name
            }
            employee_tasks["tasks"].append(task_entry)

        return employee_id, employee_tasks

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None, None
    except KeyError:
        print(f"Invalid employee ID or data format for employee {employee_id}")
        return None, None

def get_all_employees_todo():
    all_employees_data = {}

    # Fetch data for all employees
    for employee_id in range(1, 11):  # Assuming employee IDs from 1 to 10
        employee_id, employee_data = get_employee_info(employee_id)
        if employee_id is not None and employee_data is not None:
            all_employees_data[employee_id] = employee_data

    return all_employees_data

def export_to_json(data):
    json_filename = "todo_all_employees.json"
    with open(json_filename, "w") as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Data for all employees exported to {json_filename}")

if __name__ == "__main__":
    all_employees_data = get_all_employees_todo()
    export_to_json(all_employees_data)
