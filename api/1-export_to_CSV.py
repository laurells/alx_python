import csv
import requests
import sys

def get_employee_info(employee_id):
    try:
        # Fetch employee details
        employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        response = requests.get(employee_url)
        employee_data = response.json()
        employee_name = employee_data["name"]

        # Fetch employee's To-Do list
        todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        response = requests.get(todos_url)
        todos_data = response.json()

        # Prepare CSV file name
        csv_file_name = f"{employee_id}.csv"

        # Open CSV file for writing
        with open(csv_file_name, mode='w', newline='') as csv_file:
            fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            # Write CSV header
            writer.writeheader()

            # Write employee's tasks to CSV
            for todo in todos_data:
                writer.writerow({
                    "USER_ID": employee_id,
                    "USERNAME": employee_name,
                    "TASK_COMPLETED_STATUS": str(todo["completed"]),
                    "TASK_TITLE": todo["title"]
                })

        print(f"Data exported to {csv_file_name}")

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
