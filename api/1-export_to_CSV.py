import csv
import os
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

        # Check if the file exists before reading it
        if os.path.isfile(csv_file_name):
            with open(csv_file_name, mode='r') as csv_file:
                # Read the number of tasks in the CSV
                num_tasks = len(list(csv.reader(csv_file))) - 1  # Subtract 1 for the header row
                print(f"Number of tasks in CSV: {num_tasks}")
        else:
            print(f"CSV file {csv_file_name} does not exist.")

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
