# Foundations: Data, Data, Everywhere

# Foundations

## What is Data? What is Data Analysis?

> **Data**: A collection of facts
> 

> **Data analysis**: The collection, transformation, and organization of data in order to draw conclusion, make predictions, and drive informed decision-making.
> 

> **Data analyst**: Someone who collects, transforms, and organizes data in order to draw conclusions, make predictions, and drive informed decision-making.
> 

> **Data analytics**: The science of data.
> 

> **Data science**: A filed of study that uses raw data to create new ways of modeling and understanding the unknown.
> 

## What Skills Does a Data Analyst Have?

> **Analytical skills**: Qualities and characteristics associated with using facts to solve problems.
> 

> **Analytical thinking**: The process of identifying and feigning a problem, then solving it by using data in an organized, step-by-step manner.
> 

> **Technical mindse**t: The ability to break things down into smaller steps or pieces and work with them in an orderly and logical way.
> 

> **Structured thinking**: The process of recognizing the current problem or situation, organizing available information, revealing gaps and opportunities, and identifying options.
> 

## The Data Ecosystem

> **Database**: A collection of data stored in a computer system.
> 

> **Dataset**: A collection of data that can be manipulated or analyzed as one unit.
> 

> **Data element**: A piece of information in a dataset.
> 

> **Data ecosystem**: The various elements that interact with one another in order to produce, manage, store, organize, analyze, and share data.
> 

# The Six Phases of Data Analysis

## Phase 1: Ask

You need to identify your business task.

> **Business task**: The question or problem data analysis resolves for a business.
> 

You need to understand what should be down and what is expected. 

> **Gap analysis**: A method for examining and evaluating the current state of a process in order to identify opportunities for improvement in the future.
> 

You need to identify your stakeholders. 

> **Stakeholders**: People who invest time and resources into a project and are interested in its outcome.
> 

## Phase 2: Prepare

You need to prepare your data and decide what data to use. 

> **Data design**: How information is organized.
> 

When preparing data, we need to identify our data strategy. 

> **Data strategy**: The management of the people, processes, and tools used in data analysis.
> 

Also, considering the concept of “Fairness” is also essential in this part. 

> Fairness: A quality of data analysis that does not create or reinforce bias.
> 

When we realize that our data has some bias, we need to find a way to prevent the analysis of the data create or reinforce that bias. 

*E.g. We can increase the population of nighttime riders when finding the majority take the train in the daytime.* 

## Phase 3: Process

## Phase 4: Analysis

### Using a Spreadsheet

You should consider to use a spreadsheet when examining a small amount of data. 

> **Attribute**: A characteristic or quality of data used to label a column in a table.
> 

> **Observation**: The attributes that describe a piece of data contained in a row of a table.
> 

> **Formula**: A set of instructions used to perform a calculation using the data in a spreadsheet.
> 

> **Function**: A preset command that automatically performs a process or task using the data in a spreadsheet.
> 

## Using a query language

Sometimes, you need to use a query language to access a database. 

> **Query**: A request for data or information from a database.
> 

> **Query language**: A computer programming language used to communicate with a database.
> 

The most commonly-used query language is the SQL (Structured Query Language).

```sql
SELECT 
#The range of the data
FROM 
#The name of the the database
WHERE
#Additional requirement
```

Some times, we put a `*` after `SELECT`, meaning we select all data from the database that fulfills the additional requirement. 

```sql
SELECT
*
FROM
movie
WHERE
movie_genre = "Action"
```

The code above selects all data from the database *movie* that have *“Action”* as their *movie_genre.*

## Phase 5: Share

The share part focuses on visualizing the data to better present the results from the data analysis. 

> **Data visualization**: The graphical representation of data.
> 

When sharing the data,  we need to consider the context of the data

> **Context**: The condition in which something exists or happens.
> 

> **Root cause**: The reason why a problem occurs.
> 

We also need to select the ways of visualization wisely. Remember, visualizing the data makes the outcomes of the analysis more convincing and easy-to-follow. It also helps to present some interesting findings and trends directly. 

## Phase 6: Act

In this phase, the company should adjust the business strategy according to the conclusion drawn from the data analysis. 

> **Data-driven decision-making**: Using facts to guide business strategy.
>