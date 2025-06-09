# Git Standards Document

## Introduction

This document outlines the standards and conventions for using Git within our company. Adhering to these standards ensures consistency, clarity, and efficiency in managing and collaborating on projects.

## Table of Contents

- [Git Standards Document](#git-standards-document)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [1. Git Configuration](#1-git-configuration)
  - [2. Repository Structure](#2-repository-structure)
    - [Main Branch](#main-branch)
    - [Development Branch](#development-branch)
    - [Branch Protection Rules](#branch-protection-rules)
    - [Feature Branches](#feature-branches)
  - [3. Commit Messages](#3-commit-messages)
    - [Commit Message Format](#commit-message-format)
      - [Type](#type)
      - [Subject](#subject)
      - [Body](#body)
      - [Footer](#footer)
    - [Revert](#revert)
    - [Commit Message Examples](#commit-message-examples)
  - [4. Commit Granularity](#4-commit-granularity)
  - [5. Submitting a Pull Request (PR)](#5-submitting-a-pull-request-pr)
  - [6. Pull Requests (PRs)](#6-pull-requests-prs)
    - [Pull Request Template](#pull-request-template)
    - [PR Description](#pr-description)
  - [7. Code Reviews and Merge Process](#7-code-reviews-and-merge-process)
  - [8. After your pull request is merged](#8-after-your-pull-request-is-merged)
  - [9. Conflict Resolution](#9-conflict-resolution)
  - [10. Tagging and Releases](#10-tagging-and-releases)
  - [Conclusion](#conclusion)

## 1. Git Configuration

- Username and Email: Ensure your Git configuration is set with your real name and work email.

```bash
    git config --global user.name "Your Name"
    git config --global user.email "your.email@company.com"
```

## 2. Repository Structure

### Main Branch
  - Try to have `main` branch instead of `master`.
  - The `main` branch should always be deployable.
  - All commits on `main` should be made through pull requests.

### Development Branch
  - Use a `development` or `dev` branch for integration and testing.
  - The `development` branch should always contain the latest implemented changes intended for the next release.

### Branch Protection Rules
  - Set branch protection rules for `main` and `development` branches to restrict developers to push unverified changes and allow only maintainers to push/merge.
  - Here is the quick read on how to set branch protection rules:
    - [github: managing-a-branch-protection-rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule)
    - [gitlab: protected_branches](https://docs.gitlab.com/ee/user/project/protected_branches.html)

### Feature Branches
  - Create separate branches for individual features or bug fixes.
  - Do NOT combine multiple features in a single branch. Always create SEPARATE branches for different changes.
  - Feature branch should have short but descriptive names.
  - Accepted naming format: use the task [type](#type) as a prefix, followed by `/` and a short `kebab-case-description`:
    - `feat/user-authentication`
    - `fix/password-reset`
    - `chore/update-api-version`
  -  Note: Some projects may use `task shortcode` as branch name instead (Example: `REST-123`). Consult the Project Manager for what format to follow.

## 3. Commit Messages

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

Footer should contain a closing reference to an issue if any. Check the following links for more information:

- [github: closing-an-issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/closing-an-issue)
- [gitlab: closing-issues-automatically](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)

#### Type

Must be one of the following:

- **build**: Changes that affect the build system or external dependencies (example scopes: nuget, gulp, broccoli, npm)
- **chore**: Updating tasks etc.; no production code change
- **ci**: Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)
- **docs**: Documentation only changes
- **feat**: A new feature
- **fix**: A bug fix
- **perf**: A code change that improves performance
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc.)
- **test**: Adding missing tests or correcting existing tests
- **sample**: A change to the samples

Depending on the project, you can use Sentence case `Type` or project shortcode as prefix.

#### Subject

The subject contains succinct description of the change:

- use the imperative, present tense: "change" not "changed" nor "changes"
- don't capitalize first letter
- no dot (.) at the end

#### Body

- Just as in the **subject**, use the imperative, present tense: "change" not "changed" nor "changes".
- The body should include the motivation for the change and contrast this with previous behavior.

#### Footer

- The footer should contain any information about **Breaking Changes** and is also the place to
reference GitLab issues that this commit **Closes**.
- **Breaking Changes** should start with the word `BREAKING CHANGE:` with a space or two newlines. The rest of the commit message is then used for this.

### Revert

If the commit reverts a previous commit, it should begin with `revert:`, followed by the header of the reverted commit. In the body it should say: `This reverts commit <hash>.`, where the hash is the SHA of the commit being reverted.

Alternatively, you can use the shell command `git revert <commit-id>` for reverting a specific commit.

### Commit Message Examples

In summary, ensure your commit messages follow the following guidelines:

- Write clear, concise, and descriptive commit messages.
- Add the [type](#type) as prefix for each commit.
- Use the imperative mood ("add" instead of "added").
- Use lowercase for commit message
- Do not end the commit message with a dot(.) symbol.

```
build: install npm package <package-name>
chore: bump version to 1.2.3
ci: add ci for <project-name>
docs: update change log to beta.5
fix: add a check for <process-name> before sending confirmation
perf: increase concurrency number for <process-name>
refactor: separate scheduler and business logic
style: remove unnecessary comment
test: add tests for <module-name>
sample: update samples for <module-name>
```

## 4. Commit Granularity

- Make small, atomic commits that logically separate changes.
- Avoid mixing unrelated changes in a single commit.

## 5. Submitting a Pull Request (PR)

Create PRs for merging changes into the `main` or `development` branches. Ensure that these branches are protected and that PRs are merged only after thorough review and testing.

If a complex code change is proposed:
- Create a separate branch `feat/<my-complex-feature>` and target smaller PRs to this branch first.
- Then, create a new PR to merge the changes from branch `feat/<my-complex-feature>` to your desired protected branch.

**Before you submit** your Pull Request (PR) consider the following guidelines:

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

## 6. Pull Requests (PRs)

We recommend using Pull Request Templates for all active projects

- [Add PR Templates for GitHub](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)
- [Description Templates for GitLab](https://docs.gitlab.com/user/project/description_templates/)

### Pull Request Template

It is always a best practise to maintain checklist in every PR to make sure everything is submitted properly along with your PR. Example checklist can be as follows:

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

Add standard headings to your template. Some example headings are as follows:

- Task Link
- Description
- Related changes
- Query request and response
- Screenshots
- Test suite
- Documentation

Adding task links to PRs improves communication, provides context, and ensures that reviewers understand the purpose and requirements of the changes.

### PR Description

Provide a detailed description in the PR:

- What is the change
- Why is it needed
- How did we achieve this change
- Provide screenshots
- Add testcases where necessary
- Add reference links as required

## 7. Code Reviews and Merge Process

Ensure PRs are reviewed and approved by peers before merging.

- Conduct code reviews for every PR to ensure code quality and consistency.
- Address all feedback and comments before merging the PR.
- If you have CI setup, then ensure that CI passes before merging the PR.
- To maintain a clean and organized commit history, use the **"squash and merge"** option when creating a **Pull Request (PR)** against the development branch.

## 8. After your pull request is merged

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

## 9. Conflict Resolution

- Resolve merge conflicts promptly.
- Ensure conflicts are resolved locally before pushing changes.
- Ensure that you test your changes locally after resolving conflicts.

## 10. Tagging and Releases

- Use semantic versioning for your projects.
- Version number is formatted as `MAJOR.MINOR.PATCH`:
  - Increment the `MAJOR` version when making incompatible API changes.
  - Increment the `MINOR` version when adding new functionality in a backward-compatible manner.
  - Increment the `PATCH` version when making backward-compatible bug fixes.
- Create a tag for each release.
- Always add release description.

    ```bash
    git tag -a v1.0.0 -m "Version 1.0.0"
    git push origin v1.0.0
    ```

- Projects hosted on **GitHub** can take advantage of the [auto-generate release notes](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes) feature.

## Conclusion

Adhering to these Git standards ensures a smooth, efficient, and error-free workflow for managing and collaborating on projects within our company. Ensure all team members review and understand these standards, and enforce adherence in all projects.
