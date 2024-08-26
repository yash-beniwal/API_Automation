from flask import Flask, request, jsonify

app = Flask(__name__)

employees = []
departments = []


@app.route('/employee/create', methods=['POST'])
def create_employee():
    data = request.json

    # Validation for required fields
    if 'EmpID' not in data or 'EmpName' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    emp_id = data.get('EmpID')
    emp_name = data.get('EmpName')
    dob = data.get('DOB')
    dept = data.get('Dept')

    # Check for null or invalid values
    if emp_id is None or emp_name is None:
        return jsonify({"error": "EmpID and EmpName cannot be null"}), 400

    # Duplicate check
    for emp in employees:
        if emp['EmpID'] == emp_id:
            return jsonify({"error": "Employee already exists"}), 409

    # Add the employee to the list
    employees.append({
        'EmpID': emp_id,
        'EmpName': emp_name,
        'DOB': dob,
        'Dept': dept
    })

    return jsonify({"message": "Employee created successfully"}), 201


@app.route('/department/create', methods=['POST'])
def create_department():
    data = request.json

    # Validation for required fields
    if 'DepID' not in data or 'DeptName' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    dep_id = data.get('DepID')
    dept_name = data.get('DeptName')

    # Check for null or invalid values
    if dep_id is None or dept_name is None:
        return jsonify({"error": "DepID and DeptName cannot be null"}), 400

    # Duplicate check
    for dept in departments:
        if dept['DepID'] == dep_id:
            return jsonify({"error": "Department already exists"}), 409

    # Add the department to the list
    departments.append({
        'DepID': dep_id,
        'DeptName': dept_name
    })

    return jsonify({"message": "Department created successfully"}), 201


if __name__ == '__main__':
    app.run(debug=True)
