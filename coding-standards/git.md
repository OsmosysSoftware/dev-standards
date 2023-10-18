Git Standards Document
======================

Introduction:
-----------------

This document outlines the standards and conventions for using Git within our company. Adhering to these standards ensures consistency, clarity, and efficiency in managing and collaborating on projects.

Git Configuration:
----------------------

-   Username and Email: Ensure your Git configuration is set with your real name and work email.

```bash
    git config --global user.name "Your Name"    
    git config --global user.email "your.email@company.com"
```

Repository Structure:
-------------------------

-   Master/Main Branch:
    -   Try to have `main` branch instead of `master`.
    -   The `main` branch should always be deployable.
    -   All commits on `main` should be made through pull requests.
-   Development Branch:
    -   Use a `development` or `dev` branch for integration and testing.
-   Feature Branches:
    -   Create separate branches for individual features or bug fixes.
    -   Name them descriptively, e.g., `feature/user-authentication`, `bugfix/password-reset`.

Commit Messages:
--------------------

-   Write clear, concise, and descriptive commit messages.
-   Use the imperative mood ("add" instead of "added").
-   Start with a capital letter.
-   Do not end the commit message with a period.
-   Example: `Add user authentication`

Commit Granularity:
-----------------------

-   Make small, atomic commits that logically separate changes.
-   Avoid mixing unrelated changes in a single commit.

Pull Requests (PRs):
------------------------

-   Create PRs for merging changes into the `main` or `development` branches.
-   Ensure PRs are reviewed and approved by peers before merging.
-   Provide a detailed description in the PR, explaining the changes and their purpose (why?).
-   To maintain a clean and organized commit history, use the "squash and merge" option when creating a Pull Request (PR) against the development branch.

Code Reviews:
-----------------

-   Conduct code reviews for every PR to ensure code quality and consistency.
-   Address all feedback and comments before merging the PR.
-   If you have CI setup, then ensure that CI passes before merging the PR.

Conflict Resolution:
------------------------

-   Resolve merge conflicts promptly.
-   Ensure conflicts are resolved locally before pushing changes.
-   Ensure that you test your changes locally after resolving conflicts.

Tagging and Releases:
--------------------------

-   Use semantic versioning for your projects.
-   Create a tag for each release.
-   Always add release description.

```bash
    git tag -a v1.0.0 -m "Version 1.0.0"
    git push origin v1.0.0
```

Conclusion:
----------------

Adhering to these Git standards ensures a smooth, efficient, and error-free workflow for managing and collaborating on projects within our company. Ensure all team members review and understand these standards, and enforce adherence in all projects.
