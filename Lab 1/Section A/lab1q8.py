def highest_paid(employees):
    return max(employees, key=lambda e: e["salary"])

employees = [
    {"name": "Abdul Wali", "department": "CS", "salary": 88000},
    {"name": "Tahzeeb Khan", "department": "CS", "salary": 84000},
    {"name": "Maaz Hussain", "department": "CS", "salary": 108000},
]

print(f"Highest paid employee: {highest_paid(employees)}")