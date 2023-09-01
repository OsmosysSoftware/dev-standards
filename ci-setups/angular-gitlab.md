# Continuous Integration (CI) Setup for Angular Application in GitLab

## Table of Contents

- [Continuous Integration (CI) Setup for Angular Application in GitLab](#continuous-integration-ci-setup-for-angular-application-in-gitlab)
  - [Table of Contents](#table-of-contents)
  - [1. Introduction](#1-introduction)
    - [Purpose](#purpose)
    - [Scope](#scope)
  - [2. Prerequisites](#2-prerequisites)
  - [3. Setting Up Continuous Integration (CI) for Angular App](#3-setting-up-continuous-integration-ci-for-angular-app)
    - [Creating a `.gitlab-ci.yml` File](#creating-a-gitlab-ciyml-file)
    - [Defining Stages](#defining-stages)
    - [Defining Variables](#defining-variables)
    - [Adding Rule Templates](#adding-rule-templates)
    - [Writing Jobs for Linting and Building](#writing-jobs-for-linting-and-building)
    - [Complete `.gitlab-ci.yml` Configuration](#complete-gitlab-ciyml-configuration)
  - [4. Testing the CI Pipeline](#4-testing-the-ci-pipeline)
    - [Creating Merge Requests](#creating-merge-requests)
    - [Observing Pipeline Execution](#observing-pipeline-execution)
  - [5. Visualizing the CI Process in GitLab](#5-visualizing-the-ci-process-in-gitlab)
    - [1. Developer Creates Merge Request](#1-developer-creates-merge-request)
    - [2. CI Pipeline Initiation](#2-ci-pipeline-initiation)
    - [3. Job Stages](#3-job-stages)
    - [4. Merge Request Integration](#4-merge-request-integration)
  - [6. Pre-Merge Checks and Bypassing CI Checks](#6-pre-merge-checks-and-bypassing-ci-checks)
  - [7. Troubleshooting and Advanced Configuration](#7-troubleshooting-and-advanced-configuration)
    - [Handling Merge Conflicts](#handling-merge-conflicts)
    - [Customizing Scripts](#customizing-scripts)
  - [8. Bonus Section](#8-bonus-section)
    - [1. Job Artifacts](#1-job-artifacts)
      - [Update your `.gitlab-ci.yml` Configuration](#update-your-gitlab-ciyml-configuration)
      - [Usage](#usage)
  - [9. Conclusion](#9-conclusion)
    - [Benefits of CI Setup](#benefits-of-ci-setup)
    - [Future Enhancements](#future-enhancements)


## 1. Introduction

### Purpose
The purpose of this document is to provide a step-by-step guide for setting up a Continuous Integration (CI) pipeline for an Angular application in GitLab. The CI pipeline will automate linting and building processes to ensure code quality and reliability.

### Scope
This document covers the basic setup of a CI pipeline for an Angular application in GitLab, focusing on linting and building stages. More advanced topics, such as deployment and additional stages, are outside the scope of this guide.

[Back to top](#table-of-contents)
## 2. Prerequisites

Before setting up the CI pipeline, ensure you have the following prerequisites:

- A GitLab account with access to your target repository.
- An Angular application repository hosted on GitLab.
- Node.js and npm installed on your local machine.
- All required configurations done as per [Angular coding standards](https://github.com/OsmosysSoftware/dev-standards/blob/main/coding-standards/angular.md)
- The CI runner needs to be properly configured by your IT administrator to execute CI tasks. In case of GitLab, you need to set up and register GitLab Runners on the machines where your CI/CD jobs will run. These runners should be configured to work with your GitLab project.

[Back to top](#table-of-contents)
## 3. Setting Up Continuous Integration (CI) for Angular App

### Creating a `.gitlab-ci.yml` File
1. Navigate to your Angular application repository on GitLab.
2. Create a file named `.gitlab-ci.yml` in the root directory.

### Defining Stages
Define the stages for your CI pipeline. In this guide, we will use two stages: `lint` and `build`.

```yaml
stages:
  - lint
  - build
```

### Defining Variables
Define variables that specify the branches on which you want to execute your CI processes

```yaml
variables:
  merge_request_branches: "/^main|development$"
```

You can modify the variable as per your needs. For example if you want to run the jobs for merge requests targeting any release branch you can modify the condition as following:

```yaml
variables:
  merge_request_branches: "/^main|development|release.*/"
```

### Adding Rule Templates
The rules template specifies when a job should run. In this example, jobs will run for merge requests targeting the specified branches in your variable".

```yaml
.rules_template: &rules_template
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && ($CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $merge_request_branches)'
```

### Writing Jobs for Linting and Building
Create jobs within each stage to perform linting and building tasks.

```yaml
linting:
  stage: lint
  script:
    - npm install
    - npm run lint
  tags:
    - Node-18-LTS
  <<: *rules_template

building:
  stage: build
  script:
    - npm install
    - npm run build
  dependencies:
    - linting
  tags:
    - Node-18-LTS
  <<: *rules_template
```

### Complete `.gitlab-ci.yml` Configuration
Here is the completed configuration for your .gitlab-ci.yml file:

```yaml
stages:
  - lint
  - build

variables:
  merge_request_branches: "/^main|development$"

.rules_template: &rules_template
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && ($CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $merge_request_branches)'

linting:
  stage: lint
  script:
    - npm install
    - npm run lint
  tags:
    - Node-18-LTS
  <<: *rules_template

building:
  stage: build
  script:
    - npm install
    - npm run build
  dependencies:
    - linting
  tags:
    - Node-18-LTS
  <<: *rules_template
```
[Back to top](#table-of-contents)
## 4. Testing the CI Pipeline

### Creating Merge Requests
1. Create a new branch in your Angular application repository.
2. Make changes to your code and push the branch to GitLab.
3. Create a merge request (MR) targeting the main or development branch.

### Observing Pipeline Execution

1. Navigate to your merge request on GitLab.
2. Observe the pipeline execution as it runs the linting and building stages.
3. Check the job logs for any errors or warnings.
4. Ensure that the pipeline status reflects the success or failure of the linting and building stages.

[Back to top](#table-of-contents)
## 5. Visualizing the CI Process in GitLab
In this section, we will visually explain the Continuous Integration (CI) process in GitLab and how it works for your Angular application.

### 1. Developer Creates Merge Request
When a developer completes a feature or bug fix, they create a new branch in the GitLab repository. They then make changes to the code and create a Merge Request (MR) for code review.
![Developer Creates Merge Request](assets/angular-gitlab_developer-creates-mr.png)

### 2. CI Pipeline Initiation
Upon MR creation, GitLab's CI pipeline is automatically triggered. The .gitlab-ci.yml configuration file you've set up defines the stages and jobs to be executed in the pipeline. In our case, the stages are lint and build.
![CI Pipeline Initiation](assets/angular-gitlab_pipeline-initiation.png)

### 3. Job Stages
In the `lint` and `build` stage, the CI pipeline installs the necessary dependencies using Node.js and npm. It then runs the linting process on the codebase to check for any coding standards violations or errors.

![Linting Job Preview](assets/angular-gitlab_linting-job-preview.png)
![Linting Job Preview](assets/angular-gitlab_linting-job-start.png)

- If Linting or Build Fails:
  - The CI pipeline reports issues in the job logs.
  - The Merge Request status is updated to indicate that the pipeline failed.
  - Developers review the errors in the job logs and make necessary code changes.
  ![Linting Fails](assets/angular-gitlab_linting-job-failed.png)
  ![MR when Linting Fails](assets/angular-gitlab_pr-when-pipeline-fails.png)

- If Linting and Build Passes:
  - The Merge Request status is updated to indicate that the linting stage passed.
    ![All job passes](assets/angular-gitlab_job-succeed.png)
    ![MR when all job Passes](assets/angular-gitlab_mr-when-pipeline-succeed.png)

All the pipeline and job actions can be seen and reviewed under the build menu of gitlab
![All pipelines and jobs](assets/angular-gitlab_all-pipelines.png)

### 4. Merge Request Integration

The maintainer can now review the linting and building results in the Merge Request itself. If the pipeline indicates success, it signifies that the code adheres to coding standards and that the build process was successful. This reduces the risk of merging code that may cause errors or disrupt the application.

[Back to top](#table-of-contents)
## 6. Pre-Merge Checks and Bypassing CI Checks
Before merging any changes into the main codebase, it's essential to ensure that the Continuous Integration (CI) checks have been successfully completed. These checks verify that code changes adhere to coding standards, pass tests, and build successfully. To enforce this, follow these steps:

1. **Review Pipeline Status:** When a Merge Request (MR) is created, monitor the pipeline's progress and results. Ensure that all stages, such as linting and building, complete successfully.
2. **Merge Only After Success:** As a maintainer, it's crucial to enforce the policy of merging changes only when the pipeline passes without errors. If the pipeline fails, work with the contributor to address the issues before proceeding with the merge.
3. **Bypass Pipeline Check:** In certain scenarios, there may be valid reasons for bypassing the CI checks temporarily. It's recommended that leads add a comment in the MR describing the reason for bypassing the CI checks. This helps maintain a record of the decision and the context behind it.

Please note that bypassing CI checks should be used sparingly and only in exceptional cases. The goal is to maintain code quality and ensure that the CI process is an integral part of our development workflow.

[Back to top](#table-of-contents)
## 7. Troubleshooting and Advanced Configuration

### Handling Merge Conflicts
If your merge request encounters merge conflicts during the auto-merge stage, manual intervention may be required to resolve the conflicts before the pipeline can proceed.

### Customizing Scripts
Modify the scripts in the .gitlab-ci.yml file to match your specific linting and building commands and any additional requirements of your Angular application.

[Back to top](#table-of-contents)

## 8. Bonus Section
### 1. Job Artifacts

In GitLab CI/CD, artifacts are files or directories generated by a CI/CD job that you want to preserve and make available for other stages or downstream pipelines. Artifacts provide a way to pass data between different jobs or stages in a pipeline, making it easier to manage and share important files or build outputs.

In this example we'll see how to add artifacts for linting job.

#### Update your `.gitlab-ci.yml` Configuration

1. In your job, create a file with the job ID in the name before executing the script:
   ```yml
   before_script: touch lint-results-job-$CI_JOB_ID.txt
   ```
2. During the linting process, redirect the results to the pre-created file:
   ```yml
   - npm run lint | tee -a lint-results-job-$CI_JOB_ID.txt
   ```
3. Define artifact options for your job, which may include:
   - When to create the artifact
   - Custom name for the artifact output
   - Defining a output path
   - Setting an expiry for the File

   ```yml
   artifacts:
     when: always
     name: '$CI_JOB_ID'
     paths:
       - lint-results-job-$CI_JOB_ID.txt
     expire_in: 3 months
   ```
4. The final config with artifact may look like this
    ```yml
    stages:
      - lint
      - build

    variables:
      merge_request_branches: '/^main|development|release.*/'

    .rules_template: &rules_template
      rules:
        - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && ($CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $merge_request_branches)'

    linting:
      stage: lint
      before_script: touch lint-results-job-$CI_JOB_ID.txt
      script:
        - npm install
        - npm run lint | tee -a lint-results-job-$CI_JOB_ID.txt
      tags:
        - Node-18-LTS
      artifacts:
        when: always
        name: '$CI_JOB_ID'
        paths:
          - lint-results-job-$CI_JOB_ID.txt
        expire_in: 3 months
      <<: *rules_template

    building:
      stage: build
      script:
        - npm install
        - npm run build
      dependencies:
        - linting
      tags:
        - Node-18-LTS
      <<: *rules_template
    ```

Refer to the [official documentation](https://docs.gitlab.com/ee/ci/jobs/job_artifacts.html) on artifact to get a extensive idea.

#### Usage
- Navigate to Builds > Pipelines to see a list of pipelines that got triggered. Find the download button at the right which gives a list of available files to download. Download the required artifact by choosing the appropriate option from the download menu.

  ![Artifact download option](assets/angular-gitlab_artifact-download-option.png)
- Download and unzip the file to preview the artifact contents.

  ![Downloaded artifact](assets/angular-gitlab_pr-artifact-preview.png)
## 9. Conclusion

### Benefits of CI Setup
Setting up a CI pipeline for your Angular application offers several benefits:

- Improved code quality through automated linting.
- Consistent and reliable builds.
- Early detection of errors and issues.
- Streamlined collaboration through automated testing of merge requests.

### Future Enhancements
Consider enhancing your CI pipeline by adding additional stages such as unit testing, integration testing, and deployment to further improve the quality and reliability of your Angular application.

[Back to top](#table-of-contents)