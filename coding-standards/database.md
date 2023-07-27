
# Database Guidelines

## Introduction
In order to boost your database's readability, efficiency, and maintainability, you should adhere to the Guidelines. Using a consistent naming scheme will make your database more accessible to everyone, from co-developers to new users. When you need to make adjustments to your database or do troubleshooting, this can save you time and energy.

## Design
The design process consists of the following steps:
1. Determine the purpose of your database - This helps prepare you for the remaining steps.
2. Find and organize the information required - Gather all of the types of information you might want to record in the database, such as product name and order number.
3. Divide the information into tables - Divide your information items into major entities or subjects, such as Products or Orders. Each subject then becomes a table.
4. Turn information items into columns - Decide what information you want to store in each table. Each item becomes a field and is displayed as a column in the table. For example, an Employees table might include fields such as Last Name and Hire Date.
5. Specify primary keys - Choose each table�s primary key. The primary key is a column that is used to uniquely identify each row. An example might be Product ID or Order ID.
6. Set up the table relationships - Look at each table and decide how the data in one table is related to the data in other tables. Add fields to tables or create new tables to clarify the relationships, as necessary.
7. Refine your design - Analyze your design for errors. Create the tables and add a few records of sample data. See if you can get the results you want from your tables. Make adjustments to the design, as needed.
8. Apply the normalization rules - Apply the data normalization rules to see if your tables are structured correctly. Make adjustments to the tables, as needed.
[Read more](https://support.microsoft.com/en-gb/office/database-design-basics-eb2159cf-1e30-401a-8084-bd4f9c9ca1f5)

## SQL Style Guide:
Use the guidelines mentioned [here](https://www.sqlstyle.guide/)

### Best Practices:
1. To build a well-structured database, it's essential to have a thorough understanding of schemas, tables, and columns. 
2. Avoid redundant data and designing tables with normalization principles in mind.
3.Proper data modeling and normalization are critical components of any SQL development project
4. When it comes to storing data in a SQL database, choosing the appropriate data types and constraints is crucial for maintaining data accuracy, consistency, and searchability.
5. It is important to select the right data type to minimize storage space and reduce processing time. Constraints, such as NOT NULL and UNIQUE, help to ensure data integrity and prevent errors.
6. Optimizing SQL queries is essential for faster results and improved overall performance of your application. By avoiding subqueries and using simpler expressions, your queries are easier to understand and execute, resulting in better performance. 
7. Indexes are an important aspect of optimizing SQL query performance. It is important to keep in mind that adding too many indexes can also have negative effects on performance as they require additional disk space and can slow down write operations.
8. Testing and measuring the performance of SQL queries is essential in identifying bottlenecks and optimizing query execution.
9. Understand SQL expressions and operators as they form the basis for writing effective queries
10. Writing queries with complex logic can be challenging, but breaking them down into smaller, more manageable chunks can make the process easier
    
    Go through some of the Do�s & Don's mentioned [here](https://www.dbvis.com/thetable/best-practices-for-sql-coding-and-development/)

## Microsoft SQL Server Style Guide:

### Naming

**Tables:** Rules: Pascal notation; end with an ‘s’
- Examples: Products, Customers
- Group related table names

**Stored Procs:** Rules: sp<App Name>_[<Group Name >_]<Action><table/logical instance>
- Examples: spOrders_GetNewOrders, spProducts_UpdateProduct

**Triggers:** Rules: TR_<TableName>_<action>
- Examples: TR_Orders_UpdateProducts
- Notes: The use of triggers is discouraged

**Indexes:** Rules: IX_<TableName>_<columns separated by _>
- Examples: IX_Products_ProductID

**Primary Keys:** Rules: PK_<TableName>
- Examples: PK_Products

**Foreign Keys:** Rules: FK_<TableName1>_<TableName2>
- Example: FK_Products_Orderss

**Defaults:** Rules: DF_<TableName>_<ColumnName>
- Example: DF_Products_Quantity

**Columns:** If a column references another table’s column, name it <table name>ID
- Example: The Customers table has an ID column
- The Orders table should have a CustomerID column

### General Rules:
- Do not use spaces in the name of database objects
    - Do not use SQL keywords as the name of database objects
    - In cases where this is necessary, surround the
- object name with brackets, such as [Year]
- Do not prefix stored procedures with ‘sp_’2
- Prefix table names with the owner name


### Structure
- Each table must have a primary key
    - In most cases it should be an IDENTITY column named ID
- Normalize data to third normal form
    - Do not compromise on performance to reach third normal form. Sometimes, a little de-normalization results in better performance.
- Do not use TEXT as a data type; use the maximum allowed characters of VARCHAR instead
- In VARCHAR data columns, do not default to NULL; use an empty string instead
- Columns with default values should not allow NULLs
- As much as possible, create stored procedures on the same database as the main tables they will be accessing

### Formatting
- Use upper case for all SQL keywords
    - SELECT, INSERT, UPDATE, WHERE, AND, OR, LIKE, etc.
- Indent code to improve readability
- Comment code blocks that are not easily understandable
    - Use single-line comment markers(–)
    - Reserve multi-line comments (/*.. ..*/) for blocking out sections of code
- Use single quote characters to delimit strings.
    - Nest single quotes to express a single quote or apostrophe within a string
        - For example, SET @sExample = ‘SQL”s Authority’
- Use parentheses to increase readability
    - WHERE (color=’red’ AND (size = 1 OR size = 2))
- Use BEGIN..END blocks only when multiple statements are present within a conditional code segment.
- Use one blank line to separate code sections.
- Use spaces so that expressions read like sentences.
    - fillfactor = 25, not fillfactor=25
- Format JOIN operations using indents
    - Also, use ANSI Joins instead of old style joins4
- Place SET statements before any executing code in the procedure.
### Coding Standards:
1. Optimize queries using the tools provided by SQL Server
2. Do not use SELECT *
3. Return multiple result sets from one stored procedure to avoid trips from the application server to SQL server
4. Avoid unnecessary use of temporary tables
    - Use ‘Derived tables’ or CTE (Common Table Expressions) wherever possible, as they perform better
5. Avoid using <> as a comparison operator
    - Use ID IN(1,3,4,5) instead of ID <> 2
6. Use SET NOCOUNT ON at the beginning of stored procedures
7. Do not use cursors or application loops to do inserts
    - Instead, use INSERT INTO
8. Fully qualify tables and column names in JOINs
9. Fully qualify all stored procedure and table references in stored procedures.
10. Do not define default values for parameters.
    - If a default is needed, the front end will supply the value.
11. Do not use the RECOMPILE option for stored procedures.
12. Place all DECLARE statements before any other code in the procedure.
13. Do not use column numbers in the ORDER BY clause.
14. Do not use GOTO.
15. Check the global variable @@ERROR immediately after executing a data manipulation statement (like INSERT/UPDATE/DELETE), so that you can rollback the transaction if an error occurs
    - Or use TRY/CATCH
16. Do basic validations in the front-end itself during data entry
17. Off-load tasks, like string manipulations, concatenations, row numbering, case conversions, type conversions etc., to the front-end applications if these operations are going to consume more CPU cycles on the database server
18. Always use a column list in your INSERT statements.
    - This helps avoid problems when the table structure changes (like adding or dropping a column).
19. Minimize the use of NULLs, as they often confuse front-end applications, unless the applications are coded intelligently to eliminate NULLs or convert the NULLs into some other form.
    - Any expression that deals with NULL results in a NULL output.
    - The ISNULL and COALESCE functions are helpful in dealing with NULL values.
20. Do not use the identitycol or rowguidcol.
21. Avoid the use of cross joins, if possible.
22. When executing an UPDATE or DELETE statement, use the primary key in the WHERE condition, if possible. This reduces error possibilities.
23. Avoid using TEXT or NTEXT datatypes for storing large textual data.
    - Use the maximum allowed characters of VARCHAR instead
24. Avoid dynamic SQL statements as much as possible.
25. Access tables in the same order in your stored procedures and triggers consistently.
26. Do not call functions repeatedly within your stored procedures, triggers, functions and batches.
27. Default constraints must be defined at the column level.
28. Avoid wild-card characters at the beginning of a word while searching using the LIKE keyword, as these results in an index scan, which defeats the purpose of an index.
29. Define all constraints, other than defaults, at the table level.
30. When a result set is not needed, use syntax that does not return a result set.
31. Avoid rules, database level defaults that must be bound or user-defined data types. While these are legitimate database constructs, opt for constraints and column defaults to hold the database consistent for development and conversion coding.
32. Constraints that apply to more than one column must be defined at the table level.
33. Use the CHAR data type for a column only when the column is non-nullable.
34. Do not use white space in identifiers.
35. The RETURN statement is meant for returning the execution status only, but not data.

#### Reference:
1.  Group related table names:
    ```
    Products_USA
    Products_India
    Products_Mexico
    ```

2. The prefix sp_ is reserved for system stored procedures that ship with SQL Server. Whenever SQL Server encounters a procedure name starting with sp_, it first tries to locate the procedure in the master database, then it looks for any qualifiers (database, owner) provided, then it tries dbo as the owner. Time spent locating the stored procedure can be saved by avoiding the “sp_” prefix.

3. This improves readability and avoids unnecessary confusion. Microsoft SQL Server Books Online states that qualifying table names with owner names helps in execution plan reuse, further boosting performance.

4. 
    False code:
    ```sql
        SELECT *
        FROM Table1, Table2
        WHERE Table1.d = Table2.c
    ```
        
    true code:
    ```sql
        SELECT *
        FROM Table1
        INNER JOIN Table2 ON Table1.d = Table2.c
    ```

5. Use the graphical execution plan in Query Analyzer or SHOWPLAN_TEXT or SHOWPLAN_ALL commands to analyze your queries. Make sure your queries do an “Index seek” instead of an “Index scan” or a “Table scan.” A table scan or an index scan is a highly undesirable and should be avoided where possible.

6. Consider the following query to find the second highest offer price from the Items table:
    ```sql 
        SELECT MAX(Price)
        FROM Products
        WHERE ID IN
        (
        SELECT TOP 2 ID
        FROM Products
        ORDER BY Price DESC
        )
    ```
    The same query can be re-written using a derived table, as shown below, and it performs generally twice as fast as the above query:
    ```sql
        SELECT MAX(Price)
        FROM
        (
        SELECT TOP 2 Price
        FROM Products
        ORDER BY Price DESC
        )
    ```

7. This suppresses messages like ‘(1 row(s) affected)’ after executing INSERT, UPDATE, DELETE and SELECT statements. Performance is improved due to the reduction of network traffic.

8. Try to avoid server side cursors as much as possible. Always stick to a ‘set-based approach’ instead of a ‘procedural approach’ for accessing and manipulating data. Cursors can often be avoided by using SELECT statements instead. If a cursor is unavoidable, use a WHILE loop instead. For a WHILE loop to replace a cursor, however, you need a column (primary key or unique key) to identify each row uniquely.

9. You cannot directly write or update text data using the INSERT or UPDATE statements. Instead, you have to use special statements like READTEXT, WRITETEXT and UPDATETEXT. So, if you don’t have to store more than 8KB of text, use the CHAR(8000) or VARCHAR(8000) datatype instead.

10. Dynamic SQL tends to be slower than static SQL, as SQL Server must generate an execution plan at runtime. IF and CASE statements come in handy to avoid dynamic SQL.

11. This helps to avoid deadlocks. Other things to keep in mind to avoid deadlocks are:

Keep transactions as short as possible.
Touch the minimum amount of data possible during a transaction.
Never wait for user input in the middle of a transaction.
Do not use higher level locking hints or restrictive isolation levels unless they are absolutely needed.

12. You might need the length of a string variable in many places of your procedure, but don’t call the LEN function whenever it’s needed. Instead, call the LEN function once and store the result in a variable for later use.

13. 
  ```sql
    IF EXISTS (
    SELECT 1
    FROM Products
    WHERE ID = 50)
  ```
   
Instead Of:
  ```sql
    IF EXISTS (
    SELECT COUNT(ID)
    FROM Products
    WHERE ID = 50)
  ```
14. CHAR(100), when NULL, will consume 100 bytes, resulting in space wastage. Preferably, use VARCHAR(100) in this situation. Variable-length columns have very little processing overhead compared with fixed-length columns.

### Best Practices
1. Do not prefix stored procedure with SP_ prefix. As they are first searched in master database, before it is searched in any other database.
2. Always install latest server packs and security packs.
3. Make sure your SQL Server runs on optimal hardware. If your operating system supports 64 bit SQL Server, install 64 bit SQL Server on it. Raid 10 Array.
4. Reduce Network Traffic by using Stored Procedure. Return only required result set from database. If application needs paging it should have done in SQL Server instead of at application level.
5. After running query check Actual Execution Plan for cost of the query. Query can be analyzed in Database Engine Tuning Advisor.
6. Use User Defined Functions sparsely, use Stored Procedures instead.
7. Stored Procedure can achieve all the tasks UDF can do. SP provides much more features than UDFs.
8. Test system with realistic data rather than sample data. Realistic data provides better scenario for testing and reveals problems with real system before it goes to production.
9. Do not use SELECT *, use proper column names to decrease network traffic and fewer locks on table.
10. Avoid Cursors as it results in performance degradation. Sub Query, derived tables, CTE can perform same operation.
11. Reduces the use of nullable columns.
12. NULL columns consumes an extra byte on each column used as well as adds overhead in queries. Also NULL is not good for logic development for programmers.
13. Reduce deadlocks using query hints and proper logic of order in columns.
14. Normalized database always increases scalability and stability of the system. Do not go over 3rd normal form as it will adversely affect performance.
15. Use WHERE clauses to compare assertive logic. Use IN rather than NOT IN even though IN will require more value to specify in clause.
16. BLOBS must be stored filesystem and database should have path to them only. If path is common stored them in application variable and append with filename from the BLOBColumnName.
17. Always perform referential integrity checks and data validations using constraints such as the foreign key and check constraints.
18. SQL Server optimizer will use an index scan if the ORDER BY clause is on an indexed column.
19. Stored Procedure should return same numbers of result set and same columns in any input parameters. Result Set of Stored Procedure should be deterministic.
20. Index should be created on highly selective columns, which are used in JOINS, WHERE and ORDER BY clause.
21. Format SQL Code. Make it readable. Wrap it.
22. Use Column name in ORDER BY clause instead of numbers.
23. Do not use TEXT or NTEXT if possible. In SQL Server 2005 use VARCHAR(MAX) or NVARCHAR(MAX).
24. Know where to use Having & Where clause
    - HAVING specifies a search condition for a group or an aggregate function used in SELECT statement.
    - HAVING can be used only with the SELECT statement. HAVING is typically used in a GROUP BY clause. When GROUP BY is not used, HAVING behaves like a WHERE clause.
    - A HAVING clause is like a WHERE clause, but applies only to groups as a whole, whereas the WHERE clause applies to individual rows. A query can contain both a WHERE clause and a HAVING clause. The WHERE clause is applied first to the individual rows in the tables . Only the rows that meet the conditions in the WHERE clause are grouped. The HAVING clause is then applied to the rows in the result set. Only the groups that meet the HAVING conditions appear in the query output. You can apply a HAVING clause only to columns that also appear in the GROUP BY clause or in an aggregate function. (Reference :BOL)
    - Example of HAVING and WHERE in one query:
        ```sql
        SELECT titles.pub_id, AVG(titles.price)
        FROM titles INNER JOIN publishers
        ON titles.pub_id = publishers.pub_id
        WHERE publishers.state = 'CA'
        GROUP BY titles.pub_id
        HAVING AVG(titles.price) > 10
        ```
    - Sometimes you can specify the same set of rows using either a WHERE clause or a HAVING clause. In such cases, one method is not more or less efficient than the other. The optimizer always automatically analyzes each statement you enter and selects an efficient means of executing it. It is best to use the syntax that most clearly describes the desired result. In general, that means eliminating undesired rows in earlier clauses.
25. Join tables in order that they always perform the most restrictive search first to filter out the maximum number of rows in the early phases of a multiple table join.
26. Remember to SET NOCOUNT ON at the beginning of your SQL bataches, stored procedures, triggers to avoid network traffic. This will also reduct the chances of error on linked server.
27. Do not use temp tables use CTE or Derived tables instead.
28. Always take backup of all the data.
29. Never ever work on production server.

## Security Measures:
Use the security measures mentioned for different databases in [here](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html)