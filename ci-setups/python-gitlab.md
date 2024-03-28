# Python CI Setup Guide for GitLab

## Table of Contents
1. **Introduction**
2. **Prerequisites**
3. **CI Configuration Overview**
4. **Defining the Pipeline**
5. **Configuring Variables**
6. **Pipeline Stages**
    - Lint
    - Test
7. **Workflow Rules**
8. **Example `.gitlab-ci.yml`**
9. **Conclusion**

## Introduction
This guide outlines the setup of a Continuous Integration (CI) pipeline for Python projects at Osmosys on GitLab. It focuses on ensuring automated testing and linting for Python applications.

## Prerequisites
- A Python project hosted on GitLab.
- A basic understanding of Python development and GitLab CI/CD concepts.

## CI Configuration Overview
The CI pipeline is defined in a `.gitlab-ci.yml` file located at the root of your project. This file specifies the environment, stages, and jobs that make up your CI pipeline.

## Defining the Pipeline
Your pipeline should include stages for linting your code and running tests. These stages ensure code quality and functionality before merging changes.

## Configuring Variables
Use variables to configure the pipeline dynamically. Notably:
- `DEFAULT_IMAGE` for the Docker image used throughout the pipeline.
- `merge_request_branches` for specifying which branches should trigger the pipeline when targeted by merge requests.

## Pipeline Stages
### Lint
The lint stage checks the code quality using tools like `flake8`.
### Test
The test stage runs automated tests on your code, typically using `pytest`.

## Workflow Rules
Configure the pipeline to only run on merge requests targeting specified branches, improving efficiency and relevance of the CI process.

## Example `.gitlab-ci.yml`
```yaml
variables:
  DEFAULT_IMAGE: "python:3.12"
  merge_request_branches: "/^main|development$/"

image: $DEFAULT_IMAGE

stages:
  - lint
  - test

before_script:
  - pip install -r requirements.txt

lint:
  stage: lint
  script:
    - flake8 .

test:
  stage: test
  script:
    - pytest tests/

workflow:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $merge_request_branches'
```

## Conclusion
Implementing a CI pipeline in GitLab for your Python projects facilitates automated testing and linting, ensuring high code quality and functionality. This setup guide helps you utilize GitLab CI/CD features effectively for Python application development.