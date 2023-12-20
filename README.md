# B5 - Advanced DevOps
## B-DOP-500
### Whanos - Automatically deploy (nearly) anything with a snap

---

## Usage

You can spin up the application using:

```./handler/build.sh```

---

## Overview
DevOps is a collection of great notions and technologies that allows oneself to have a truly great control over the lifecycle of an application. This project, named Whanos, empowers you to combine your knowledge of various DevOps technologies, including Docker, GitHub Actions, Jenkins, Ansible, and Kubernetes, to set up a powerful infrastructure for automatic deployment.

---

## General Description
Master individual DevOps notions and technologies, and combine them to set up an infrastructure using Docker, GitHub Actions, Jenkins, Ansible, and Kubernetes. The project challenges you to create a Whanos infrastructure that enables developers to automatically deploy applications into a cluster with a simple push to their Git repository.

---

## Whanos-Compatible Repository Specifications
For a repository to be usable within the Whanos infrastructure, it must adhere to specific specifications, including a supported language (C, Java, JavaScript, Python, Befunge), a defined structure, and criteria for detection. Whanos automatically analyzes the repository, containerizes the application, and deploys it based on the provided configuration.

---

## Whanos Images Specifications
Whanos images serve as the foundation for all applications running on the Whanos infrastructure. These images, based on official images, are tailored to each supported language and come in two types: Standalone Images and Base Images. The specifications include using the Bourne-Again shell, managing dependencies, and setting the execution command.

---

## Jenkins Instance
Utilize Jenkins for automatic containerization and deployment. Configure Jenkins jobs for building Whanos base images, linking projects, and creating jobs for automatic containerization and deployment. The Jenkins instance configuration can use the Jenkins Configuration as Code approach, providing a convenient setup within a single file.

---

## Kubernetes Cluster
Automatically deploy applications into a Kubernetes cluster based on the presence of a whanos.yml file in the repository. The whanos.yml file specifies deployment configurations such as replicas, resources, and ports. Ensure accessibility of the application from the outside world, and support private Git repositories with documented credential handling.


## Delivery Repository Structure
Organize your delivery repository with Dockerfiles in the 'images' directory, documentation in 'docs', and any necessary files related to Jenkins, Kubernetes, or other technologies. Include helper scripts and configuration files for easy redeployment of the infrastructure.
