SELECT Title FROM movies;
SELECT director FROM movies;
SELECT Title, Directory FROM movies;
SELECT Title, year FROM movies;
SELECT * from movies;
-- not case sensitive
-- SELECT column, another_column, …
-- FROM mytable
-- WHERE condition
--     AND/OR another_condition
--     AND/OR …;
SELECT * FROM movies where id = 6;
SELECT * FROM movies where year BETWEEN 2000 AND 2010;
SELECT * FROM movies where year BETWEEN 2000 AND 2010;
SELECT * FROM movies where id < 6;

-- (String) filtering
SELECT * FROM movies WHERE Title like "Toy Story%";
SELECT * FROM movies WHERE Director = "John Lasseter";
SELECT * FROM movies WHERE Director = "John Lasseter";
SELECT * FROM movies WHERE Title LIKE "WALL-%";
-- SELECT * FROM movies WHERE Title LIKE "WALL-_";

-- ORDER BY AND LIMIT
SELECT DISTINCT Director FROM movies ORDER BY Director;
SELECT * FROM movies ORDER BY Year DESC LIMIT 4;
SELECT * FROM movies ORDER BY Title LIMIT 5;
SELECT * FROM movies ORDER BY Title LIMIT 5 OFFSET 5;

SELECT City, Population FROM north_american_cities WHERE Country = "Canada";
SELECT * FROM north_american_cities WHERE Country = "United States" ORDER BY Latitude DESC;
-- nested query/subquery
SELECT * FROM north_american_cities WHERE Longitude < (SELECT Longitude FROM north_american_cities WHERE City = "Chicago") ORDER BY Longitude ASC;
SELECT * FROM north_american_cities WHERE Country = "Mexico" ORDER BY population DESC LIMIT 2;
SELECT City, population FROM north_american_cities WHERE Country = "United States" ORDER BY population DESC LIMIT 2 OFFSET 2;

-- Inner join
-- Find the domestic and international sales for each movie
SELECT Title, Domestic_sales, International_sales FROM movies INNER JOIN Boxoffice on movies.id = boxoffice.movie_id;
-- Don't need to give table.id as it is uncommon amongst them and so no confusions can happen
SELECT Title, Domestic_sales, International_sales FROM movies INNER JOIN Boxoffice on id = movie_id;
-- Show the sales numbers for each movie that did better internationally rather than domestically
SELECT Title, Domestic_sales, International_sales FROM movies INNER JOIN Boxoffice on movies.id = boxoffice.movie_id WHERE International_sales > Domestic_sales;
-- List all the movies by their ratings in descending orde
SELECT Title, Rating FROM movies INNER JOIN boxoffice WHERE movies.id = boxoffice.movie_id ORDER BY Rating DESC;

-- Find the list of all buildings that have employees
SELECT Distinct Building FROM Employees;
-- Find the list of all buildings and their capacity 
SELECT * FROM Buildings;
-- List all buildings and the distinct employee roles in each building (including empty buildings) 
SELECT DISTINCT building_name, role FROM Buildings LEFT JOIN Employees on building = building_name;

-- Find the name and role of all employees who have not been assigned to a building
SELECT * FROM employees LEFT JOIN Buildings on building = building_name WHERE building_name IS NULL;
-- Find the names of the buildings that hold no employees
SELECT * FROM Buildings LEFT JOIN employees on building = building_name WHERE Name IS NULL;

-- List all movies and their combined sales in millions of dollars 
SELECT Title, (International_sales + Domestic_sales) / 1000000 AS gross_millions FROM movies INNER JOIN Boxoffice WHERE id = movie_id;
-- List all movies and their ratings in percent
SELECT Title, rating * 10 AS rating_percentage FROM movies INNER JOIN Boxoffice WHERE id = movie_id;
-- List all movies that were released on even number years
SELECT Title, Year FROM movies WHERE Year % 2 = 0;

-- Find the longest time that an employee has been at the studio
SELECT MAX(Years_employed) AS Max_years_employed FROM employees;
-- For each role, find the average number of years employed by employees in that role
SELECT role, AVG(Years_employed) AS Avg_Years_Employed FROM employees GROUP BY role;
-- Find the total number of employee years worked in each building
SELECT Building, SUM(Years_employed) AS Total_number_of_employee_years FROM employees GROUP BY Building;
-- The HAVING clause constraints are written the same way as the WHERE clause constraints
-- , and are applied to the grouped rows. With our examples, this might not seem like 
-- a particularly useful construct, but if you imagine data with millions of rows with 
-- different properties, being able to apply additional constraints is often necessary 
-- to quickly make sense of the data.

-- Find the number of Artists in the studio (without a HAVING clause)
SELECT Role, COUNT(Role) AS Number_of_artists FROM employees WHERE role = "Artist";
-- Find the number of Employees of each role in the studio
SELECT role, COUNT(*) AS Num_employees FROM employees GROUP BY role;
-- Find the total number of years employed by all Engineers
SELECT Role, SUM(Years_Employed) AS total_years_employed_by_all FROM employees WHERE role = "Engineer";
-- Or
SELECT role, SUM(years_employed) AS total_years_employed_by_all FROM employees GROUP BY role HAVING role = "Engineer";

-- Find the number of movies each director has directed 
SELECT Director, COUNT(*) AS num_movies_directed FROM movies GROUP BY Director;
-- Find the total domestic and international sales that can be attributed to each director
SELECT Director, SUM(International_sales) + SUM(Domestic_sales) AS gross_total_sales_by_director 
FROM movies 
    INNER JOIN boxoffice 
        ON id = movie_id 
GROUP BY Director;
-- Or
SELECT director, SUM(domestic_sales + international_sales) as Cumulative_sales_from_all_movies
FROM movies
    INNER JOIN boxoffice
        ON movies.id = boxoffice.movie_id
GROUP BY director;