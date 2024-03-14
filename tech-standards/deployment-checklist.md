## General Deployment Checklist

### Pre deployment
1. Testing:
   - Ensure pre-deployment testing is performed in staging environment to catch any issues before they reach production.
   - Ensure you have the approval from QA or equivalent to go ahead for the deployment. 
2. Backup:
   - Take a backup of the current production database.
   - Create a backup of any important configuration files or data.
   - Ensure that you have a clear strategy for handling data migrations.
3. Maintenance Page
   - Enable maintenance page 
   - Stop API / App which updates the database.  
4. Version Control:
   - Ensure you merge all the code to the branch that tracks the Live/Production environment. 
   - Tag releases with version numbers to easily identify and rollback changes if needed.
5. Rollback Plan:
    - Always ensure to have a rollback plan in case the deployment encounters issues. This includes reverting code changes, restoring backups, etc.
6. Communication:
    - Communicate the deployment schedule and any potential downtime to relevant stakeholders.

### Deployment

1. Pull the changes
   - If your live instance is tracking main branch, (assuming you are already on main) - pull the changes on the server.  
2. Environment Configuration:
   - Assuming you have a specific environment configuration file, please add all the new configuration changes onto it. 
3. Dependency Management:
   - Ensure to update all the dependencies.
   - Use a dependency management tool (e.g., npm, pip) to install/update required packages.
4. Build Process:
   - Run any necessary build processes (e.g., compiling assets, minifying scripts) for the  deployment.
5. Database Migrations:
    - If your application uses a database, plan and execute any necessary database migrations.
6. Documentation:
   - Update any necessary documentation, including release notes, if applicable.
7. Monitoring:
   - If you are deploying for the first time, add the new application to your monitoring system to track its performance and detect potential issues.
   - Make sure to set up alerts for key metrics and error rates.
   - Ensure to monitor the web url and required services.
8. Security:
   - If you are setting up the server for the first time, make sure to check and update security settings, including firewalls, permissions, and access controls.
9. Caching:
    - Clear or warm up caches to ensure that the application starts with fresh data.
10. Post-Deployment Checks:
    - Conduct post-deployment checks to ensure that the application is functioning correctly.
    - Monitor error logs for any issues that may arise after deployment.
11. Scheduling Backups:
    - If you are setting up the project for the first time, ensure to setup scheduled backups for databases and critical files to ensure data integrity.
    - Also have a plan to restore the backups once in a month to make sure it works as expected. 
12. Housekeeping
	- Ensure to have a plan for housekeeping activities like deleting the attachments after a year or so.  


