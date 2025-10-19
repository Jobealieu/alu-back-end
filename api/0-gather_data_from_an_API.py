#!/usr/bin/python3
"""Script to gather data from an API for a given employee ID"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch user data
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get("name")
    
    # Fetch todos for the employee
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos = todos_response.json()
    
    # Calculate completed tasks
    completed_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    number_of_done_tasks = len(completed_tasks)
    
    # Print the first line
    print(f"Employee {employee_name} is done with tasks"
          f"({number_of_done_tasks}/{total_tasks}):")
    
    # Print completed task titles
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
