create table IF NOT EXISTS countries.region( ID INT,NAME VARCHAR(255));
CREATE TABLE IF NOT EXISTS COUNTRIES.SUB_REGION(ID INT,NAME VARCHAR(255));

INSERT INTO region (ID, NAME) VALUES
(1, 'Asia'),
(2, 'Europe'),
(3, 'Africa'),
(4, 'North America'),
(5, 'South America'),
(6, 'Oceania'),
(7, 'Antarctica');

INSERT INTO COUNTRIES.SUB_REGION (ID, NAME) VALUES
(1, 'South Asia'),
(2, 'Southeast Asia'),
(3, 'East Asia'),
(4, 'Western Europe'),
(5, 'Eastern Europe'),
(6, 'Northern Africa'),
(7, 'Sub-Saharan Africa'),
(8, 'Caribbean'),
(9, 'Central America'),
(10, 'Southern America'),
(11, 'Pacific Islands');

SELECT * FROM COUNTRIES.REGION;
SELECT NAME FROM countries.sub_region;

-- SAME COLUMN CAN BE PRINTED MULTIPLE TIMES
SELECT *,ID FROM countries.sub_region;

-- Alising id as country_id
select  id as country_id from countries.region;
-- without using as 
select 
	id country_id,
    name country_name from countries.region;
-- if you are giving space for column name then use quotes
select 
	id 'country id'
    from countries.sub_region;
-- alias to the database 
-- if  you use alis then use updated database name otherwise it will throw error
select c.name from countries.countries as c;
