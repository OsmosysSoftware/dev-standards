# Standard PR Review Checklist

## PR Meta Information

- **PR Title**: Ensure the PR title is clear, concise, and adheres to the project's naming standards (e.g., `[Feature] Add X`, `[Bugfix] Fix Y`, `[Refactor] Z`).
- **Description**: Include a detailed description explaining:
  - What the PR does.
  - Why the changes are necessary.
  - Links to related issues, tickets, or tasks (if applicable).
- **Checklist in Description (Optional)**: Include a checklist of tasks completed (if the project uses task checklists).
- **Reviewer Assignment**: The PR must be assigned to at least one reviewer.
- **Labels/Tags (Optional)**: Ensure the PR has appropriate labels/tags (e.g., `Bugfix`, `Feature`, `Documentation`).
- **Branch Naming**: Follow the project's branch naming conventions (e.g., `feature/xyz`, `bugfix/abc`).

## Code Changes

- **Scope of Changes**:
  - PR should contain changes related to only one feature, bugfix, or task.
  - Avoid mixing multiple unrelated changes in one PR.
  - PRs should not exceed a maximum of 500 lines of code (excluding tests and documentation).
- **Clean Code**:
  - Code should follow the project's coding standards (naming conventions, indentation, spacing).
  - Ensure proper formatting (auto-format code if tools are available).
- **No Repetition**: Avoid duplicate code; refactor into reusable functions or components where possible.
  - **No Hardcoded Values**: Replace hardcoded values with constants, environment variables, or configurations.
- **Breaking Down Large Changes**:
  - For large features, break down changes into smaller, manageable PRs.

## Commit Messages

- **Format**: Ensure commit messages follow the [company's git standards](https://github.com/OsmosysSoftware/dev-standards/blob/main/coding-standards/git.md).
  - Example: `[Component] Short description of change`
  - Use imperative mood (e.g., "Fix bug" instead of "Fixed bug").
  - Provide detailed explanations if the change is complex.

## Quality and Best Practices

- **Tests**:
  - Ensure unit tests or integration tests are added/updated for the feature or bugfix.
  - Run all tests and confirm they pass locally.
- **Linting and Static Analysis**:
  - Code should pass all linting checks (e.g., ESLint, Flake8, etc.).
  - Resolve any warnings or errors flagged by static analysis tools.
- **Error Handling**: Ensure proper error handling is implemented (avoid swallowing errors silently).
- **Performance Considerations**: Check for code efficiency (e.g., avoid unnecessary loops, database queries, or API calls).

## Compliance

- **CI/CD Pipelines**:
  - Ensure all CI pipelines (builds, tests, deployments) pass successfully.
  - Attach a CI screenshot if the pipelines aren't integrated into the PR system.
- **Security**:
  - Verify no sensitive information (API keys, passwords, etc.) is exposed in the code or configuration.
  - Check for usage of secure methods and libraries.
- **Backward Compatibility**: Ensure the changes don't break existing functionality or introduce regressions.

## Documentation and UI

- **Documentation**: Update relevant documentation (e.g., README, API documentation, comments) for new features or changes.
- **Screenshots/Videos (Optional)**:
  - Add screenshots or video recordings for UI changes (if applicable).
  - Ensure the UI matches the design and is responsive on different screen sizes.

## Miscellaneous

- **Dead Code**: Remove any unused code, variables, or imports.
- **Debugging Artifacts**: Ensure no debugging code (e.g., `console.log`, `print`) is left in the codebase.
- **Dependencies**:
  - Verify no unnecessary or outdated dependencies are introduced.
  - Lock file changes (e.g., `package-lock.json`, `requirements.txt`) should be reviewed.

## Final Checks

- **Self-Review**: The developer submitting the PR must perform a thorough self-review before assigning it to a reviewer.
- **Cross-Environment Testing (Optional)**: Confirm the changes work in multiple environments (e.g., dev, staging, production).
- **Feature Flags (Optional)**: Ensure new features are behind feature flags if they are not fully ready for release.

