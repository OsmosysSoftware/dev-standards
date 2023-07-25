
# Database Guidelines

## Introduction
In order to boost your database's readability, efficiency, and maintainability, you should adhere to the Guidelines. Using a consistent naming scheme will make your database more accessible to everyone, from co-developers to new users. When you need to make adjustments to your database or do troubleshooting, this can save you time and energy.

## Design
The design process consists of the following steps:
1. Determine the purpose of your database - This helps prepare you for the remaining steps.
2. Find and organize the information required - Gather all of the types of information you might want to record in the database, such as product name and order number.
3. Divide the information into tables - Divide your information items into major entities or subjects, such as Products or Orders. Each subject then becomes a table.
4. Turn information items into columns - Decide what information you want to store in each table. Each item becomes a field and is displayed as a column in the table. For example, an Employees table might include fields such as Last Name and Hire Date.
5. Specify primary keys - Choose each table’s primary key. The primary key is a column that is used to uniquely identify each row. An example might be Product ID or Order ID.
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
    
    Go through some of the Do’s & Don's mentioned [here](https://www.dbvis.com/thetable/best-practices-for-sql-coding-and-development/)

## Microsoft SQL Server Style Guide:
Use the guidelines mentioned in [part-1](https://blog.sqlauthority.com/2007/06/04/sql-server-database-coding-standards-and-guidelines-part-1/) & [part-2](https://blog.sqlauthority.com/2007/06/05/sql-server-database-coding-standards-and-guidelines-part-2/)

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
24. Know where to use Having & Where clause. [Read more](https://blog.sqlauthority.com/2007/07/04/sql-server-definition-comparison-and-difference-between-having-and-where-clause/)
25. Join tables in order that they always perform the most restrictive search first to filter out the maximum number of rows in the early phases of a multiple table join.
26. Remember to SET NOCOUNT ON at the beginning of your SQL bataches, stored procedures, triggers to avoid network traffic. This will also reduct the chances of error on linked server.
27. Do not use temp tables use CTE or Derived tables instead.
28. Always take backup of all the data.
29. Never ever work on production server.

## Security Measures:
Use the security measures mentioned for different databases in [here](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html)