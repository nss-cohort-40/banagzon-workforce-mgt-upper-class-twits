INSERT INTO hrapp_trainingprogram
  (training_title, start_date, end_date, max_capacity)
VALUES
  ("M&A", "04/02/0323", "04/02/0323", 1);

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
