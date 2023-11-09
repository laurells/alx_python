"""
Module Name: requests, json, sys
Description: This module provides functions for network call, command line argument and writing json files
"""
import requests
import sys
import json

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
employee_username = employee_data.get("username", "unknown employee")

json_filename = f"{employee_id}.json"


tasks_list = []

for task in todo_data:
    task_data = {
        "task": task["title"],
        "completed": task["completed"],
        "username": employee_username
    }
    tasks_list.append(task_data)


user_data = {f"USER_ID {employee_id}": tasks_list}


with open(json_filename, mode="w") as json_file:
    json.dump(user_data, json_file, indent=4)