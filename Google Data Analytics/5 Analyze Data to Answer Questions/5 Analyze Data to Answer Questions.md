# Analyze Data to Answer Questions

# Organizing Data

> **Analysis**: The process used to make sense of the data collected.
> 

## Sorting and Filtering

Using SQL to filter data: 

```sql
SELECT _____
FROM   _____
WHERE _____  AND _____
```

## Sorting Data in Spreadsheets

> **Sort sheet**: A spreadsheet menu function that sorts all data by the ranking of a specific sorted column and keeps data together across rows.
> 

> **Sort range**: A spreadsheet menu function that sorts a specified range and preserves the cells outside the range.
> 

Writing the SORT function

```
SORT(DataRange,ColumnNumber,True/False)
*True means sort the data in ascending order. 
**False means to sort the data in descending order.
```

You can add another sorting criterion. 

## Sorting Data in SQL

> **ORDER BY**: A SQL clause that sorts results returned in a query.
> 

```sql
SELECT _____
FROM _____
WHERE _____ AND _____
ORDER BY "Criteria" (DESC)
#If you include DESC in the clause, SQL will sort the data in descending order. 
#If DESC is not included, SQL will sort the data in ascending order. 
```

# Converting and Formatting Data

## Convert and Format Data

### Using the Spreadsheet

### Using SQL

The `CAST` function: 

```sql
CAST (expression AS typename)
#expression is the data to be converted 
#typename is the data type to be returned
```

Converting a number to a string

```sql
SELECT CAST (MyCount AS STRING) FROM MyTable
#SELECT indicates that you will be selecting data from a table
#CAST indicates that you will be converting the data you select to a different data type
#AS comes before and identifies the data type which you are casting to
#STRING indicates that you are converting the data to a string
#FROM indicates which table you are selecting the data from
```

Converting a string to a number

```sql
SELECT CAST (MyVarcharCol AS INT) FROM MyTable
#SELECT indicates that you will be selecting data from a table
#CAST indicates that you will be converting the data you select to a different data type
#AS comes before and identifies the data type which you are casting to
#INT indicates that you are converting the data to an integer
#FROM indicates which table you are selecting the data from
```

Converting a date to a string

```sql
SELECT CAST (MyDate AS STRING) FROM MyTable
#SELECT indicates that you will be selecting data from a table
#CAST indicates that you will be converting the data you select to a different data type
#AS comes before and identifies the data type which you are casting to
#STRING indicates that you are converting the data to a string
#FROM indicates which table you are selecting the data from
```

Converting a date to a datetime

```sql
SELECT CAST (MyDate AS DATETIME) FROM MyTable
#SELECT indicates that you will be selecting data from a table
#CAST indicates that you will be converting the data you select to a different data type
#AS comes before and identifies the data type which you are casting to
#DATETIME indicates that you are converting the data to a datetime value
#FROM indicates which table you are selecting the data from
```

The `SAFE_CAST` function: 

```sql
SELECT SAFE_CAST (MyDate AS STRING) FROM MyTable
```

## Combine Multiple Datasets

> **Dataset**: A collection of data that can be manipulated or analyzed as one unit.
> 

> **Ranking**: A system to position values of a dataset within a scale of achievement or status.
> 

Using the `CONCAT` function

```sql
SELECT CONCAT ('Data','analysis')
```

The result will be `Dataanalysis`.

```sql
SELECT CONCAT ('Data',' ','analysis')
```

The result will be `Data analysis`.

`CONCAT_WS`: A function that adds two or more strings together with a separator.

```sql
CONCAT_WS (‘ . ’, ‘www’, ‘google’, ‘com’)
#The separator (being the period) gets input before and after Google when you run the SQL function
```

`CONCAT with +`: Adds two or more strings together using the + operator

> **LIMIT**: A SQL clause that specifies the maximum number of records returned in a query.
> 

***Example:*** 

```sql
SELECT
	usertype,
	CONCAT(start_station_name, " to ", end_station_name) AS route,
	COUNT(*) as num_trips,
	ROUND(AVG(CAST(tripduration as int64)/60),2) AS duration
FROM
	'bigquery-public-data,new_york,citibike_trips'
GROUP BY
	start_station_name, end_station_name, usertype
ORDER BY
	num_trips DESC
LIMIT 10
```

> **ROUND**: A SQL function that returns a number rounded to a certain number of decimal places.
> 

