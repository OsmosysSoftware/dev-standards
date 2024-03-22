# Setting Up Docker Environment for Angular Application with Nginx

## Table of Contents

1. [Introduction](#1-introduction)
   - [Purpose](#purpose)
   - [Scope](#scope)
2. [Prerequisites](#2-prerequisites)
3. [Set up angular project](#3-set-up-for-angular-project)
4. [Setting Up Docker Environment](#3-setting-up-docker-environment)
   - [Dockerfile](#41-dockerfile)
      - [Dockerfile angular version specific fix](#note)
   - [Docker Compose](#42-docker-compose)
   - [nginx.conf](#43-nginxconf)
   - [.dockerignore](#44-dockerignore)
5. [Testing the Docker Environment](#5-testing-the-docker-environment)
   - [Using docker-compose](#build-and-run-using-docker-compose-file)
   - [Step by step build](#or-alternatively-build-step-by-step)
6. [Access Angular Application](#6-access-angular-application)
7. [Sample Repository](#6-sample-repository)
8. [Conclusion](#7-conclusion)
   - [Benefits of Docker Setup](#benefits-of-docker-setup)
   - [Future Enhancements](#future-enhancements)

Each section is linked to its corresponding content in the document for easy navigation.

## 1. Introduction

### Purpose

The purpose of this document is to provide a guide for setting up a Docker environment for an Angular 17 application and to host it on nginx server.

### Scope

- This document covers the basic setup of a Docker environment for an Angular application, including Dockerfile creation, Docker Compose setup, and database configuration.

- Dockerization for this example is done on app built on Angular version 17.1.0

- This document also covers dockerization for apps built on version 16 and below of Angular.

[Back to top](#table-of-contents)

## 2. Prerequisites

Before setting up the Docker environment, ensure you have the following prerequisites:

- Docker installed on your local machine.
- An Angular application set up with necessary dependencies.
- Basic knowledge of Docker and Docker Compose.

Download links:

- [Docker](https://docs.docker.com/get-docker/)
- [NodeJS](https://nodejs.org/en/download/)
- [Angular CLI](https://angular.io/guide/setup-local)
- [Visual Studio Code (Optional)](https://code.visualstudio.com/)

[Back to top](#table-of-contents)

## 3. Set up for angular project

In `package.json`, set the production environment command

```json
// package.json
{
  // ...
  "scripts": {
    // Other Commands
    // Add the following line under "scripts"
    "build:prod": "ng build --configuration production"
  }
  // ...
}
```

Run following command

```shell
ng build
```

[Back to top](#table-of-contents)

## 4. Setting Up Docker Environment

### 4.1 Dockerfile

Create a Dockerfile in the root directory of your Angular application.

```Dockerfile
### Stage 0: Build ###
#--------------------------------------
# Use an official Node runtime as a parent image
FROM node:20 AS builder

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install Angular CLI Globally
RUN npm install -g @angular/cli

# Install app dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the Angular app for production
RUN npm run build:prod

### Stage 1: Run ###
#--------------------------------------
# Defining nginx image to be used
FROM nginx:latest AS ngi

# Fetch APP_NAME from docker-compose
ARG APP_NAME

# Create App Path for build files for Angular 17 and above projects
# For versions older than 17, replace APP_PATH with /usr/src/app/dist/
ENV APP_PATH=/usr/src/app/dist/${APP_NAME}/browser

# Copy the built Angular app to the default Nginx public folder
COPY --from=builder $APP_PATH /usr/share/nginx/html/

# Need to make nginx config file
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start Nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]
```

### Note
#### 1. For angular version 17
- For `APP_PATH`, you can directly replace `${APP_NAME}` with your application name like so:
> ENV APP_PATH=/usr/src/app/dist/`your_application_name`/browser
- OR you can define `${APP_NAME}` in docker-compose and build using that.

#### 2. For angular versions 16 and below:
- Remove the line `ARG APP_NAME`
- Set `APP_PATH` as `/usr/src/app/dist/`:
> ENV APP_PATH=/usr/src/app/dist/

### 4.2 Docker Compose

Create a docker-compose.yml file in the root directory of your project. Set the arg `APP_NAME` as name of your application.

```yml
version: '1'
services:
  angular-docker:
    build:
      context: .
      dockerfile: Dockerfile
      args:
        APP_NAME: your_app_name
    image: angular-sample-image
    container_name: angular-sample-container
    ports:
      - '127.0.0.1:5000:80'

```

### 4.3 nginx.conf

Create a `nginx.conf` file in your root directory folder (where the `package.json` is located) and copy the below code into it.

```plaintext
server {
    listen 80;

    location / {
        root /usr/share/nginx/html;
        index index.html;
        try_files $uri $uri/ /index.html;
    }
}
```

### 4.4 Dockerignore

Create a `.dockerignore` file to exclude unnecessary files and directories from being copied into the Docker image. This helps in reducing the image size.

```plaintext
.git
.gitignore
.editorconfig
/.vscode/*
/node_modules
/npm-debug.log
/e2e
/docs
*.zip
```

## 5. Testing the Docker Environment

### Build and run using docker-compose file

Run the following command to build and compose your docker image using docker-compose.

```shell
docker-compose -f docker-compose.yml up
```
### OR Alternatively build step by step

#### Build Docker Image

Run the following command in the root directory of your project to build the Docker images. Replace `your_app_name` with suitable value as an argument:

```shell
docker build --build-arg APP_NAME=your_app_name -t ng-docker-app:v1.0.0 -f ./Dockerfile .
```

#### Create Docker Containers

Start the Docker containers using the following command:

```shell
docker run -p 5000:80 -d ng-docker-app:v1.0.0
```

#### Optional: To get the list of currently running containers

```shell
docker container ls
```

[Back to top](#table-of-contents)

## 6. Access Angular Application

You can access your Angular application at http://localhost:5000.

[Back to top](#table-of-contents)

## 7. Sample Repository

Explore the following practical demonstration for dockerizarion of angular app: [Repository Link]()

[Back to top](#table-of-contents)

## 8. Conclusion

### Benefits of Docker Setup

Setting up a Docker environment for your NestJS application with MariaDB database offers several benefits:

- Easy deployment and scalability.
- Consistent development environment across different machines.
- Simplified dependency management.

[Back to top](#table-of-contents)

### Future Enhancements

Consider enhancing your Docker setup by adding features such as environment-specific configurations, health checks, and Docker Swarm/Kubernetes integration for production deployments.

[Back to top](#table-of-contents)