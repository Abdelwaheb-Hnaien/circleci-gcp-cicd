# Continious deployment to Google Compute Instance with CircleCi

--> https://medium.com/@abdelwaheb.hnaien/ci-cd-with-circleci-and-google-cloud-platform-fb1f2206daa4

In this tutorial we demonstrate how to continiously deploy a simple website developed with python flask to a Google Compute Instance.

Notice, this work doesn’t address DevOps/GitOps best practices, it only shows how to deploy an app through a very basic pipeline using CircleCi.
There are more advanced pipelines which implements various testing techniques, notification, rollback, etc. We encourage you to look for them and use them in production.

## Overview

![image](https://drive.google.com/uc?export=view&id=1UDWWf1InIKMzEOLgwUGvrRDZTnaEep6z)

## prerequisites

in order to reproduce the steps of this demo, you need to have basic knowledge of Google Cloud Platform, Docker and [CircleCI config syntaxe](https://circleci.com/docs/2.0/sample-config/).
You will also need a Google Cloud Project with billing enabled.

## Steps
1. Create a github repository
2. Set up a CircleCi project from the repository created in the previous step
3. Create a compute instance, ssh to that instance and install docker
4. Create a service account with the follwing roles: 
    - Compute Admin (warning: circle-ci needs only to access the server, so this doesn't meet least previlege principal)
    - Service Account User
    - IAP-secured Tunnel User
5. Create a service account key.
6. In your CircleCi project, create the following environment variables:
    - GCLOUD_SERVICE_KEY : the value of the key you created in the previous step.
    - GOOGLE_COMPUTE_ZONE : the location of your compute instance
    - GOOGLE_PROJECT_ID : the id of your google cloud project
    - DOCKERHUB_USERNAME : dockerhub username
    - DOCKERHUB_PASSWORD : dockerhub password
    - IMAGE_NAME : the image name that CircleCi will build, it has to be in the form : <your_docker_repo>/<any_name_you_choose>
    - GCE_INSTANCE_NAME: the name of your google compute instance
7. Clone this repository and push the code to your repository (created in step 1)

The website should be deployed to your compute instance now. If you try to access the website through the instance public IP make sure first that firewall rules are correctely set up (allow ingress traffic to port 80).
