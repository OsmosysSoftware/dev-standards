# Git Standards Document

## Introduction

This document outlines the standards and conventions for using Git within our company. Adhering to these standards ensures consistency, clarity, and efficiency in managing and collaborating on projects.

## Table of Contents

- [Git Standards Document](#git-standards-document)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [1. Git Configuration](#1-git-configuration)
  - [2. Repository Structure](#2-repository-structure)
    - [Main/Master Branch](#mainmaster-branch)
    - [Development Branch](#development-branch)
    - [Branch Protection Rules](#branch-protection-rules)
    - [Feature Branches](#feature-branches)
  - [3. Commit Messages](#3-commit-messages)
    - [Commit Message Format](#commit-message-format)
      - [Type](#type)
      - [Subject](#subject)
      - [Body](#body)
      - [Footer](#footer)
    - [Commit Message Samples](#commit-message-samples)
    - [Revert](#revert)
  - [4. Commit Granularity](#4-commit-granularity)
  - [5. Pull Requests (PRs)](#5-pull-requests-prs)
  - [6. Submitting a Pull Request (PR)](#6-submitting-a-pull-request-pr)
    - [After your pull request is merged](#after-your-pull-request-is-merged)
  - [7. Code Reviews](#7-code-reviews)
  - [8. Conflict Resolution](#8-conflict-resolution)
  - [9. Tagging and Releases](#9-tagging-and-releases)
  - [Conclusion](#conclusion)

## 1. Git Configuration

- Username and Email: Ensure your Git configuration is set with your real name and work email.

```bash
    git config --global user.name "Your Name"
    git config --global user.email "your.email@company.com"
```

## 2. Repository Structure

### Main/Master Branch
  - Try to have `main` branch instead of `master`.
  - The `main` branch should always be deployable.
  - All commits on `main` should be made through pull requests.

### Development Branch
  - Use a `development` or `dev` branch for integration and testing.
  - The `development` branch should always contain the latest implemented changes intended for the next release.

### Branch Protection Rules
  - Set branch protection rules for `main` and `development` branches to restrict developers to push unverified changes and allow only maintainers to push/merge.
  - Here is the quick read on how to set branch protection rules:
    - github: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule
    - gitlab: https://docs.gitlab.com/ee/user/project/protected_branches.html

### Feature Branches
  - Create separate branches for individual features or bug fixes.
  - Do NOT combine multiple features in a single branch. Always create SEPARATE branches for different changes.
  - Feature branch should have short but descriptive names.
    - Accepted naming formats are using task [type](#type) as prefix, forward slash `/`, followed by a short `kebab-case-description`.
    - Examples: `feature/user-authentication`, `bugfix/password-reset`, `chore/update-api-version` etc.
  - Note: Some projects may use `task shortcode` as branch name instead. Consult the Project Manager for what format to follow.

## 3. Commit Messages

- Write clear, concise, and descriptive commit messages.
- Use the imperative mood ("add" instead of "added").
- Start with a capital letter.
- Do not end the commit message with a period.
  - Example: `Add user authentication`
- Always put your commit message in the below context & frame a proper message like this,
  - If applied this commit will, \<your commit message\>
  - Example 1: `Add validation to the email field`
  - Example 2: `Update get users API response with lastname`

### Commit Message Format

Each commit message consists of a **header**, a **body** and a **footer**. The header has a special format that includes a **type**, a **scope** and a **subject**:

```shell
    <type>: <subject>
    <BLANK LINE>
    <body>
    <BLANK LINE>
    <footer>
```

The **header** is mandatory.

Any line of the commit message cannot be longer than 100 characters! This allows the message to be easier
to read in various git tools.

Footer should contain a closing reference to an issue if any.

- github: https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/closing-an-issue
- gitlab: https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically

#### Type

Must be one of the following:

- **build**: Changes that affect the build system or external dependencies (example scopes: nuget, gulp, broccoli, npm)
- **chore**: Updating tasks etc; no production code change
- **ci**: Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)
- **docs**: Documentation only changes
- **feat**: A new feature
- **fix**: A bug fix
- **perf**: A code change that improves performance
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- **test**: Adding missing tests or correcting existing tests
- **sample**: A change to the samples

Depending on the project, you can use Sentence case `Type` or project shortcode as prefix.

#### Subject

The subject contains succinct description of the change:

- use the imperative, present tense: "change" not "changed" nor "changes"
- don't capitalize first letter
- no dot (.) at the end

#### Body

Just as in the **subject**, use the imperative, present tense: "change" not "changed" nor "changes".
The body should include the motivation for the change and contrast this with previous behavior.

#### Footer

The footer should contain any information about **Breaking Changes** and is also the place to
reference GitLab issues that this commit **Closes**.

**Breaking Changes** should start with the word `BREAKING CHANGE:` with a space or two newlines. The rest of the commit message is then used for this.

### Commit Message Samples

```shell
# lowercase
docs: update change log to beta.5
fix: need to depend on latest rxjs and zone.js
chore: bump version to 1.2.3

# Sentence case
Feature: Add redis service
Documentation: Create usage guide

# Project shortcode
PINT-345: Add new webpage
PINB-678: Fix textbox positioning
```

### Revert

If the commit reverts a previous commit, it should begin with `revert:`, followed by the header of the reverted commit. In the body it should say: `This reverts commit <hash>.`, where the hash is the SHA of the commit being reverted.

## 4. Commit Granularity

- Make small, atomic commits that logically separate changes.
- Avoid mixing unrelated changes in a single commit.

## 5. Pull Requests (PRs)

- Create PRs for merging changes into the `main` or `development` branches.
- Ensure PRs are reviewed and approved by peers before merging.
- Adding task links to PRs improves communication, provides context, and ensures that reviewers understand the purpose and requirements of the changes.
- Provide a detailed description in the PR. Use the body to explain what is it, why is it needed and how is it done etc.

    ```text
    What is the change
    Why is it needed
    How did we achieve this change
    ```

- It is always a best practise to maintain checklist in every PR to make sure everything is submitted properly along with your PR. Example checklist can be as follows:

    ```text
    [ ] No build errors
    [ ] No linting issues
    [ ] No formatting issues
    [ ] Changes Tested Locally
    [ ] Added PR title as per standards
    [ ] Added PR description as per standards
    [ ] Attached document link
    [ ] Attached test cases file
    [ ] Updated deployment checklist
    ```

- To maintain a clean and organized commit history, use the "squash and merge" option when creating a Pull Request (PR) against the development branch.

## 6. Submitting a Pull Request (PR)

Before you submit your Pull Request (PR) consider the following guidelines:

1. Search the Pull Requests/Merge Requests of the respective project for an open or closed PR that relates to your submission. You don't want to duplicate effort.
2. Fork the repository.
3. Make your changes in a new git branch:

   ```shell
   git checkout -b my-fix-branch main
   ```

4. Create your patch, **including appropriate test cases**.
5. Follow our Coding Standards.
6. Run the test suite of the respective project (if any), and ensure that all tests pass.
7. Commit your changes using a descriptive commit message that follows our [commit message conventions](#commit-message-format). Adherence to these conventions is necessary because release notes are automatically generated from these messages.

   ```shell
   git commit -a
   ```

   Note: the optional commit `-a` command line option will automatically "add" and "rm" edited files.

8. Push your branch to GitHub:

   ```shell
   git push origin my-fix-branch
   ```

9. In GitHub, send a pull request to `main` branch.

10. If the reviewer(s) suggests changes then:

  - Make the required updates.
  - Re-run the project test suites to ensure tests are still passing.
  - Depends on the project: Rebase your branch and force push to your GitHub repository (this will update your Pull Request):

    ```shell
    git rebase main -i
    git push -f
    ```

### After your pull request is merged

After your pull request is merged, you can safely delete your branch and pull the changes
from the main (upstream) repository:

- Delete the remote branch on GitHub either through the GitHub web UI or your local shell as follows:

  ```shell
  git push origin --delete my-fix-branch
  ```

- Check out the main branch:

  ```shell
  git checkout main -f
  ```

- Delete the local branch:

  ```shell
  git branch -D my-fix-branch
  ```

- Update your main with the latest upstream version:

  ```shell
  git pull --ff upstream main
  ```

## 7. Code Reviews

- Conduct code reviews for every PR to ensure code quality and consistency.
- Address all feedback and comments before merging the PR.
- If you have CI setup, then ensure that CI passes before merging the PR.

## 8. Conflict Resolution

- Resolve merge conflicts promptly.
- Ensure conflicts are resolved locally before pushing changes.
- Ensure that you test your changes locally after resolving conflicts.

## 9. Tagging and Releases

- Use semantic versioning for your projects.
- In a version number formatted as `MAJOR.MINOR.PATCH`:
  - Increment the `MAJOR` version when making incompatible API changes.
  - Increment the `MINOR` version when adding new functionality in a backward-compatible manner.
  - Increment the `PATCH` version when making backward-compatible bug fixes.
- Create a tag for each release.
- Always add release description.

    ```bash
    git tag -a v1.0.0 -m "Version 1.0.0"
    git push origin v1.0.0
    ```

- Projects hosted on GitHub can take advantage of the [auto-generate release notes](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes) feature.

## Conclusion

Adhering to these Git standards ensures a smooth, efficient, and error-free workflow for managing and collaborating on projects within our company. Ensure all team members review and understand these standards, and enforce adherence in all projects.
