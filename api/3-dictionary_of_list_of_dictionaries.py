import json
import requests
import sys

def fetch_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch data from {url}")
        sys.exit(1)
    return response.json()

def main(output_file):
    # Fetch user and tasks data
    users = fetch_data("https://jsonplaceholder.typicode.com/users")
    tasks = fetch_data("https://jsonplaceholder.typicode.com/todos")

    # Create a dictionary to store the tasks for each user
    user_tasks = {}

    # Populate the user_tasks dictionary
    for user in users:
        user_id = user["id"]
        username = user["username"]
        user_tasks[user_id] = []

        for task in tasks:
            if task["userId"] == user_id:
                task_data = {
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                }
                user_tasks[user_id].append(task_data)

    # Write the data to the output file in JSON format
    with open(output_file, "w") as json_file:
        json.dump(user_tasks, json_file)

    print(f"Data exported to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 3-dictionary_of_list_of_dictionaries.py <output_file>")
        sys.exit(1)

    output_file = sys.argv[1]
    main(output_file)
