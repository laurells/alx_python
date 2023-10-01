import requests
import sys
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
            "USER_ID": employee_id,
            "USERNAME": employee_name,
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

        # Serialize to JSON
        json_filename = f"{employee_id}.json"
        with open(json_filename, "w") as json_file:
            json.dump(employee_tasks, json_file, indent=4)

        print(f"Data exported to {json_filename}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except KeyError:
        print("Invalid employee ID or data format.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
    else:
        employee_id = int(sys.argv[1])
        get_employee_info(employee_id)
