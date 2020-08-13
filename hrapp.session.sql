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

INSERT INTO hrapp_computer
  (manufacturer, make, purchase_date, decommission_date)
VALUES
  ("apple", "air", "05/03/2300", "08/03/2039");
INSERT INTO hrapp_computer
  (manufacturer, make, purchase_date, decommission_date)
VALUES
  ("apple", "goggles", "05/03/2300", "08/03/2039");