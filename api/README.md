# API

This project contains Python scripts that interact with a REST API to manage and export employee TODO list data.

## Description

A collection of scripts that fetch employee data from the JSONPlaceholder API and export it in various formats (CSV, JSON). The project demonstrates working with APIs, data manipulation, and file handling in Python.

## Requirements

- Python 3.4.3
- Ubuntu 14.04 LTS
- `requests` or `urllib` module
- PEP 8 style compliance

## Files

| File | Description |
|------|-------------|
| `0-gather_data_from_an_API.py` | Fetches and displays employee TODO list progress |
| `1-export_to_CSV.py` | Exports employee tasks to CSV format |
| `2-export_to_JSON.py` | Exports employee tasks to JSON format |
| `3-dictionary_of_list_of_dictionaries.py` | Exports all employees' tasks to JSON |

## Usage

### Task 0: Gather data from API

bash
python3 0-gather_data_from_an_API.py <employee_id


Example:

bash
python3 0-gather_data_from_an_API.py 2

## API Reference

- Base URL: `https://jsonplaceholder.typicode.com`
- Endpoints used:
  - `/users/<id>` - Get user information
  - `/todos?userId=<id>` - Get user's TODO list

## Author

Alieu O. Jobe
