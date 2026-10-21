-- Step 1: Create the employees table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date VARCHAR(20),
    department VARCHAR(50)
);

-- Step 2: Insert the 20 sample records
INSERT INTO employees (employee_id, employee_name, salary, hire_date, department) VALUES
(1, 'Amy West', 60000.00, '2021-01-15', 'HR'),
(2, 'Ivy Lee', 75000.50, '2020-05-22', 'Sales'),
(3, 'joe smith', 80000.75, '2019-08-10', 'Marketing'), 
(4, 'John White', 90000.00, '2020-11-05', 'Finance'),
(5, 'Jane Hill', 55000.25, '2022-02-28', 'IT'),
(6, 'Dave West', 72000.00, '2020-03-12', 'Marketing'),
(7, 'Fanny Lee', 85000.50, '2018-06-25', 'Sales'),
(8, 'Amy Smith', 95000.25, '2019-11-30', 'Finance'),
(9, 'Ivy Hill', 62000.75, '2021-07-18', 'IT'),
(10, 'Joe White', 78000.00, '2022-04-05', 'Marketing'),
(11, 'John Lee', 68000.50, '2018-12-10', 'HR'),
(12, 'Jane West', 89000.25, '2017-09-15', 'Sales'),
(13, 'Dave Smith', 60000.75, '2022-01-08', NULL),
(14, 'Fanny White', 72000.00, '2019-04-22', 'IT'),
(15, 'Amy Hill', 84000.50, '2020-08-17', 'Marketing'),
(16, 'Ivy West', 92000.25, '2021-02-03', 'Finance'),
(17, 'Joe Lee', 58000.75, '2018-05-28', 'IT'),
(18, 'John Smith', 77000.00, '2019-10-10', 'HR'),
(19, 'Jane Hill', 81000.50, '2022-03-15', 'Sales'),
(20, 'Dave White', 70000.25, '2017-12-20', 'Marketing');

-- Step 3: Create a cleaned and transformed staging table (Handling Missing Values & Data Types)
CREATE TABLE cleaned_employees AS
SELECT 
    employee_id,
    -- Standardize name formatting (Title Case)
    INITCAP(TRIM(employee_name)) AS employee_name,
    salary,
    -- Ensure hire_date is properly formatted as a DATE data type
    DATE(hire_date) AS hire_date,
    -- Handle missing values in department by assigning a default value
    COALESCE(NULLIF(TRIM(department), ''), 'Unassigned') AS department
FROM employees
WHERE salary IS NOT NULL AND hire_date IS NOT NULL;

-- Step 4: Eliminate duplicate rows (if any exist based on employee_id)
DELETE FROM cleaned_employees
WHERE rowid NOT IN (
    SELECT MIN(rowid)
    FROM cleaned_employees
    GROUP BY employee_id
);

-- Step 5: Address outliers (e.g., filtering out unrealistic salaries if applicable, or viewing them)
-- For example, standardizing/filtering out extreme anomalies:
DELETE FROM cleaned_employees
WHERE salary < 0;

-- Step 6: View the final cleaned and transformed dataset
SELECT * FROM cleaned_employees;