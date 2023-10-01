import requests
import sys
import csv

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

        # Create a CSV file for the employee
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, mode="w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            # Write TODO tasks to the CSV file
            for todo in todos_data:
                task_completed_status = "Completed" if todo["completed"] else "Not Completed"
                csv_writer.writerow([employee_id, employee_name, task_completed_status, todo["title"]])

        print(f"Data exported to {csv_filename}")

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
