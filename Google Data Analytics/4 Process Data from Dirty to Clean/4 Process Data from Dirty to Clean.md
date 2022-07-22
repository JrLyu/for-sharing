# Process Data from Dirty to Clean

# Data Integrity

> **Data integrity**: The accuracy, completeness, consistency, and trustworthiness of data throughout its life cycle.
> 

> **Accuracy**: The degree to which the data conforms to the actual entity being measured or described.
> 

> **Completeness**: The degree to which the data contains all desired components or measures.
> 

> **Consistency**: The degree to which data is repeatable from different points of entry or collection.
> 

> **Data constrains**: The criteria that determine whether a piece of a data is clean and valid.
> 

> **Validity**: The degree to which the data conforms to constraints when it is input, collected, or created.
> 

> **Cross-field validation**: A process that ensures certain conditions for multiple data fields are satisfied.
> 

## Dealing with Insufficient Data

> **Data range**: Numerical values that fall between predefined maximum and minimum values.
> 

> **Estimated response rate**: The average number of people who typically complete a survey.
> 

> **Data manipulation**: The process of changing data to make it more organized and easier to read.
> 

> **Data replication**: The process of storing data in multiple locations.
> 

> **Data transfer**: The process of copying data from a storage device to computer memory or from one computer to another.
> 

> **Random sampling**: A way of selecting a sample from a population so that every possible type of the sample has an equal chance of being chosen.
> 

# Using Statistics

## Statistical Power

> **Statistical Power**: The probability that a test of significance will recognize an effect that is present.
> 

> **DATEDIF**: A spreadsheet function that calculates the number of days, months, or years between two dates.
> 

> **VLOOKUP**: A spreadsheet function that vertically searches for a certain value in a column to return a corresponding piece of information.
> 

> **Regular expression (RegEx)**: A rule that says the values in a table must match a prescribed pattern.
> 

> **Mandatory**: A data value that cannot be left blank or empty.
> 

## Hypothesis testing

> **Hypothesis testing**: A process to determine if a survey or experiment has meaningful results.
> 

> **Statistical significance**: The probability that sample results are not due to random chance.
> 

> **Confidence interval**: A range of values that conveys how likely a statistical estimate reflects the population.
> 

> **Confidence level**: The probability that a sample size accurately reflects the greater population.
> 

> **Margin of error**: The maximum amount that the sample results are expected to differ from those of the actual population.
> 

> **A/B testing**: The process of testing two variations of the same web page to determine which page is more successful at attracting user traffic and generating revenue.
> 

# Ways to Clean Data

> **Clean data**: Data that is complete, correct, and relevant to the problem being solved.
> 

> **Dirty data**: Data that is incomplete, incorrect, or irrelevant to problem to be solved.
> 

> **Data mapping**: The process of matching fields from one data source to another.
> 

> **Data merging**: The process of combing two or more datasets into a single dataset.
> 

> **Data validation**: A tool for checking the accuracy and quality of data.
> 

## Why Cleaning Data is Important?

> **Compatibility**: How well two or more datasets are able to work together.
> 

> **Duplicate data**: Any record that inadvertently shares data with another record.
> 

> **Incomplete data**: Data that is important fields.
> 

> **Inconsistent data**: Data that uses different formats to represent the same thing.
> 

> **Incorrect/Inaccurate data**: Data that is complete but inaccurate.
> 

> **Outdated data**: Any data that has been superseded by newer and more accurate information.
> 

> **Null**: An indication that a value does not exist in a dataset.
> 

> **Data engineer**: A professional who transforms data into a useful format for analysis and gives it a reliable infrastructure.
> 

> **Data warehousing specialist**: A professional who develops processes and procedures to effectively store and organize data.
> 

> **Merger**: An agreement that unites two organizations into a single new one.
> 

## Cleaning Data Using Spreadsheets

> **Syntax**: The predetermined structure of a language that includes all required words, symbols, and punctuation, as well as their proper placement.
> 

> **Conditional formatting**: A spreadsheet tool that changes how cells appear when values meet specific conditions.
> 

> **Remove duplicates**: A spreadsheet tool that automatically searches for and eliminates duplicate entries from a spreadsheet.
> 

> **Split**: A function that divides text around a specified character and puts each fragment into a new, separate cell.
> 

> **CONCATENATE**: A spreadsheet function that joins together two or more text strings.
> 