# Data Aggregation

> **Aggregation**: The process of collecting or gathering many separate pieces into a whole.
> 

> **Data aggregation**: The process of gathering data from multiple sources and combining it into a single, summarized collection.
> 

## Using VLOOKUP in Spreadsheets

> **MATCH**: A spreadsheet function used to locate the position of a specific lookup value.
> 

> **VALUE**: A spreadsheet function that converts a text string that represents a number to a numeric value.
> 

Basic syntax: =VLOOKUP(”value_to_search”, sheet2!$A$1:$D$10, column_number, FALSE)

TRUE searches for approximate results, and FALSE searches for exact matches. 

> **Absolute reference**: A reference within a function that is locked so that rows and columns won’t change if the function is copied.
> 

## Using JOIN in SQL

> **JOIN**: A SQL function that is used to combine rows from two or more tables based on a related column.
> 

***Example:***

```sql
SELECT
	employees.name AS employee_name,
	employees.role AS employy_role,
	departments.name AS department_name
FROM
	employees
INNER JOIN
	deparments ON
	employees.deparment_id = deparments.deparment_id
```

Other JOINs: LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN

> **INNER JOIN**: A SQL function that returns records with matching values in both tables.
> 

> **LEFT JOIN**: A SQL function that will return all the records from the left table and only the matching records from the right table.
> 

> **RIGHT JOIN**: A SQL function that will return all records from the right table and only the matching records from the left.
> 

> **OUTER JOIN**: A SQL function that combines RIGHT and LEFT JOIN to return all matching records in both tables.
> 

## Using COUNT and COUNT DISTINCT in SQL

> **COUNT DISTINCT**: A SQL function that only returns the distinct values in a specified range.
> 

***Example:*** 

```sql
SELECT
	orders.*,
	warehouse.warehouse_alias,
	warehouse.state
FROM 
	warehouse_orders.Orders AS orders
JOIN
	warehouse_orders.Warehouse AS warehouse ON
	orders.warehouse_id = warehouse.warehouse_id
LIMIT 100

SELECT
	COUNT(DISTINCT warehouse.state) AS num_states
FROM 
	warehouse_orders.Orders AS orders
JOIN
	warehouse_orders.Warehouse AS warehouse ON
	orders.warehouse_id = warehouse.warehouse_id
GROUP BY
	warehouse.state
```

> **Aliasing**: Temporarily naming a table or column in a query to make it easier to read and write.
> 

## Work with Subqueries

> **Subquery**: A SQL query that is nested inside a larger query.
> 

> **Inner query**: A SQL subquery that is inside of another SQL statement.
> 

> **Outer query**: A SQL statement containing a subquery.
> 

***Examples:***

```sql
SELECT
	station_id,
	num_bikes_available
	(SELECT
		AVG(num_bikes_available)
	FROM bigquery-public-data.new_york.citibike_stations) AS avg_num_bikes_available
FROM 
	bigquery-public-data.new_york.citibike_stations
```

```sql
SELECT
	station_id,
	name,
	number_of_rides AS number_of_rides_starting_at_station
FROM
	(
		SELECT
			start_station_id
			COUNT(*) number_of_rides
		FROM
			bigquery-public-data.new_york.trips
		GROUP BY
			start_station_id
		)
AS station_num_trips
INNER JOIN
	bigquery-public-data.new_york.citibike_stations ON
	station_id = start_station_id
ORDER BY
	number_of_rides DESC
```

```sql
SELECT
	station_id,
	name
FROM
		bigquery-public-data.new_york.citibike_stations
WHERE
	station_id IN
	(
		SELECT
			start_station_id
		FROM
			bigquery-public-data.new_york.trips
		WHERE
			usertype = 'Subscriber'
	)
```

Use HAVING and CASE in subqueries. 

> **HAVING**: A SQL clause that adds a filter to a query instead of the underlying table that can only be used with aggregate functions.
> 

***Example:***

