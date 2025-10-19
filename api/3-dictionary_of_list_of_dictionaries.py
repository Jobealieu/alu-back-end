#!/usr/bin/python3
"""
Script that exports all employee TODO list data to JSON format.
Uses JSONPlaceholder API to fetch user and todo information.
"""
import json
import requests


if __name__ == "__main__":
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch all users
    users_response = requests.get(f"{base_url}/users")
    users = users_response.json()
    
    # Fetch all todos
    todos_response = requests.get(f"{base_url}/todos")
    todos = todos_response.json()
    
    # Create dictionary to store all employee tasks
    all_employees = {}
    
    # Process each user
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        
        # Filter todos for this user
        user_todos = [todo for todo in todos if todo.get("userId") == int(user_id)]
        
        # Create list of task dictionaries for this user
        task_list = []
        for todo in user_todos:
            task_dict = {
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
            task_list.append(task_dict)
        
        # Add to main dictionary
        all_employees[user_id] = task_list
    
    # Export to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employees, json_file)
