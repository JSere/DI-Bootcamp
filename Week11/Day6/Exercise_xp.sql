-- Exercise 1
CREATE TABLE df_employee AS
SELECT 
    employee_id || '_' || CAST(date AS TEXT) AS id,  
    DATE(date) AS month_year,  
    employee_id, 
    employee_name, 
    gender,  
    age, 
    salary, 
    function_group, 
    company_name, 
    company_city, 
    company_state, 
    company_type, 
    const_site_category
FROM (
    SELECT * 
    FROM employees
    LEFT JOIN salaries USING (employee_id)
    LEFT JOIN functions USING (function_id)
    LEFT JOIN company USING (company_id)
) emp_dataset;

-- Exercise 2
SELECT *
FROM df_employee;

UPDATE df_employee
SET id = TRIM(id),
    month_year = TRIM(month_year),
    employee_id = TRIM(employee_id),
    employee_name = TRIM(employee_name),
    gender = TRIM(gender),
    age = TRIM(age),
    salary = TRIM(salary),
    function_group = TRIM(function_group),
    company_name = TRIM(company_name),
    company_city = TRIM(company_city),
    company_state = TRIM(company_state),
    company_type = TRIM(company_type),
    const_site_category = TRIM(const_site_category);

SELECT *
FROM df_employee
WHERE id IS NULL
   OR month_year IS NULL
   OR employee_id IS NULL
   OR employee_name IS NULL
   OR gender IS NULL
   OR age IS NULL
   OR salary IS NULL
   OR function_group IS NULL
   OR company_name IS NULL
   OR company_city IS NULL
   OR company_state IS NULL
   OR company_type IS NULL
   OR const_site_category IS NULL;

DELETE FROM df_employee
WHERE salary = ' ' 
   OR salary IS NULL
   OR id IS NULL
   OR month_year IS NULL
   OR employee_id IS NULL;

-- Exercise 3
SELECT company_name, COUNT(DISTINCT employee_id) AS current_employee_count
FROM df_employee
WHERE month_year = (SELECT MAX(month_year) FROM df_employee)
GROUP BY company_name;

-- Exercise 4
SELECT 
    company_city, 
    COUNT(DISTINCT employee_id) AS total_employees,
    (COUNT(DISTINCT employee_id) * 100.0 / (SELECT COUNT(DISTINCT employee_id) FROM df_employee)) AS percentage
FROM df_employee
GROUP BY company_city;

SELECT 
    month_year, 
    COUNT(DISTINCT employee_id) AS total_employees
FROM df_employee
GROUP BY month_year;

SELECT 
    AVG(employee_count) AS avg_monthly_employees
FROM (
    SELECT month_year, COUNT(DISTINCT employee_id) AS employee_count
    FROM df_employee
    GROUP BY month_year
);

-- Exercise 5
WITH monthly_counts AS (
    SELECT month_year, COUNT(DISTINCT employee_id) AS emp_count
    FROM df_employee
    GROUP BY month_year
)
SELECT 
    (SELECT month_year FROM monthly_counts ORDER BY emp_count ASC LIMIT 1) AS min_month,
    (SELECT MIN(emp_count) FROM monthly_counts) AS min_employees,
    (SELECT month_year FROM monthly_counts ORDER BY emp_count DESC LIMIT 1) AS max_month,
    (SELECT MAX(emp_count) FROM monthly_counts) AS max_employees;

SELECT 
    month_year, 
    function_group, 
    COUNT(DISTINCT employee_id) AS avg_monthly_employees
FROM df_employee
GROUP BY month_year, function_group;

SELECT 
    STRFTIME('%Y', month_year) AS year,
    AVG(CAST(salary AS NUMERIC)) AS annual_average_salary
FROM df_employee
GROUP BY STRFTIME('%Y', month_year);