> **COUNTIF**: A spreadsheet function that returns the number of cells that match a specified value.
> 

> **Text string**: A group of characters within a cell, most often composed of letters.
> 

> **Substring**: A smaller subset of a text string.
> 

> **LEFT**: A function that returns a set number of characters from the left side of a text string.
> 

> **RIGHT**: A function that returns a set number of characters from the right side of a text string.
> 

> **Length**: The number of characters in a text string.
> 

> **LEN**: A function that returns the length of a text string by counting the number of characters it contains.
> 

> **MID**: A function that returns a segment from the middle of a text string.
> 

> **TRIM**: A function that removes leading, trailing, and repeated spaces in data.
> 

> **Delimiter**: A character that indicates the beginning or end of a data item.
> 

> **Field length**: A tool for determining how many characters can be keyed into a spreadsheet field.
> 

# Using SQL to Clean Data

```sql
SELECT
	name
FROM
	table_name
```

```sql
INSERT INTO xxx ()
VALUES ()
```

```sql
UPDATE table_name
SET variable_nanme1 = 'value1'
WHERE variable_name2 = 'value2'
```

To avoid duplicated data, we can use the `DISTINCT` function.

> **DISTINCT**: A keyword that is added to a SQL SELECT statement to retrieve only non-duplicate entries.
> 

```sql
SELECT
	DISTINCT variable_name
FROM
	table_name
```

Use the `LENGTH` or `LEN` function to check if the text string variable matches. 

```sql
SELECT
	LENGTH(variable_name) AS column_name
FROM
	table_nanme

```

```sql
SELECT
	variable_nanme
FROM
	table_name
WHERE
	LENGTH(coulumn_nanme) > number
```

Use `SUBSTR` function to select data we want. 

> **SUBSTR**: A SQL function that extracts a substring from a string variable.
> 

```sql
SELECT
	DISTINCT variable_name
FROM
	table_name
WHERE
	SUBSTR(column_nanme,start_letter_position,number_of_letter) = 'value'
```

Use the `TRIM` function to remove extra spaces. 

```sql
SELECT
	DISTINCT variable_name
FROM
	table_nanme
WHERE
	TRIM(variable_name) = 'value'
	
```

> **Typecasting**: Converting data from one type to another.
> 

Use `CAST` function to convert data into different data types.

> **CAST**: A SQL function that converts data from one datatype to another.
> 

> **Float**: A number that contains a decimal.
> 

```sql
SELECT
	CAST(variable_name AS FLOAT64)
FROM
	table_name
ORDER BY
	CAST(variable_name AS FLOAT64) DESC
```

```sql
SELECT
	CAST(date AS date) AS date_only, variable_name2
FROM
	table_name
WHERE
	date BETWEEN '2020-12-01' AND '2020-12-31'
```

Use `CONCAT` function to combine two columns.

> **CONCAT**: A SQL function that adds strings together to create new text strings that can be used as unique keys.
> 

```sql
SELECT
	CONCAT(varibale_name1,variable_name2) AS new_name
FROM
	table_name
WHERE
	variable = 'value'
```

When some information is missing, `COALESCE` function gives a secondary reference. 

> **COALESCE**: A SQL function that returns non-null values in a list.
> 

```sql
SELECT
	COALESCE(variable_name1,variable_name2) AS new_name
FROM
	table_name
WHERE
	variable = 'value'
```

# Reporting and Validating Clean Data

## Using Spreadsheet

> **COUNTA**: A spreadsheet function that counts the total number of values within a specified range.
> 

> **Find and replace**: A tool that finds a specified search term and replaces it with something else.
> 

## Using SQL

Use the `CASE` function

> **CASE**: A SQL statement that returns record that meet conditions by including an if/then statement in a query.
> 

```sql
SELECT
	variable_name1
	CASE
		WHEN variable_name2 = 'wrong_value' THEN 'correct_value'
		ELSE variable_name2
		END AS new_variable_name
FROM
	table_name
WHERE
```

## The Change Log

> **Change log:** A file containing a chronologically ordered list of modifications made to a project.
> 

> **Verification**: A process to confirm that a data-cleaning effort was well executed and the resulting data is accurate and reliable.
> 

# Build Your Resume

> **Estimated response rate**: The average number of people who typically complete a survey.
> 

> **Soft skills**: Non-technical traits and behaviors that relate to how people work.
> 

> **Transferable skills**: Skills and qualities that can transfer from one job or industry to another.
>