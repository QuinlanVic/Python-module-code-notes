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

