
# Pull Request Title Validation CI/CD Setup on GitHub

## Table of Contents

- [1. Introduction](#1-introduction)
- [2. Getting Started](#2-getting-started)
- [3. Workflow Configuration](#3-workflow-configuration)
  - [3.1 Trigger](#31-trigger)
  - [3.2 Job](#32-job)
  - [3.3 Steps](#33-steps)
- [4. Setting up config.json file](#4-setting-up-configjson-file)
- [5. Example YAML Configuration](#5-example-yaml-configuration)
- [6. Example config.json file Configuration](#6-example-configjson-file-configuration)
- [7. Validation Checks](#7-validation-checks)
- [8. Troubleshooting](#8-troubleshooting)
- [9. Sample Repository](#9-sample-repository)
- [10. Conclusion](#10-conclusion)
  - [Benefits of CI Setup](#benefits-of-ci-setup)
  - [Future Enhancements](#future-enhancements)

## 1. Introduction

This document provides guidelines for setting up Continuous Integration and Continuous Deployment (CI/CD) to validate PR Title for projects on GitHub using GitHub Actions. It aims to ensure consistent pull request titles across all projects.

[Back to top](#table-of-contents)

## 2. Getting Started

Before you begin, ensure you have a GitHub account, and a basic understanding of GitHub workflows.

[Back to top](#table-of-contents)

## 3. Workflow Configuration

Create a `.github/workflows` directory in your project. Inside this directory, create a YAML file (e.g., `pr_title_validation.yml`) to define your workflow.

### 3.1 Trigger

Specify when your workflow should run. Trigger to use is `pull_request_target` and its types are `opened`, `edited`, `synchronize`, `labeled`, `unlabeled`, `reopened`.

### 3.2 Job

Define job such as `check`. The job runs in a fresh virtual environment.

### 3.3 Steps

Within the job, define steps such as Get PR Title, Check PR Title.

[Back to top](#table-of-contents)

## 4. Setting up config.json file

Create the config.json file `root/pr-title-checker-config.json`. Write the PR validation checks and messages in this file.

[Back to top](#table-of-contents)

## 5. Example YAML Configuration

Here is an example of a basic GitHub Actions workflow file for PR Title Validation:

```yaml
name: "PR Title Checker"
on:
  pull_request_target:
    types:
      - opened
      - edited
      - synchronize
      - labeled
      - unlabeled
      - reopened

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Get PR Title
        id: get_pr_title
        run: |
          echo "Checking PR_TITLE = ${{ github.event.pull_request.title }}"
      
      - name: Check PR Title
        uses: thehanimo/pr-title-checker@v1.4.1
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          pass_on_octokit_error: false
          configuration_path: .github/pr-title-checker-config.json
```

[Back to top](#table-of-contents)

## 6. Example config.json file Configuration

Here is an example of config.json file for PR Title Validation:

```json
{
    "CHECKS": {
      "regexp": "^(build|chore|ci|docs|feat|fix|perf|refactor|style|test|sample): [a-zA-Z0-9 ]{0,50}$"
    },
    "MESSAGES": {
      "success": "PR title is as per standards",
      "failure": "PR title is not as per standards. PR title must start with one of the following prefixes: build, chore, ci, docs, feat, fix, perf, refactor, style, test, sample. PR title content must not exceed 50 characters.",
      "notice": ""
    }
}
```

[Back to top](#table-of-contents)

## 7. Validation Checks

1. PR title must start with the following prefixes: build, chore, ci, docs, feat, fix, perf, refactor, style, test, sample.
2. PR title content must not exceed 50 characters.

[Back to top](#table-of-contents)

## 8. Troubleshooting

If your CI build fails, check the logs in GitHub Actions. Ensure your PR Title follows the above checks to pass the validation.

[Back to top](#table-of-contents)

## 9. Sample Repository

[Repository Link](https://github.com/sujoy-pal144/DevOps-Test-Repo)

Explore this for practical demonstration of PR Title Validation CI setups.

[Back to top](#table-of-contents)

## 10. Conclusion

### Benefits of CI Setup

Setting up a CI pipeline for PR Title Validation provides several benefits:

- Consistency: Ensures uniform pull request titles for easier understanding and management.
- Communication: Enhances clarity and collaboration among team members.
- Efficiency: Streamlines the review process by providing immediate context to reviewers.
- Compliance: Automatically enforces naming conventions and standards, reducing manual checks.

### Future Enhancements

Additional checks for PR title validation can be incorporated as per project requirements.

[Back to top](#table-of-contents)
