insert into hrapp_department (department_name, department_budget) values ("Human Resources", 100560);

select
            d.id,
            d.department_name,
            d.department_budget
        from hrapp_department d;