[![made with python](https://img.shields.io/badge/made%20in-python-red)](https://img.shields.io/badge/made%20in-python-red)
[![made with Docker](https://img.shields.io/badge/made%20with-docker-blue)](https://img.shields.io/badge/made%20in-python-blue)
[![author](https://img.shields.io/badge/author-saami97-green)](https://img.shields.io/badge/author-saami97-green)

## Kyubi-Dockerized

## Table of Contents

- [Introduction](#introduction)
- [Building the Docker Image](#building-the-docker-image)
- [Running the Docker Image](#running-the-docker-image)

## Introduction

This directory contains the necessary files and instructions to build and run a Docker image for Kyubi. 

## Prerequisites

To build and run the Docker image, you'll need the following:

- Access to a machine with Docker installed: [Docker Installation Guide](https://docs.docker.com/get-docker/)
- Docker Hub account (optional) for pushing and pulling Docker images

## Using Google Cloud Shell for Docker

Experiment with Docker in Google Cloud Shell without needing to install Docker on your local machine. Follow these steps:

1. Navigate to [Google Cloud Shell](https://console.cloud.google.com/cloudshell).

2. Use the provided terminal to run the below given Docker commands and experiment with Docker containers.

## Building the Docker Image

To build the Docker image locally, follow these steps:

1. Clone this repository:

    ```bash
    git clone https://github.com/saami97/Kyubi.git
    ```

2. Build the Docker image using the provided Dockerfile:

    ```bash
    docker build -t <any-name-you-wish> .
    ```
    example: 

    ```bash
    docker build -t kyubi:1.0 .
    ```
    Here the image is named as **kyubi** and is tagged as **1.0**


## Running the Docker Image

To run the Docker image locally, use the following command:

```bash
docker run -it your-image-name:tag
```

Replace `your-image-name` and `tag` with the name of the Docker image and the tag that you specified during the build process respectively.
Adding  `-i` and `-t` options will make it interactive.

example: 

```bash
docker run -it kyubi:1.0
```

 Here the image is named as **kyubi** and is tagged as **1.0**
