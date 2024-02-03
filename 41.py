name = ["Abhra","Suka","Indra","Shoob"]
salary = [500000, 600000, 700000, 800000]

if len(name)!=len(salary):
    print("Error: The lists must have same length")
else:
    employee_salary = dict(zip(name, salary))
    print("The dictionary is:",employee_salary)