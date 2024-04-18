# Continuous Integration (CI) Setup for Python Projects in GitLab

## Table of Contents

- [Continuous Integration (CI) Setup for Python Projects in GitLab](#continuous-integration-ci-setup-for-python-projects-in-gitlab)
  - [Table of Contents](#table-of-contents)
  - [1. Introduction](#1-introduction)
    - [Purpose](#purpose)
    - [Scope](#scope)
  - [2. Prerequisites](#2-prerequisites)
  - [3. Setting Up Continuous Integration (CI) for Python Project](#3-setting-up-continuous-integration-ci-for-python-project)
    - [Creating a `.gitlab-ci.yml` File](#creating-a-gitlab-ciyml-file)
    - [Defining the Pipeline](#defining-the-pipeline)
      - [Lint](#lint)
      - [Test](#test)
    - [Defining Variables](#defining-variables)
    - [Installing Dependencies Before Running Script](#installing-dependencies-before-running-script)
    - [Writing Jobs for Linting and Testing](#writing-jobs-for-linting-and-testing)
    - [Adding Workflow Rules](#adding-workflow-rules)
    - [Complete `.gitlab-ci.yml` Configuration](#complete-gitlab-ciyml-configuration)
  - [4. Conclusion](#4-conclusion)
    - [Benefits of CI Setup](#benefits-of-ci-setup)
    - [Future Enhancements](#future-enhancements)

## 1. Introduction

### Purpose

The purpose of this document is to provide a step-by-step guide for setting up a Continuous Integration (CI) pipeline for a Python project in GitLab. The CI pipeline will automate linting and testing processes to ensure code quality and reliability.

### Scope

This document covers the basic setup of a CI pipeline for a Python project in GitLab, focusing on linting and testing stages. More advanced topics, such as deployment and additional stages, are outside the scope of this guide.

## 2. Prerequisites

Before setting up the CI pipeline, ensure you have the following prerequisites:

- A GitLab account with access to your target repository.
- A Python project repository hosted on GitLab.
- Basic knowledge of Python development and GitLab CI/CD principles.
- The CI runner needs to be properly configured by your IT administrator to execute CI tasks. In case of GitLab, you need to set up and register GitLab Runners on the machines where your CI/CD jobs will run. These runners should be configured to work with your GitLab project.

## 3. Setting Up Continuous Integration (CI) for Python Project

### Creating a `.gitlab-ci.yml` File

The foundation of the CI pipeline is the `.gitlab-ci.yml` file placed at the project's root. This configuration file outlines the environment settings, stages, and jobs that constitute your CI pipeline.

### Defining the Pipeline

The pipeline comprises stages dedicated to linting code and running automated tests, essential practices for upholding code quality and verifying functionality. In this guide, we will use two stages: `lint` and `test`.

```yaml
stages:
  - lint
  - test
```

#### Lint

This stage employs tools like `flake8` to evaluate code quality.

#### Test

During this stage, the pipeline runs automated tests using `pytest`, setting the `PYTHONPATH` to ensure modules are correctly found.

### Defining Variables

Variables offer a way to dynamically adjust the pipeline's settings. Key variables include:

- `DEFAULT_IMAGE`: Specifies the Docker image for the pipeline.
- `merge_request_branches`: Determines which branches trigger the pipeline upon receiving merge requests.

We will not be defining any variables in this guide, but can be done based on project needs.

### Installing Dependencies Before Running Script

We need to ensure that the different requirements have been installed before running the script.

```yaml
before_script:
  - pip install -r requirements.txt
```

### Writing Jobs for Linting and Testing

Create jobs within each stage to perform linting and testing tasks.

```yaml
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
```

### Adding Workflow Rules

The pipeline's execution is fine-tuned to activate only for merge requests that target certain branches, streamlining the CI process to focus on critical updates.

```yaml
workflow:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ /^main|development$/'
```

### Complete `.gitlab-ci.yml` Configuration

Here is the completed configuration for your `.gitlab-ci.yml` file:

```yaml
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

## 4. Conclusion

### Benefits of CI Setup

Setting up a CI pipeline for your Python project offers several benefits:

- Improved code quality through automated linting.
- Early detection of errors and issues.
- Streamlined collaboration through automated testing of merge requests.

### Future Enhancements

Consider enhancing your CI pipeline by adding additional stages such as unit testing, integration testing, and deployment to further improve the quality and reliability of your Python projects.
