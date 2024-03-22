# Setting Up Docker Environment for NestJS Application with MariaDB

## Table of Contents

1. [Introduction](#1-introduction)
   - [Purpose](#purpose)
   - [Scope](#scope)
2. [Prerequisites](#2-prerequisites)
3. [Setting Up Docker Environment](#3-setting-up-docker-environment)
   - [Creating Dockerfile](#creating-dockerfile)
   - [Setting Up Docker Compose](#setting-up-docker-compose)
4. [Testing the Docker Environment](#4-testing-the-docker-environment)
   - [Building Docker Images](#building-docker-images)
   - [Running Docker Containers](#running-docker-containers)
   - [Accessing NestJS Application](#accessing-nestjs-application)
5. [Sample Repository](#5-sample-repository)
6. [Conclusion](#6-conclusion)
   - [Benefits of Docker Setup](#benefits-of-docker-setup)
   - [Future Enhancements](#future-enhancements)

Each section is linked to its corresponding content in the document for easy navigation.

## 1. Introduction

### Purpose

The purpose of this document is to provide a guide for setting up a Docker environment for a Node.js application built with NestJS framework, along with a MariaDB database.

### Scope

This document covers the basic setup of a Docker environment for a NestJS application, including Dockerfile creation, Docker Compose setup, and database configuration.

[Back to top](#table-of-contents)

## 2. Prerequisites

Before setting up the Docker environment, ensure you have the following prerequisites:

- Docker installed on your local machine.
- A NestJS application set up with necessary dependencies.
- Basic knowledge of Docker and Docker Compose.

[Back to top](#table-of-contents)

## 3. Setting Up Docker Environment

### Creating Dockerfile

Create a Dockerfile in the root directory of your NestJS application.

```Dockerfile
FROM node:20.11.1

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Set NODE_ENV environment variable
ENV NODE_ENV production

# Running `npm ci` removes the existing node_modules directory and passing in --only=production ensures that only the production dependencies are installed. This ensures that the node_modules directory is as optimized as possible
RUN npm ci --only=production && npm cache clean --force

# Install Nest CLI globally
RUN npm install -g @nestjs/cli

# Copy the rest of the application code to the container
COPY . .

# Build the NestJS application
RUN npm run build

# Expose the port your application will run on
EXPOSE 3000

# Command to start your NestJS application
CMD ["node", "dist/main.js"]
```

### Setting Up Docker Compose

Create a docker-compose.yml file in the root directory of your project.

```yaml
version: "3"
services:
  api:
    container_name: api
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "127.0.0.1:${SERVER_PORT}:${SERVER_PORT}"
    depends_on:
      - mariadb
    environment:
      NODE_ENV: production

  mariadb:
    container_name: mariadb
    image: mariadb:10.11
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: ${DB_PASSWORD}
      MYSQL_USER: ${DB_USERNAME}
      MYSQL_PASSWORD: ${DB_PASSWORD}
      MYSQL_DATABASE: ${DB_NAME}
    ports:
      - "127.0.0.1:${MARIADB_DOCKER_PORT}:3306"
    volumes:
      - app-db:/var/lib/mysql

volumes:
  app-db: ~
```

## 4. Testing the Docker Environment

### Building Docker Images

Run the following command in the root directory of your project to build the Docker images:

```
docker-compose build
```

### Running Docker Containers

Start the Docker containers using the following command:

```
docker-compose up
```

### Accessing NestJS Application

You can access your NestJS application at http://localhost:3000.

[Back to top](#table-of-contents)

## 5. Sample Repository

[Repository Link](https://github.com/OsmosysSoftware/node-server-docker-sample)

Explore this for practical demonstration of CI setups.

## 6. Conclusion

### Benefits of Docker Setup

Setting up a Docker environment for your NestJS application with MariaDB database offers several benefits:

- Easy deployment and scalability.
- Consistent development environment across different machines.
- Simplified dependency management.

[Back to top](#table-of-contents)

### Future Enhancements

Consider enhancing your Docker setup by adding features such as environment-specific configurations, health checks, and Docker Swarm/Kubernetes integration for production deployments.

[Back to top](#table-of-contents)
