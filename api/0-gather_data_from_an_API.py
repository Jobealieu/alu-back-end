#!/usr/bin/python3
"""
Script that gathers employee TODO list data from an API
and displays progress information
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get employee data
    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")
    
    # Get TODO list
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    # Calculate progress
    completed_tasks = [task for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)
    number_done = len(completed_tasks)
    
    # Display results
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_done, total_tasks))
    
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
