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
8. **Updated `.gitlab-ci.yml` Example**
9. **Conclusion**

## Introduction
This guide provides a detailed walkthrough for setting up a Continuous Integration (CI) pipeline for Python projects at Osmosys using GitLab. It emphasizes automating testing and linting to maintain high-quality code standards.

## Prerequisites
- A Python project hosted on GitLab.
- Basic knowledge of Python development and GitLab CI/CD principles.

## CI Configuration Overview
The foundation of the CI pipeline is the `.gitlab-ci.yml` file placed at the project's root. This configuration file outlines the environment settings, stages, and jobs that constitute your CI pipeline.

## Defining the Pipeline
The pipeline comprises stages dedicated to linting code and running automated tests, essential practices for upholding code quality and verifying functionality.

## Configuring Variables
Variables offer a way to dynamically adjust the pipeline's settings. Key variables include:
- `DEFAULT_IMAGE`: Specifies the Docker image for the pipeline.
- `merge_request_branches`: Determines which branches trigger the pipeline upon receiving merge requests.

## Pipeline Stages
### Lint
This stage employs tools like `flake8` to evaluate code quality.
### Test
During this stage, the pipeline runs automated tests using `pytest`, setting the `PYTHONPATH` to ensure modules are correctly found.

## Workflow Rules
The pipeline's execution is fine-tuned to activate only for merge requests that target certain branches, streamlining the CI process to focus on critical updates.

## Updated `.gitlab-ci.yml` Example
```yaml
variables:
  DEFAULT_IMAGE: "python:3.12"

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
  tags:
    - python-3.12 # Ensure you are using correct runner

test:
  stage: test
  script:
    - export PYTHONPATH=$PYTHONPATH:$(pwd) # Ensure Python can locate the project modules
    - pytest tests/
  tags:
    - python-3.12 # Ensure you are using correct runner

workflow:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ /^main|development$/'
```

## Conclusion
By integrating a CI pipeline with your GitLab-hosted Python project, you leverage automated testing and linting capabilities, fostering a culture of quality and efficiency. The guidance provided here equips you to efficiently employ GitLab CI/CD features for Python app development, ensuring your code remains robust and reliable.