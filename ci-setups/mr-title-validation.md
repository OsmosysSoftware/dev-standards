
# Merge Request Title Validation CI/CD Setup on Gitlab

## Table of Contents

- [1. Introduction](#1-introduction)
- [2. Getting Started](#2-getting-started)
- [3. Workflow Configuration](#3-workflow-configuration)
  - [3.1 Stages](#31-stages)
  - [3.2 Tags](#32-tags)
  - [3.3 Script](#33-script)
- [4. Example YAML Configuration](#4-example-yaml-configuration)
- [5. Validation Checks](#5-validation-checks)
- [6. Troubleshooting](#6-troubleshooting)
- [7. Sample Repository](#7-sample-repository)
- [8. Conclusion](#8-conclusion)
  - [Benefits of CI Setup](#benefits-of-ci-setup)
  - [Future Enhancements](#future-enhancements)

## 1. Introduction

This document provides guidelines for setting up Continuous Integration and Continuous Deployment (CI/CD) to validate MR Title for projects on GitLab. It aims to ensure consistent merge request titles across all projects.

[Back to top](#table-of-contents)

## 2. Getting Started

Before you begin, ensure you have a Gitlab account, and a basic understanding of Gitlab workflows.

[Back to top](#table-of-contents)

## 3. Workflow Configuration

Create a `.gitlab-ci.yml` file in your project to define your workflow.

### 3.1 Stages

Specify in which stage your workflow should run. Stage used is `validate`.

### 3.2 Tags

Define gitlab runner tag in which your workflow will run. For example - `python-3.11.9`.

### 3.3 Script

Specify the logic of the checks which needs to be checked for merge request validation.

[Back to top](#table-of-contents)

## 4. Example YAML Configuration

Here is an example of a basic Gitlab Actions workflow file for MR Title Validation:

```yaml
stages:
  - validate

validate_merge_request_title:
  stage: validate
  tags:
    - python-3.11.9
  script:
    - 'echo "Validating merge request title: $CI_MERGE_REQUEST_TITLE"'
    - |
      if echo "$CI_MERGE_REQUEST_TITLE" | grep -Eq "^(build|chore|ci|docs|feat|fix|perf|refactor|style|test|sample): [a-zA-Z0-9 ]{0,50}$"; then
        echo "PR title is as per standards"
      else
        echo "PR title is not as per standards. PR title must start with one of the following prefixes: build, chore, ci, docs, feat, fix, perf, refactor, style, test, sample. PR title content must not exceed 50 characters."
        exit 1
      fi
  only:
    - merge_requests
    - triggers
```

[Back to top](#table-of-contents)

## 5. Validation Checks

1. MR title must start with the following prefixes: build, chore, ci, docs, feat, fix, perf, refactor, style, test, sample.
2. MR title content must not exceed 50 characters.

[Back to top](#table-of-contents)

## 6. Troubleshooting

If your CI build fails, check the logs in Gitlab Actions. Ensure your MR Title follows the above checks to pass the validation.

[Back to top](#table-of-contents)

## 7. Sample Repository

[Repository Link](https://gitlab.osmosys.co/sujoy.p/devops-testing/-/tree/main?ref_type=heads)

Explore this for practical demonstration of MR Title Validation CI setups.

[Back to top](#table-of-contents)

## 8. Conclusion

### Benefits of CI Setup

Setting up a CI pipeline for MR Title Validation provides several benefits:

- Consistency: Ensures uniform pull request titles for easier understanding and management.
- Communication: Enhances clarity and collaboration among team members.
- Efficiency: Streamlines the review process by providing immediate context to reviewers.
- Compliance: Automatically enforces naming conventions and standards, reducing manual checks.

### Future Enhancements

Additional checks for MR title validation can be incorporated as per project requirements.

[Back to top](#table-of-contents) 
