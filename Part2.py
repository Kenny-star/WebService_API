import requests

inp = ""
myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,' 'image/webp,/;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 ' 'Firefox/93.0'}


def updateEmployee(employee_id):
    new_name = input("Enter a new name: ")
    response = requests.put("http://dummy.restapiexample.com/api/v1/update/" + employee_id, headers=myHeader,
                            data={'employee_name': new_name})
    while response.status_code != 200:
        response
    print(response)


def deleteEmployee(employee_id, employee_name):
    fetched_employee = requests.get("http://dummy.restapiexample.com/api/v1/employee/" + employee_id, headers=myHeader)
    while fetched_employee.status_code != 200:
        fetched_employee
    print(fetched_employee)
    employee_formatted = fetched_employee.json()
    print(employee_formatted)
    while employee_formatted['data']['employee_name'] != employee_name:
        employee_name = input("Employee Name: ")
        if employee_formatted['data']['employee_name'] == employee_name:
            requests.delete("http://dummy.restapiexample.com/api/v1/delete/" + employee_id, headers=myHeader)
            print("\nEmployee Deleted Successfully!\n\n")


def createEmployee(salary, name, age):
    json_obj = {"name": name, "salary": salary, "age": age}
    response = requests.post("http://dummy.restapiexample.com/api/v1/create", headers=myHeader, data=json_obj)
    while response.status_code != 200:
        response
    print(response.json())


def listEmployees():
    response = requests.get("http://dummy.restapiexample.com/api/v1/employees", headers=myHeader)
    while response.status_code != 200:
        response
    json_object = response.json()
    for i in range(len(json_object['data'])):
        if i % 10 == 0 and i != 0:
            answer = input("Do you want to continue? ('ENTER KEY'/N-n): \n")

            if "N" in answer or "n" in answer:
                break

            elif answer == "":
                print(json_object['data'][i])
                continue

        print(json_object['data'][i])


def showDetail(employee_id):
    response = requests.get("http://dummy.restapiexample.com/api/v1/employee/" + employee_id, headers=myHeader)
    while response.status_code != 200:
        response
    json_object = response.json()
    print(json_object)


def showAverage():
    total_salary = 0
    response = requests.get("http://dummy.restapiexample.com/api/v1/employees", headers=myHeader)
    while response.status_code != 200:
        response
    json_object = response.json()
    for employee in json_object['data']:
        print(employee)
        total_salary += employee['employee_salary']

    average_salary = "${:,.2f}".format(total_salary / len(json_object['data']))
    print(average_salary + "\n")


def showInfo(max_age, min_age):
    total_salary = 0
    highest_salary = 0
    lowest_salary = 0
    response = requests.get("http://dummy.restapiexample.com/api/v1/employees", headers=myHeader)
    while response.status_code != 200:
        response
    json_object = response.json()
    employee = json_object['data']
    for i in range(len(json_object['data'])):
        if int(min_age) <= employee[i]['employee_age'] <= int(max_age):
            total_salary += employee[i]['employee_salary']
            if highest_salary == 0 and lowest_salary == 0:
                highest_salary = employee[i]['employee_salary']
                lowest_salary = employee[i]['employee_salary']
            if highest_salary < employee[i]['employee_salary']:
                highest_salary = employee[i]['employee_salary']
            elif lowest_salary >= employee[i]['employee_salary']:
                lowest_salary = employee[i]['employee_salary']
            else:
                continue

    average_salary = "${:,.2f}".format(total_salary / len(json_object['data']))
    print("Highest salary: " + str(highest_salary))
    print("Lowest salary: " + str(lowest_salary))
    print("Average salary: " + str(average_salary))


def checkOption(option):
    if option == 1:
        print("Employee ID: ", end="")
        employee_id = input()
        updateEmployee(employee_id)

    if option == 2:
        print("Employee ID: ", end="")
        employee_id = input()
        print("Employee Name: ", end="")
        employee_name = input()
        deleteEmployee(employee_id, employee_name)

    if option == 3:
        print("Salary: ", end="")
        salary = input()
        print("Name: ", end="")
        name = input()
        print("Age: ", end="")
        age = input()

        createEmployee(salary, name, age)

    if option == 4:
        listEmployees()

    if option == 5:
        print("Id: ", end="")
        employee_id = input()
        showDetail(employee_id)

    if option == 6:
        showAverage()

    if option == 7:
        print("Max age: ", end="")
        max_age = input()
        print("Min age: ", end="")
        min_age = input()
        showInfo(max_age,min_age)


while "q" not in inp and "Q" not in inp:
    print("=====================\nWelcome to the main menu")
    print("please enter a number")
    print("1. Updates an employee name based on the ID")
    print("2. Deletes an employee based on the employee ID")
    print("3. Creates an employee with salary, name and age")
    print("4. Fetches all employees")
    print("5. Shows the salary, age, and name of an employee")
    print("6. Shows the salary, age, and name of an employee")
    print("7. Shows age info")
    print("q or Q. Quit\n=====================")

    print("\nOption:", end="")
    inp = input()
    checkOption(int(inp))
