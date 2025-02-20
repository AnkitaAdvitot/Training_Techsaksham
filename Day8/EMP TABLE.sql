CREATE TABLE EMP(EMPNO INT,
	ENAME VARCHAR(255),
    JOB VARCHAR(255),
    HIREDATE DATE,
    SAL INT);

INSERT INTO EMP (EMPNO, ENAME, JOB, HIREDATE, SAL) VALUES
(101, 'John Doe', 'Manager', '2020-05-15', 75000),
(102, 'Jane Smith', 'Analyst', '2021-08-20', 65000),
(103, 'Robert Brown', 'Developer', '2019-11-10', 55000),
(104, 'Emily Davis', 'HR', '2018-06-25', 48000),
(105, 'Michael Johnson', 'Sales Executive', '2022-01-15', 50000),
(106, 'Sarah White', 'Consultant', '2017-09-30', 70000),
(107, 'David Miller', 'Clerk', '2023-04-10', 40000),
(108, 'Chris Wilson', 'Project Manager', '2016-12-05', 90000);

SELECT * FROM EMP;
-- ALIASAING 
SELECT ENAME AS EMPLOYEE_NAME, 
	JOB AS JOB_TITLE,
    SAL AS MONTHLY_SALARY
    FROM EMP;

-- RETRUN TOP 5 SALARIES
SELECT * 
FROM EMP
ORDER BY SAL DESC LIMIT 5;