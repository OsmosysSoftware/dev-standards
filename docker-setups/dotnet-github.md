# Dockerizing .NET projects

## Table of Contents

- [Dockerizing .Net project](#dockerizing-net-project)
  - [Table of Contents](#table-of-contents)
  - [1. Introduction](#1-introduction)
    - [Purpose](#purpose)
    - [Scope](#scope)
  - [2. Prerequisites](#2-prerequisites)
  - [3. Setting Up Docker for a .Net project](#3-setting-up-docker-for-a-net-project)
    - [1. Dockerfile](#1-dockerfile)
    - [2. Dockerignore](#2-dockerignore)
    - [3. Docker Compose (Optional for Development)](#3-docker-compose-optional-for-development)
    - [4. Build Docker Image](#4-build-docker-image)
    - [5. Run Docker Container](#5-run-docker-container)
    - [6. Test the Container](#6-test-the-container)
    - [7. Deployment](#7-deployment)
      - [Push Dockerized application to DockerHub](#push-dockerized-application-to-dockerhub)
      - [Run Dockerized application](#run-dockerized-application)
  - [4. Addressing Common Issues](#4-addressing-common-issues)
  - [5. Best Practices for Enhanced Dockerization](#5-best-practices-for-enhanced-dockerization)
  - [6. Conclusion](#6-conclusion)
## 1. Introduction

### Purpose

The purpose of this document is to provide a step-by-step guide for dockerizing a .NET Core application. Dockerizing ensures consistent dependency versions and effortless cross-environment compatibility, simplifies development and deployment processes significantly.

### Scope

The scope of this document covers the following

1. Docker setup for an .NET Core application
2. How to Deploy a Dockerized application using DockerHub

[Back to top](#table-of-contents)

## 2. Prerequisites

Before setting up the dockerize the application, ensure you have the following prerequisites:

- A GitHub account with access to your target repository.
- A Dotnet application repository hosted on GitHub.
- **Docker Environment:** Ensure your development machine has Docker Desktop or the command-line equivalent installed. Refer to the official Docker documentation for installation instructions: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

[Back to top](#table-of-contents)

## 3. Setting up Docker for a .Net project

Dockerizing an existing .NET application for development and deployment involves a series of steps to containerize the application effectively. Below are guidelines to help you dockerize a .NET application:

### 1. Dockerfile:

Create a Dockerfile in the root directory of your .NET application. This file contains instructions for building a Docker image for your application.

Here's a well-structured Dockerfile template for a .NET application (customize based on your project's requirements):

```Dockerfile
# Use the official .NET SDK image for building
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /app

# Expose port 5000 (adjust if your application uses a different port)
EXPOSE 5000

# Copy the project file and restore dependencies
COPY . ./
RUN dotnet restore

# Copy the remaining source code
COPY . ./

# Build the application
RUN dotnet publish -c Release -o out

# Install EF Core tools extension
RUN dotnet tool install --global dotnet-ef --version 8.0.0
ENV PATH $PATH:/root/.dotnet/tools

# Build runtime image
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS runtime
WORKDIR /app
COPY --from=build /app/out ./
ENTRYPOINT ["dotnet", "YourAppName.dll"]
```

### 2. Dockerignore:

Create a `.dockerignore` file to exclude unnecessary files and directories from being copied into the Docker image. This helps in reducing the image size.

```plaintext
bin/
obj/
```

### 3. Docker Compose (Optional for Development):

Create a `docker-compose.yml` file if you want to define services, networks, and volumes for your development environment.

Sample docker file with database(mariadb) and backend setup 
```yaml
version: "3"
services:
  foundation-mariadb:
    image: mariadb:11.2.2
    container_name: foundation-mariadb
    ports:
      - '127.0.0.1:3307:3306'
    env_file:
      - .env
    environment:
      - MYSQL_ROOT_PASSWORD=${MARIADB_ROOT_PASSWORD}
      - MYSQL_USER=${MARIADB_USER}
      - MYSQL_PASSWORD=${MARIADB_PASSWORD}
      - MYSQL_DATABASE=${MARIADB_DATABASE}
    volumes:
      - foundation-mariadb-db-data:/var/lib/mysql
    restart: always

  foundation-backend:
    build:
      context: .
      dockerfile: Dockerfile
    depends_on:
      - foundation-mariadb
    image: foundation-backend
    container_name: foundation-backend
    ports:
      - '127.0.0.1:5000:5000'
    environment:
      - DOTNET_URLS=http://+:5000

volumes:
  foundation-db-data:
    driver: local
```
### 4. Build Docker images using Docker Compose

Instead of manually building the Docker image, you'll use Docker Compose to build it based on the configuration in docker-compose.yml. Run the following command:

```shell
docker-compose build
```

### 5. Run Docker containers using Docker Compose
Once the image is built, you can use Docker Compose to start the containers:
```shell
docker-compose up -d
```
This command will start the containers defined in the docker-compose.yml file in detached mode.

### 6. Optional: List currently running containers:
You can use Docker Compose to view the list of currently running containers:
```shell
docker container ls
```

### 7. Test the Container:

Access your application in a web browser or using a tool like curl to ensure it's running properly.

```bash
curl http://localhost:5000
```

### 8. Deployment:

For deployment to a production instance, you can push your Docker image to a container registry like Docker Hub or Azure Container Registry. Then, pull the image onto your production server and run it similarly to the development setup.

#### Push Dockerized application to DockerHub

Docker Hub is like GitHub but for your docker images. Using DockerHub you can share your images with others also you can use others images in your projects.

To upload your Docker image to Docker Hub, you need a Docker Hub account.
1. If you don’t have one, follow these steps:
    - Go to [Docker Hub](https://hub.docker.com/) in your web browser.
    - Click the “Sign Up” button and follow the registration process to create your account.
2. Once you have a Docker Hub account, log in to Docker Hub from your terminal using the following command:
    ```bash
    docker login
    ```
- You will be prompted to enter your Docker Hub username and password.

3. To push your Docker image to Docker Hub, use the following command:
    ```bash
    docker tag mydotnetapp <your-docker-hub-username>/mydotnetapp:v1

    docker push <your-docker-hub-username>/mydotnetapp:v1
    ```
- Replace <your-docker-hub-username> with your actual Docker Hub username.

This command will upload your Docker image to Docker Hub. You can change v1 to a different version tag if needed.

#### Run Dockerized application 

To run your Dockerized .NET application on a server or cloud platform, follow these steps:

1. Ensure Docker is installed on the server.
2. Log in to your Docker Hub account on the server using `docker login`.
3. Pull the Docker image you uploaded to Docker Hub:

    ```bash
    docker pull <your-docker-hub-username>/mydotnetapp:v1
    ```
4. Run the Docker container:

    ```bash
    docker run -d -p 8080:80 --name mydotnetapp <your-docker-hub-username>/mydotnetapp:v1
    ```
- This command starts a container named mydotnetapp and maps port 8080 on the host to port 80 inside the container. Adjust the port mapping and container name as needed.

5. Access your .NET application by visiting http://your-server-ip:8080 in a web browser.

## 4. Addressing Common Issues:

- **Missing Dependencies:** Ensure all necessary dependencies (NuGet packages, libraries) are included in your Dockerfile or copied into the container image. Utilize `docker logs` to inspect container logs for dependency-related errors.
- **Port Conflicts:** Verify that the exposed port in your Dockerfile doesn't clash with another container or application running on your host machine. Use `docker ps` to list running containers and their ports.
- **Application Errors:** If your application encounters errors inside the container, use `docker logs` to view container logs and pinpoint the root cause. You might need to adjust your Dockerfile commands or application configuration.
- **Permissions Issues:** Double-check that your application has the required permissions to access files or resources within the container. Use `docker exec` to enter the container and examine file permissions.

## 5. Best Practices for Enhanced Dockerization:

- **Multi-Stage Builds for Efficiency:** Consider adopting multi-stage builds to create smaller and more efficient images for production by separating the build and runtime environments in your Dockerfile.
- **Persistent Data with Volumes:** Mount volumes using the `-v` flag with `docker run` to persist application data outside of the container, ensuring data survives container restarts.
- **Environment Variables:** Manage configuration details within your container by defining environment variables in your Dockerfile or during runtime using -e with docker run.

[Back to top](#table-of-contents)

## 6. Conclusion

### Benefits of Docker

Dockerizing your .NET application offers several benefits:

- **Isolation and Consistency**: Docker ensures consistent environments and isolates dependencies.
- **Portability**: Docker containers are portable across different platforms.
- **Simplified Deployment**: It simplifies the deployment process and reduces compatibility issues.

### Future Enhancements

Consider enhancing your DockerFile by using minimal base images, layer caching, multi-stage builds, minimizing dependencies, and leveraging .dockerignore files and implementing robust monitoring and logging solutions for insights into container performance

[Back to top](#table-of-contents)

### Remember to:

- Add COMPOSE_PROJECT_NAME in .env.example and .env files to avoid conflicts with other projects.

```plaintext

COMPOSE_PROJECT_NAME=project-name

```

[Back to top](#table-of-contents)
