insert into hrapp_department (department_name, department_budget) values ("Human Resources", 100560);

select
            d.id,
            d.department_name,
            d.department_budget
        from hrapp_department d;

insert into hrapp_employee (first_name, last_name, start_date, is_supervisor, department_id) values ("Jane", "Doe", 03/20/2005, False, 1);
