#https://www.simplifiedpython.net/python-rest-api-example/
from bottle import run, get, post ,request,delete
employee  =  [{'name' : 'Sam','address':'Ranchi','Dept':'HR'},
              {'name': 'Sarah', 'address': 'Ranchi', 'Dept': 'MGR'},
              {'name': 'Arsh', 'address': 'Delhi', 'Dept': 'HR'}]

@get('/employee')
def getAllEmployee():
    return{'employees':employee}

@post('/employee')
def add_emp():
    new_emp = {'name' : request.json.get('name'),'address' : request.json.get('address'),'Dept':request.json.get('Dept')}
    employee.append(new_emp)
    return {'employees' : employee}

@delete('/employee/<name>')
def remove_emp(name):
    the_emp = [emp for emp in employee if emp['name'] == name]
    employee.remove(the_emp[0])
    return {'employees': employee}

@get('/employee/<name>')
def get_Emp_by_name(name):
    the_emp = [emp for emp in employee if emp['name'] == name]
    return{'employee' : the_emp[0]}