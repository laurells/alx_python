"""
Employee Task Data Exporter

This module retrieves task data for a specific employee from a remote API and exports it to a JSON file.

Usage:
    python script.py <employee_id>

Example:
    python script.py 1

Requirements:
    - requests library (install using 'pip install requests')

"""

import json
import requests
import sys


def get_employee_data(employee_id):
    # Define the API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        # Fetch user data
        user_response = requests.get(user_url)
        user_data = user_response.json()
        username = user_data.get('username')

        # Fetch TODO list data
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Create a list to store tasks for this employee
        user_tasks = []

        # Populate the user_tasks list
        for task in todos_data:
            task_data = {
                "task": task["title"],
                "completed": task["completed"],
                "username": username
            }
            user_tasks.append(task_data)

        # Write the data to a JSON file named USER_ID.json
        output_file = f"{employee_id}.json"
        with open(output_file, "w") as json_file:
            json.dump(user_tasks, json_file)

        print(f"Data exported to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)
