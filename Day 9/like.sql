-- Like used to search pattern
-- % represents zero or more
-- _ represents single character

-- eemployee name starts with s
select ename from countries.emp where ename like 's%';

-- empoyee name ends with s
select ename from countries.emp where ename like '%s';

-- country name start with A and one character and s 
select name from countries.countries where name like 'A_s%';

-- 