use countries;
-- return records whose poulation is greater than 200 million
select * from countries 
where (population/10)>200
order by population desc;
-- return records of employee who taken commission
select * from hr.emp
where comm>0
order by comm asc;

select * from customer_orders.order_items
where QUANTITY>4 and UNIT_PRICE>49;

-- return records 
select * from countries.countries 
where (POPULATION between 100 and 200) or (area_km2>5)
and  (Name not like '% %');

DROP TABLE IF EXISTS HR.SALES_PEOPLE;
create table hr.sales_people 
SELECT EMP_NO,E_NAME,JOB,MGR,HIRE_DATE,SAL+COMM  AS TOTAL_PAY 
FROM HR.EMP;

SET SQL_SAFE_UPDATES=0;
UPDATE  HR.SALES_PEOPLE 
SET JOB="SENIOR SALESMAN" 
WHERE TOTAL_PAY>2000;

select order_id,product_id,UNIT_PRICE,quantity,round(UNIT_PRICE*QUANTITY,1) as line_item_amount from customer_orders.order_items;