```sql
SELECT
	Warehouse.warehouse_id,
	CONCAT(Warehouse.state, ': ', Warehouse.warehouse_alias) AS warehouse_name
	COUNT(Orders.order_id) AS number_of_orders,
	(
		SELECT
			COUNT(*)
		FROM warehouse_orders.Orders Orders
	)
	AS total_orders,
	CASE
		WHEN COUNT(Orders.order_id)/(SELECT COUNT(*) FROM warehouse_orders.Orders Orders) <= 0.20
		THEN "Fulfilled 0-20% of Orders"
		WHEN COUNT(Orders.order_id)/(SELECT COUNT(*) FROM warehouse_orders.Orders Orders) > 0.20
		AND COUNT(Orders.order_id)/(SELECT COUNT(*) FROM warehouse_orders.Orders Orders) <= 0.60
		THEN "Fulfilled 21-60% of Orders"
	ELSE "Fulfilled moree than 60% of Orders"
	END AS fulfillment_summary
FROM
	warehouse_orders.Warehouse Warehouse
LEFT JOIN
	warehouse_orders.Orders Orders ON
	Orders.warehouse_id = Warehouse.warehouse_id
GROUP BY
	Warehouse.warehouse_id,
	warehouse_name
HAVING 
	COUNT(Orders.order_id) > 0
```

# Data Calculation

> **Statistics**: The study of how to collect, analyze, summarize, and present data.
> 

> **Calculus**: A branch of mathematics that involves the study of rates of change and the changes between values that are related by a function.
> 

> **Causation**: When an action directly leads to an outcome, such as cause-effect relationship.
> 

> **Correlation**: The measure of the degree to which two variables change in relationship to each other.
> 

## Data Calculation in Spreadsheets

### Formula

> **Array**: A collection of values in spreadsheet cells.
> 

> **Modulo**: An operator (%) that returns the remainder when one number is divided by another.
> 

> **SUMIF**: A spreadsheet function that adds numeric data based on one condition.
> 

> **AVERAGEIF**: A spreadsheet function that returns the average of all cell values from a given range that meet a specified condition.
> 

> **SUMPRODUCT**: A function that multiplies arrays and returns the sum of those products.
> 

> **MAXIFS**: A spreadsheet function that returns the maximum value from a given range that meets a specified condition.
> 

> **MINIFS**: A spreadsheet function that returns the minimum value from a given range that meets a specified condition.
> 

### Pivot Table

> **Summary table**: A table used to summarize statistical information about data.
> 

> **Calculated field**: A new field within a pivot table that carries out certain calculations based on the values of other fields.
> 

> **Profit margin**: A percentage that indicates how many cents of profit has been generated for each dollar of sale.
> 

## Data Calculation in SQL

> **GROUP** **BY**: A SQL clause that groups rows that have the same values from a table into summary rows.
> 

The simplest way to embed calculations in SQL:

```sql
SELECT
	columnA,
	columnB,
	columnA/columnB AS columnX
FROM
	table_name
```

## Data Validation

> **Data validation process**: The process of checking and rechecking the quality of data so that it is complete, accurate, secure, and consistent.
> 

> **Underscores**: Lines used to underline words and connect text characters.
> 

## Temporary Tables in SQL

> **Temporary table**: A database table that is created and exists temporarily on a database server.
> 

> **CONVERT**: A SQL function that changes the unit of measurement of a value in data.
> 

Create a temporary table using the `WITH` clause: 

> **WITH**: A SQL clause that creates a temporary table that can be queried multiple times.
> 

```sql
WITH trips_over_1_hr AS (
	SELECT
		*
	FROM
		bigquery-public-date.new_york.citibike_trips
	WHERE
		tripduration >= 60
	)

## Count how many trips are 60+ munite long: 
SELECT
	COUNT(*) AS cnt
FROM
	trips_over_1_hr
```

Use the `SELECT INTO` statement: 

> **SELECT INTO**: A SQL clause that copies data from one table into a temporary table without adding the new table to the database.
> 

```sql
SELECT
	*
INTO
	Africa_Sales
FROM
	Global_Sales
WHERE
	Region = "Africa"
```

Use the `CREATE TABLE` clause: 

> **CREATE TABLE**: A SQL clause that adds a temporary table to a database that can be used by multiple people.
> 

```sql
CREATE TABLE Africa_Sales AS
(
	SELECT
		*
	FROM
		Global_Sales
	WHERE
		Region = "Africa"
	)
```

> **DROP TABLE**: A SQL clause that removes a temporary table from a database.
> 

[Intermediate Guide to SQL.pdf](Analyze%20Data%20to%20Answer%20Questions%20a2d98075461148e1aec056d3d5d46695/Intermediate_Guide_to_SQL.pdf)