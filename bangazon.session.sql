INSERT INTO hrapp_department
    (department_name, department_budget)
VALUES
    ("Sales", 100000),
    ("Technology", 150000);


UPDATE hrapp_employee
SET department_id = 1
WHERE id = 1
