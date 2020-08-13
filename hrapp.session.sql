INSERT INTO hrapp_department
  (department_name, department_budget)
VALUES
  ("Human Resources", 150000);

SELECT
  e.id,
  e.first_name,
  e.last_name,
  e.department_id,
  d.id department_id,
  d.department_name
FROM hrapp_employee e
  JOIN hrapp_department d ON e.department_id = d.id
WHERE e.id = 1;

        SELECT
                c.id,
                c.make,
                c.purchase_date,
                c.decommission_date,
                c.manufacturer
            from hrapp_computer c
          