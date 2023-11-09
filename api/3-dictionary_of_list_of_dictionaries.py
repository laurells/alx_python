import json
import requests

# Function to fetch tasks for a given user ID
def fetch_user_tasks(user_id):
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        return []  # Return an empty list if there was an error
    return todos_response.json()

# Function to fetch all user IDs
def fetch_user_ids():
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    if users_response.status_code != 200:
        return []  # Return an empty list if there was an error
    return [user["id"] for user in users_response.json()]

# Function to export data in JSON format for all tasks from all employees
def export_todo_all_employees():
    all_employee_data = {}

    user_ids = fetch_user_ids()
    for user_id in user_ids:
        user_tasks = fetch_user_tasks(user_id)
        employee_name = user_tasks[0]["username"] if user_tasks else "Unknown Employee"
        
        #a list of tasks for the current user
        employee_tasks = [{"username": employee_name, "task": task["title"], "completed": task["completed"]} for task in user_tasks]
        
        
        all_employee_data[user_id] = employee_tasks

    # Export data to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employee_data, json_file, indent=4)

if __name__ == "__main__":
    export_todo_all_employees()