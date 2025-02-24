/* distinct*/

select distinct name from countries.countries;
-- when we give multiple columns with distinct then it checks whether whole row is repeated again 
-- if it is then it wont return it 
select distinct id,name from countries.region;
select distinct * from countries.sub_region;


