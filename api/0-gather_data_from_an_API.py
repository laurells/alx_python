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

        # Calculate progress
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo["completed"])

        # Display progress with the specified formatting
        print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
        
        # Display completed tasks
        for todo in todos_data:
            if todo["completed"]:
                print(f"     {todo['title']}")

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
