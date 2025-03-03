# Standard PR Review Checklist

## PR Meta Information

1. **PR Title**: Ensure the PR title is clear, concise, and follows the project's naming standards (e.g., '[Feature] Add X', '[Bugfix] Fix Y', '[Refactor] Z').
2. **Description**: The PR must include a detailed description explaining:
   - What the PR does.
   - Why the changes are necessary.
   - Links to related issues, tickets, or tasks (if applicable).
3. **Checklist in Description (Optional)**: Include a checklist of tasks completed (if the project uses task checklists).
4. **Reviewer Assignment**: The PR must be assigned to at least one reviewer.
5. **Labels/Tags (Optional)**: Ensure the PR has appropriate labels/tags (e.g., 'Bugfix', 'Feature', 'Documentation').

## Code Changes

6. **Scope of Changes**:
   - PR should contain changes related to only one feature, bugfix, or task.
   - Avoid mixing multiple unrelated changes in one PR.
7. **Clean Code**:
   - Code should follow the project's coding standards (naming conventions, indentation, spacing).
   - Ensure proper formatting (auto-format code if tools are available).
8. **No Repetition**: Avoid duplicate code; refactor into reusable functions or components where possible.
9. **No Hardcoded Values**: Replace hardcoded values with constants, environment variables, or configurations.

## Quality and Best Practices

10. **Tests**:
    - Ensure unit tests or integration tests are added/updated for the feature or bugfix.
    - Run all tests and confirm they pass locally.
11. **Linting and Static Analysis**:
    - Code should pass all linting checks (e.g., ESLint, Flake8, etc.).
    - Resolve any warnings or errors flagged by static analysis tools.
12. **Error Handling**: Ensure proper error handling is implemented (avoid swallowing errors silently).
13. **Performance Considerations**: Check for code efficiency (e.g., avoid unnecessary loops, database queries, or API calls).

## Compliance

14. **CI/CD Pipelines**:
    - Ensure all CI pipelines (builds, tests, deployments) pass successfully.
    - Attach a CI screenshot if the pipelines aren't integrated into the PR system.
15. **Security**:
    - Verify no sensitive information (API keys, passwords, etc.) is exposed in the code or configuration.
    - Check for usage of secure methods and libraries.
16. **Backward Compatibility**: Ensure the changes don't break existing functionality or introduce regressions.

## Documentation and UI

17. **Documentation (Optional)**: Update relevant documentation (e.g., README, API documentation, comments) for new features or changes.
18. **Screenshots/Videos (Optional)**:
    - Add screenshots or video recordings for UI changes (if applicable).
    - Ensure the UI matches the design and is responsive on different screen sizes.

## Miscellaneous

19. **Dead Code**: Remove any unused code, variables, or imports.
20. **Debugging Artifacts**: Ensure no debugging code (e.g., `console.log`, `print`) is left in the codebase.
21. **Dependencies (Optional)**:
    - Verify no unnecessary or outdated dependencies are introduced.
    - Lock file changes (e.g., `package-lock.json`, `requirements.txt`) should be reviewed.

## Final Checks

22. **Self-Review**: The developer submitting the PR must perform a thorough self-review before assigning it to a reviewer.
23. **Cross-Environment Testing (Optional)**: Confirm the changes work in multiple environments (e.g., dev, staging, production).
24. **Feature Flags (Optional)**: Ensure new features are behind feature flags if they are not fully ready for release.

