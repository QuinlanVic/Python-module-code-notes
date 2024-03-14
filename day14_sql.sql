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
-- Or - Don't need to give table.id as it is uncommon amongst them and so no confusions can happen
SELECT Title, Domestic_sales, International_sales FROM movies INNER JOIN Boxoffice on id = movie_id;
-- Show the sales numbers for each movie that did better internationally rather than domestically
SELECT Title, Domestic_sales, International_sales FROM movies INNER JOIN Boxoffice on movies.id = boxoffice.movie_id WHERE International_sales > Domestic_sales;
-- List all the movies by their ratings in descending order
SELECT Title, Rating FROM movies INNER JOIN boxoffice WHERE movies.id = boxoffice.movie_id ORDER BY Rating DESC;

-- Find the list of all buildings that have employees
SELECT Distinct Building FROM Employees;
-- Find the list of all buildings and their capacity 
SELECT * FROM Buildings;
-- List all buildings and the distinct employee roles in each building (including empty buildings) 
SELECT DISTINCT building_name, role FROM Buildings LEFT JOIN Employees on building = building_name;

-- LESSON 8
-- Find the name and role of all employees who have not been assigned to a building
SELECT * FROM employees LEFT JOIN Buildings on building = building_name WHERE building_name IS NULL;
-- Or (Don't need join)
SELECT Name, Role FROM employees WHERE Building IS NULL;
-- Find the names of the buildings that hold no employees
SELECT * FROM Buildings LEFT JOIN employees on building = building_name WHERE Name IS NULL;
-- Or 
SELECT DISTINCT building_name FROM Buildings LEFT JOIN employees on building = building_name WHERE Building IS NULL;

-- LESSON 9
-- List all movies and their combined sales in millions of dollars 
SELECT Title, (International_sales + Domestic_sales) / 1000000 AS gross_millions FROM movies INNER JOIN Boxoffice ON id = movie_id;
-- List all movies and their ratings in percent
SELECT Title, rating * 10 AS rating_percentage FROM movies INNER JOIN Boxoffice ON id = movie_id;
-- List all movies that were released on even number years. % = MODULUS OPERATOR)
SELECT Title, Year FROM movies WHERE Year % 2 = 0;

-- Find the longest time that an employee has been at the studio
SELECT *, MAX(Years_employed) AS Max_years_employed FROM employees;
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
-- Or
SELECT role, COUNT(role) AS total_artists FROM employees GROUP BY role HAVING role = "Artist";
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

-- ORDER MATTERS
-- Complete SELECT query!!!!!
-- SELECT DISTINCT column, AGG_FUNC(column_or_expression), …
-- FROM mytable
--     JOIN another_table
--       ON mytable.column = another_table.column
--     WHERE constraint_expression
--     GROUP BY column
--     HAVING constraint_expression
--     ORDER BY column ASC/DESC
--     LIMIT count OFFSET COUNT;

-- INSERTS
-- Add the studio's new production, Toy Story 4 to the list of movies (you can use any director)
INSERT into movies VALUES (11, "Toy Story 4", "John Lasseter", 2019, 90);
-- or (specify columns)
INSERT INTO movies (Title, Director, Year, Length_minutes) VALUES ("Toy Story 4", "John Lasseter", 2019, 90)
-- or (include id specifically so it isn't added at the end)
INSERT INTO movies (id, Title, Director, Year, Length_minutes) VALUES (11, "Toy Story 4", "John Lasseter", 2019, 90)

-- Toy Story 4 has been released to critical acclaim! It had a rating of 8.7, and made 340 million domestically and 270 million internationally. Add the record to the BoxOffice table.
-- have to ensure ids are the same
INSERT INTO boxoffice VALUES (11, 8.7, 340000000, 270000000)

-- UPDATES
-- Write SET then WHERE
-- UPDATE mytable
-- SET column = value_or_expr, 
--     other_column = another_value_or_expr, 
--     …
-- WHERE condition;

-- Or you can use *ID* AS IT IS UNIQUE and other titles could be the same!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-- The director for A Bug's Life is incorrect, it was actually directed by John Lasseter
UPDATE Movies
    SET Director = "John Lasseter"
        WHERE title = "A Bug's Life";

    SET Director = "John Lasseter"
        WHERE id = _;
-- The year that Toy Story 2 was released is incorrect, it was actually released in 1999
UPDATE Movies
    SET Year = 1999
        WHERE title = "Toy Story 2";
-- Both the title and director for Toy Story 8 is incorrect! The title should be "Toy Story 3" and it was directed by Lee Unkrich
UPDATE movies
    SET title = "Toy Story 3", Director = "Lee Unkrich"
        WHERE title = "Toy Story 8";

-- DELETES
-- DELETE FROM mytable
-- WHERE condition;
-- NB! Use SELECT BEFORE DELETE TO MAKE SURE YOU ARE DELETING THE RIGHT STUFF
-- This database is getting too big, lets remove all movies that were released before 2005.
SELECT * FROM movies WHERE Year < 2005;
DELETE FROM movies WHERE Year < 2005;
-- Andrew Stanton has also left the studio, so please remove all movies directed by him.
SELECT * from movies WHERE Director = "Andrew Stanton";
DELETE FROM MOVIES WHERE Director = "Andrew Stanton";

-- BEEN LEARNING DML (Data Manipulation Language) commands (only changes data in tables)
-- NOW LEARNING DDL (Data Definition Language) commands (now changing tables themselves)

-- CREATE TABLES
-- CREATE TABLE IF NOT EXISTS mytable (
--     column DataType TableConstraint DEFAULT default_value,
--     another_column DataType TableConstraint DEFAULT default_value,
--     …
-- );
-- Table Schema
-- CREATE TABLE movies (
--     id INTEGER PRIMARY KEY,
--     title TEXT,
--     director TEXT,
--     year INTEGER, 
--     length_minutes INTEGER
-- );

-- Create a new table named Database with the following columns:
-- Name A string (text) describing the name of the database
-- Version A number (floating point) of the latest version of this database
-- Download_count An integer count of the number of times this database was downloaded
-- This table has no constraints. 
CREATE TABLE IF NOT EXISTS Database (
    -- id INTEGER PRIMARY KEY
    Name TEXT,
    Version FLOAT,
    Download_count INTEGER
);

-- ALTERING TABLES
-- Add a column named Aspect_ratio with a FLOAT data type to store the aspect-ratio each movie was released in. 
-- Don't need the COLUMN keyword
ALTER TABLE Movies
  ADD COLUMN Aspect_ratio FLOAT DEFAULT 2.39;
-- Add another column named Language with a TEXT data type to store the language that the movie was released in. 
-- Ensure that the default for this language is English. 
ALTER TABLE Movies
  ADD COLUMN Language TEXT DEFAULT "English";

-- Dropping tables
-- Fails silently if the table does not exist
-- Drop the movies table
DROP TABLE IF EXISTS movies;
-- And drop the BoxOffice table as well
DROP TABLE IF EXISTS BoxOffice;

