# Data Analysis with R Programming

# Introduction to Programming Languages

## Programming Languages

> **Programming language**: A system of words and symbols used to write instructions that computers follow.
> 

> **Coding**: The process of writing instructions to a computer in the syntax of a specific programming language.
> 

> **Computer programming**: The process of giving instructions to a computer in order to perform an action or set of actions.
> 

Different programming languages: 

> **CSS(Cascading Style Sheets)**: A programming language used for web page design that controls graphic elements and page presentation.
> 

> **HTML5**: A programming language that provides structure for web pages and connects to hosting platforms.
> 

> **Java**: A programming language widely used to create enterprise web applications that can run on multiple clients.
> 

> **PHP(Hypertext Preprocessor)**: A programming language for web application development.
> 

> **Python**: A general-purpose programming language.
> 

> **Ruby**: An object-oriented programming language for web application development.
> 

> **Swift**: A programming language for MacOS, iOS, WatchOS, and TVOS.
> 

> **C#**: An object-oriented programming language used to create games and mobile apps in the .NET open source developer platform.
> 

> **C++**: An extension of the C programming language that is used to create console games, such as those for Xbox.
> 

## R Studio

> **IDE(Integrated Development Environment)**: A software application that brings together all the tools a data analyst may want to use in a single place.
> 

> **Open-source**: Code that is freely available and may be modified and shared by the people who use it.
> 

> **Portfolio**: A collection of materials that can be shared with potential employers.
> 

# Introduction to R

## Programming Basics in R

### Concepts

> **Data frame**: A collection of columns containing data, similar to a spreadsheet or SQL table.
> 

> **Data structure**: A format for organizing and storing data.
> 

> **Argument**: Information needed by a function in R in order to run.
> 

> **Variable**: A representation of a value in R that can be stored for later use.
> 

> **Vector**: A group of data elements of the same type stored in a one-dimensional sequence in R.
> 

> **Factor**: An object that stores categorical data where the data values are limited and usually based on a finite group, such as country or year.
> 

> **Function**: A body of reusable code for performing specific tasks in R.
> 

> **Nested**: Code that performs a particular function and is contained within code that performs a broader function.
> 

> **Nested function**: A function that is completely contained within another function.
> 

> **List**: A vector whose elements can be of any type.
> 

> **Matrix**: A two-dimensional collection of elements with rows and columns.
> 

### Operators

> **Assignment operator**: An operator used to assign values to variables and vectors.
> 

> **Arithmetic operator**: An operator used to perform basic math operations such as addition, subtraction, multiplication, and division.
> 

`+` `-` `*` `/`

> **Relational operator**: An operator used to compare values, also known as a comparator.
> 

> **Logical operator**: An operator that returns a logical data type.
> 

`&` and `|` or `!` not

> **Conditional statement**: A declaration that if a certain condition holds, then a certain event must take place.
> 

If/Else if condition:

```r
if (condition){
	operation_1
} else if (condition) {
	operation_2
} else {
	operation_3
}
```

> **Pipe**: A tool in R for expressing a sequence of multiple operations, represented with `%>%`.
> 

## Packages in R

> **CRAN(Comprehensive R Archive Network)**: An online archive with R packages, source, code, manuals, and documentation.
> 

> **Package**: A unit of reproducible R code.
> 

> **Library**: A directory containing all of a data analyst’s installed packages.
> 

> **Vignette**: Documentation for an R package that describes the problem the package is designed to solve, explains how its function can be used, and lists any dependencies on other packages.
> 

> **Tidyverse**: A system of packages in R with a common design philosophy of data manipulation, exploration, and visualization.
> 

> **readr**: An R package in Tidyverse used for importing data.
> 

> **tidyr**: An R package in Tidyverse used for data cleaning to make tidy data.
> 

> **dplyr**: An R package in Tidyverse that offers a consistent set of functions to complete common data-manipulation tasks.
> 

> **ggplot2**: An R package in Tidyverse that creates a variety of data visualizations by applying different visual properties to the data variables in R.
> 

# Clean Data Using R

> **Anscombe’s quartet**: Four datasets that have nearly identical summary statistics but contain different plotted values.
> 

> **Log file**: A computer-generated file that records events from operating systems and other software programs.
> 

> **FWF(fixed-width file)**: A text file with a specific format, which enables the saving of textual data in an organized fashion.
> 

> **TSV(Tab-separated-values file)**: A text file that stores a data table by separating columns of data with tabs.
> 

> **Tidy data**: A way of standardizing the organization of data within R.
> 

> **Tibble**: A streamlined variation of data frames.
> 

> **head()**: An R function that returns a preview of the column names and the first few rows of a dataset.
> 

> **mutate()**: An R function that makes changes to a data frame, separating and merging columns or creating new variables.
> 

# Data Visualization Using R

[Google Analytics_R for Data Viz.Rmd](Data%20Analysis%20with%20R%20Programming%20f5629d1aeec94a8c9715d13ffe35602c/Google_Analytics_R_for_Data_Viz.rmd)

> **Analysis**: The process used to make sense of the data collected.
> 

> **Dashboard filter**: A tool for showing only the data that meets a specific criteria while hiding the rest.
> 

## Basic Concepts

> **Aesthetic**: A visual property of an object in a plot.
> 

> **Facets**: A series of functions that splits data into subsets in a matrix of panels.
> 

> **Geom**: The geometric object used to represent data.
> 

> **Mapping**: The process of matching up a specific variable in a dataset with a specific aesthetic.
> 

> **Labels and annotations**: A group of R functions used for customizing a plot.
> 

## Smoothing Data in R

> **Smoothing**: A process used to make data visualizations in R clearer and more readable.
> 

> **Smoothing line**: A line on a data visualization that uses smoothing to represent a trend.
> 

> **GAM (generalized additive model) smoothing: A process for smoothing plots with a large number of points.**
> 

> **Loess smoothing**: A process used for smoothing plots with fewer than 1,000 points.
> 

# R Documentation

> **Markdown**: A syntax for formatting plain text files.
> 

> **R Markdown**: A file format for making dynamic documents with R.
> 

> **R Notebook**: A document for running code and displaying the graphs and charts that visualize the code.
> 

> **HTML (Hypertext Markup Language)**: The set of markup symbols or codes used to create a webpage.
> 

> **Jupyter Notebook**: An open-source web application used to create and share documents that contain live code, equations, visualizations, and narrative text.
> 

> **Code chunk**: A piece of code added in an R Markdown file that is used to process, visualize, or analyze data.
> 

> **Inline code**: Code that can be inserted directly into the text of an R Markdown file.
> 

> **Elevator pitch**: A short statement describing an idea or concept.
> 

> **YAML**: A language that translate data to improve readability
> 

> **Shiny**: An R package used to build interactive web apps with R code.
>