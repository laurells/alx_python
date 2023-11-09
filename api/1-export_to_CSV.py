import csv
import requests
import sys

if len(sys.argv) != 2:
    sys.exit(1)

employee_id = int(sys.argv[1])

employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

employee_response = requests.get(employee_url)
todos_response = requests.get(todos_url)

if employee_response.status_code != 200 or todos_response.status_code != 200:
    sys.exit(1)

employee_data = employee_response.json()
todo_data = todos_response.json()
employee_name = employee_data.get("name", "unknown employee")
employee_username = employee_data.get("username", "unkown employee")

csv_filename = f"{employee_id}.csv"

with open(csv_filename, mode="w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

for task in todo_data:
        task_completed_status = "Completed" if task["completed"] else "Not Completed"
        csv_writer.writerow([employee_id, employee_username, task_completed_status, task["title"]])


with open(csv_filename, 'r') as f:
     pass