def search_employee(emp_list, emp_id, index=0):
    if index >= len(emp_list):
        return False
    
    if emp_list[index] == emp_id:
        return True
    
    return search_employee(emp_list, emp_id, index + 1)
#joshikhaa laasya


employees = [101, 102, 103, 104, 105]
emp_id = int(input("Enter employee ID to search: "))

if search_employee(employees, emp_id):
    print("Employee ID found!")
else:
    print("Employee ID not found.")
