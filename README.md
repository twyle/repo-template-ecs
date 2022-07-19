# A Template For Deploying a Flask app to AWS ECS.

> This flask application enables an admin to register then authorizes them to create new users.

<p align="center">
  <img title="Bandit badge" alt="Bandit badge" src="https://github.com/twyle/repo-template-ecs/actions/workflows/feature-development-workflow.yml/badge.svg" />
  <img title="Bandit badge" alt="Bandit badge" src="https://github.com/twyle/repo-template-ecs/actions/workflows/development-workflow.yml/badge.svg" />
  <img title="Bandit badge" alt="Bandit badge" src="https://github.com/twyle/repo-template-ecs/actions/workflows/staging-workflow.yml/badge.svg" />
  <img title="Bandit badge" alt="Bandit badge" src="https://github.com/twyle/repo-template-ecs/actions/workflows/release-workflow.yml/badge.svg" />
  <img title="Bandit badge" alt="Bandit badge" src="https://github.com/twyle/repo-template-ecs/actions/workflows/production-workflow.yml/badge.svg" />
  <img title="Bandit badge" alt="Bandit badge" src="https://img.shields.io/badge/security-bandit-yellow.svg" />
  <img title="Bandit badge" alt="Bandit badge" src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336" />
  <img title="Bandit badge" alt="Bandit badge" src="https://img.shields.io/badge/Made%20with- Python-1f425f.svg" />
  <img title="Bandit badge" alt="Bandit badge" src="https://img.shields.io/github/license/Naereen/StrapDown.js.svg" />
  <img title="Bandit badge" alt="Bandit badge" src="https://img.shields.io/badge/Medium-12100E?style=flat&logo=medium&logoColor=white" />
  <img title="Bandit badge" alt="Bandit badge" src="https://img.shields.io/badge/github%20actions-%232671E5.svg?style=flat&logo=githubactions&logoColor=white" />
  <img title="Bandit badge" alt="Bandit badge" src="https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white" />
  <img title="Bandit badge" alt="Bandit badge" src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=flat&logo=visual-studio-code&logoColor=white" />
  <img title="Bandit badge" alt="Bandit badge" src="https://img.shields.io/badge/Ubuntu-E95420?style=flat&logo=ubuntu&logoColor=white" />
  <img title="Bandit badge" alt="Bandit badge" src="https://img.shields.io/badge/gunicorn-%298729.svg?style=flat&logo=gunicorn&logoColor=white" />
</p>

![](resources/images/header.jpg)

## Project Overview

This is a User managementsystem that enables an admin user to register and then authorizes them to create other non-admin users. The admin registers using a unique email address and user then has to confirm their account via a link sent to their email. Once their account is confirmed,they can then log into the application, upon which they receive an authorization token. Using this token, the admin can then create other non-admin users.

## Working

It's pretty easy to use the application. On the home page (http://localhost:5000/apidocs):

 1. Register as an admin, using a unique email address, unique name and a password.
 2. Head over to the email address that you provided and click on the confirmation link.
 3. At the application home page, log in with the email address and password, to get back a token.
 4. Use the token, to authorize the user.
 5. Make requests to the user routes to create, update, view or delete a user.

Here's a video showing how to use the application:

<p align=center>
  <img width=400 src="resources/videos/register-admin.gif" />
  <img width=400 src="resources/videos/login-admin.gif" />
</p>

<p align=center>
  <img width=400 src="resources/videos/authorize-admin.gif" />
  <img width=400 src="resources/videos/create-user.gif" />
</p>

## Features

This application has several features including:
 1. Deployed to an AWS ECS using Fargate with a custom domain name.
 2. Versioned using Git and Hosted on GitHub and AWS CodeCommit.
 3. Auto-deployed to AWS using AWS CodePipeline.
 4. Uses gunicorn as the application server.
 5. Uses AWS ECR to host the container image.
 6. Uses an Application Load Balancer with an SSL certifivcate from AWS certificate manager.
 7. Uses AWS SES to send emails.
 8. Uses AWS Opensearch and Firehose for logging as well as filebeats.
 9. Uses AWS Secrets manager to manage the application secrets and AWS KMS for key management.
 10. Uses a containerized PostgreSQL instnace for data storage.
 11. Uses JSON Web Tokens to authorize users.
 12. Uses AWS Route53 to route traffic to the application.
 13. Built using flask, flask-mail, flask-jwt
 14. Documented using swagger

## Application Structure

```sh
repo-template-containerized/
│
└───.github/
│     │
│     └───workflows/
|             |
|             └───feature-development-workflow.yml
|             |
|             └───development-workflow.yml
|             |
|             └───staging-workflow.yml
|             |
|             └───release-workflow.yml
|             |
|             └───production-workflow.yml
│
└───resources/
│     |
│     └───images/
│     |     |
|     |     └───header.jpg
|     └───videos/
|           |
|           └───header.gif
|
└───services/
│     |
│     └───database/
│     |     |
|     |     └───.env
|     |     |
|     |     └───database-compose.yml
|     |
│     └───traefik/
│     |     |
|     |     └───Dockerfile.traefik.dev
|     |     |
|     |     └───Dockerfile.traefik.prod
|     |     |
|     |     └───traefik.dev.toml
|     |     |
|     |     └───traefik.prod.toml
|     |
|     └───web/
|           |
|           └───api/
|           |    |
|           |    └───blueprints/
|           |    |
|           |    └───config
|           |
|           └───tests/
|           |
|           └───.env
|           |
|           └───Dockerfile.dev
|           |
|           └───Dockerfile.prod
|           |
|           └───manage.py
|           |
|           └───requirements.txt
|
└───.gitignore
|
└───.pre-commit-config.yaml
|
└───.pylintrc
|
└───docker-compose-dev.yml
|
└───docker-compose-prod.yml
|
└───LICENSE
|
└───Makefile
|
└───pytest.ini
|
└───README.md
|
└───requirements-dev.txt
|
└───setup.cfg
```

* **repo-template/.github/workflows** </br>
  *Holds the GitHub Action workflow files.*

* **repo-template/resources** </br>
  *Holds the resources used to describe this project.*

* **repo-template/services/database** </br>
  *Holds the database compose file and the database environment variables.*

* **repo-template/services/web** </br>
  *Holds the web application.*

* **repo-template/services/web/api** </br>
  *Holds the api code*

* **repo-template/services/web/api/config** </br>
  *Holds the application configuration.*

* **repo-template/services/web/api/blueprints** </br>
  *Holds the flask blueprints.*

* **repo-template/services/web/api/blueprints/default** </br>
  *Holds the default blueprint.*

* **repo-template/services/web/tests** </br>
  *Holds the api tests.*

## Local Setup

Here is how to set up the application locally:

  1. Clone the application repo:</br>

      ```sh
      git clone https://github.com/twyle/repo-template-ecs.git
      ```

  2. Navigate into the cloned repo:

      ```sh
      cd repo-template-ecs
      ```

  3. Create a Virtual environment:

      ```sh
      python3 -m venv venv
      ```

  4. Activate the virtual environmnet:

      ```sh
      source venv/bin/activate
      ```

  5. Install the project dependancies:

      ```sh
      make update # update the package manager
      make install-dev  # install the development requirements
      make install  # install the runtime requirements
      make pre-commit # initialize pre-commit
      make initial-tag # create the initial tag
      # Delete the pyproject.toml file
      make init-cz # initialize commitizen
      ```

  6. Create the environment variables:

      ```sh
      cd services/web
      touch .env
      ```

      Then paste the following into the file:

      ```sh
        SECRET_KEY=supersecretkey

        POSTGRES_HOST=<YOUR-IP-ADDRESS>
        POSTGRES_DB=lyle
        POSTGRES_PORT=5432
        POSTGRES_USER=postgres
        POSTGRES_PASSWORD=lyle

        MAIL_HOST=<YOUR-MAIL-HOST>
        MAIL_PORT=<YOUR-MAIL-PORT>
        MAIL_USERNAME=<YOUR-USER-NAME>
        MAIL_PASSWORD=<YOUR-PASSWORD>

        FIREHOSE_DELIVERY_STREAM=flask-logging-firehose-stream

        AWS_KEY=<YOUR-AWS-KEY>
        AWS_SECRET=<YOUR-AWS-SECRET>
        AWS_REGION=<YOUR-AWS-REGION>
      ```

      Then create the database secrets:

      ```sh
      cd services/database
      touch .env
      ```

      Then paste the following into the file:

      ```sh
        POSTGRES_DB=lyle
        POSTGRES_PORT=5432
        POSTGRES_USER=postgres
        POSTGRES_PASSWORD=lyle
      ```

  7. Start the database containers:

      ```sh
      make start-db-containers
      make create-db
      make seed-db
      ```

  8. Start the application:

      ```sh
      make build
      make run-dev
      ```

  9. View the running application

      Head over to http://0.0.0.0:5000/apidocs

## Development

 #### 1. Application Design

  1. **Database**

      The database was designed to store the Admin details as well as the users details. These are stored in the tables admin and users.

  2. **Routes**

      Here are the application routes:

      | Route       | Method      | Description      |
      | ----------- | ----------- |----------------- |
      | '/'         | GET         | Get the home page |
      | '/user'     | GET         | Get a single user by supplying an ID |
      | '/user'     | POST        | Create a new user by supplying the email address |
      | '/user'     | PUT         | Update a single user's data by supplying the user ID and email address |
      | '/user'     | DELETE      | Delete a single user by supplying the users ID |
      | '/users'    | GET         | Get the list of all created users |
      | '/auth/register'     | POST         | Register a new admin. |
      | '/auth/login'     | POST         | Login a registered admin to get an access token. |
      | '/auth/me'     | GET         | Get a logged in admins data. |
      | '/auth/me'     | PUT         | Update a logged in admins data. |
      | '/auth/me'     | DELETE      | Delete a logged in admins data. |
      | '/auth/admins'     | GET         | Get all logged in admins data. |

  3. **Logging**

      The application logs to the standard output as well as to AWS OpnSearch using AWS Firehose. Both logging options use custom loggers.

  4. **Security**

      The application uses JSON Web Tokens to authorize access to protected routes. The passwords are also encrypted.

 #### 2. Project Management

   1. **Coding standards** </br>

      The application had to adhere to the following coding standards:
      1. Variable names
      2. Function names
      3. Test driven development
      4. Individual modules need 60% coverage and an overall coverage of 60%.
      5. CI/CD pipeline has to pass before deployments.
      6. Commit messages format has to be adhered to.
      7. Only push code to github using development branches.
      8. Releases have to be tagged.
      9. Use pre-commit to run code quality checks
      10. Use comitizen to format commit messages

   2. **Application development process management** </br>

      The project uses JIRA for management.

 #### 3. Development Workflow

 The application uses atleast 5 branches:

  1. Features branch used to develop new features.
  2. Development branch used to hold the most upto date features that are yet to be deployed.
  3. Staging branch holds the code that is currently being tested for production.
  4. The release branch holds all the assets used when creating a release.
  5. The production branch holds the code for the currently deployed application.

The development workflow follows the following steps:

  1. A feature branch is created for the development of a new feature.
  2. The code is then pushed to GitHub, triggering the feature-development-workflow.yml workflow. If all the tests pass, the feature is reviewde and merged into the development branch.
  3. The code in the development branch is then deployed to the development environment. If the deployment is succesful, the development branch is merged into the staging branch.
  4. This triggers the staging workflow. If all the tests are succesful, this branch is reviewed and deployed to a staging environment.
  5. For creatinga release, the staging branch is merged into the release branch. This happens when a tag is pushed to GitHub.
  6. Once a release is created, the release branch is merged into the production branch, which is deployed into production.

The workflows require a couple of secrets to work:

      ```sh
        FLASK_APP=api/__init__.py
        FLASK_ENV=development

        SECRET_KEY=supersecretkey

        POSTGRES_HOST=<YOUR-IP-ADDRESS>
        POSTGRES_DB=lyle
        POSTGRES_PORT=5432
        POSTGRES_USER=postgres
        POSTGRES_PASSWORD=lyle

        MAIL_HOST=<YOUR-MAIL-HOST>
        MAIL_PORT=<YOUR-MAIL-PORT>
        MAIL_USERNAME=<YOUR-USER-NAME>
        MAIL_PASSWORD=<YOUR-PASSWORD>

        FIREHOSE_DELIVERY_STREAM=flask-logging-firehose-stream

        AWS_KEY=<YOUR-AWS-KEY>
        AWS_SECRET=<YOUR-AWS-SECRET>
        AWS_REGION=<YOUR-AWS-REGION>

        HOST_IP=<AWS-EC2-STATIC-IP>
        AWS_PRIVATE_KEY=<AWS-PRIVATE-KEY>
        APP_DIR=/home/user/repo-template
        USER_NAME=user
        USER_PASSWORD=userpassword
        SERVICE_NAME=gunicorn
      ```

The workflows also require the followingenvironments to work:

  1. Test
  2. Staging
  3. Development
  4. Production

And within each environment, create a secret that indicates the environment type i.e

  1. Test -> ```FLASK_ENV=test```
  2. Staging -> ```FLASK_ENV=stage```
  3. Development -> ```FLASK_ENV=development```
  4. Production -> ```FLASK_ENV=production```

## Deployment

The deployemt process for this application can be divided into two groups:

 * Initial Deployment
 * Incremental deployment

The initial deployment describes the first dployment to the AWS EC2 instance. The process involves the following steps:

 1. **Set up a container registry on ECR**

      Head on over to AWS and set up a container registry using ECR.

 2. **Push the python container to ECR**

      To push the created container image to ECR, you need to tag it, then sign into your account then push it:

      1. Log into ECR

        ```sh
        aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/xxxxx
        ```

      2. Build the image

        ```sh
        make build
        ```

      3. Tag the image

        ```sh
        docker tag repo-template-ecs:latest public.ecr.aws/xxxxxxxx/repo-template-ecs:latest
        ```

      3. Pushto ECR registry

        ```sh
        docker push public.ecr.aws/xxxxxxxxx/repo-template-ecs:latest
        ```

 3. **Set up an ECS Cluster using Fargate**

      Set up an ECS cluster that uses Fargate

 4. **Set up a Task Definition for PostgreSQL database**

      Set up a task for PostgreSQL and make sure to note the database secrets such as the database name, port, user e.t.c. You can create a custom image and upload it to an ECR repo or use the image that comes from docker. You can use AWS S3 to store the .env file with the secrets.

 5. **Create a Service for the Postgres Database Task**

      This service ensures that we always have a task running and never lose connection to our task. Make sure to enable service detection so that the flask app easily connects t this service.

 6. **Create a target group.**

      Create a target group that wil be use by the load balancer to route the traffic to our python service.

 7. **Set up an Application Load balancer**

      The load balancer will direct the HTTP and HTTPS traffic to our Python Service through the created target group.

 8. **Create the application Task Definition**

      Use the docker image that you pushed to ECR to create th task definition. You can also upload the .env file to an S3 bucket and use i within your task definition.

 9. **Create the application Service**

      Use the task defination above to create a service fr the flask app.

 10. **Create the application Service**

      Create the deployment pipeline. This involves setting up a build project that buils the image and pushes it to the ecr registry and also a deployment job that deploys the latest changes.

  11. **Setting up Logging**

      This involves creating a FirehoseDeliveryStream as well as AWS OpenSearch domain.

      Once the application is up and running, you can view the logs by heading over to the OpenSearch dashboard. Here is a video showing some logs:

      ![](resources/videos/logging.gif)

The incremental deployment describes the process of deploying new changes to the already deployed application. It involves the following steps:

 1. Merging the new feature code into the development branch.
 2. This triggers the AWS code pipeline
 3. Codebuild builds the image and pushes it to the ecr repo thatt we created.
 4. Codedeploy pulls the latest image from ecr and gradually updates each task in the serice we created.

Here is the buildspec file:

```sh
    version: 0.2

    phases:
      pre_build:
        commands:
          - echo Logging in to Amazon ECR...
          - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com

      build:
        commands:
          - echo Build started on `date`
          - echo Building the Docker image...
          - docker build -t $IMAGE_REPO_NAME:$IMAGE_TAG .
          - docker tag $IMAGE_REPO_NAME:$IMAGE_TAG $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:$IMAGE_TAG
      post_build:
        commands:
          - echo Build completed on `date`
          - echo Pushing the Docker image...
          - docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:$IMAGE_TAG
          - printf '[{"name":"ecs-container","imageUri":"%s"}]' $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:$IMAGE_TAG > imagedefinitions.json
          - cat imagedefinitions.json

    artifacts:
        files: imagedefinitions.json
```

 12. **Create a hosted zone using Route53**

      Purchase a domain name from a service such as namecheap, then use that domain name to create a hosted zone on AWS using Route53.

 13. **Create an SSL Certificate for your domain**

      Use AWS Certificate manager to generate an SSL certificate for your newly created domain.

 14. **Create a record that points your application load balancer to this domain**

      To use this domain with your application, you need to:

      1. Set up a static IP for your application load balancer using the AWS static IP service.
      2. Create an A record that points to that static IP
      3. Create a listener on your ALB for HTTPS traffic.

## Releases

## v0.1.0 (2022-07-18)

### Feat

- creating the next release.
- updates the project badges.
- creates the initial layout.

## v0.0.1 (2022-07-15)

## Contribution

1. Fork it https://github.com/twyle/repo-template/fork
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Developer

Lyle Okoth – [@lylethedesigner](https://twitter.com/lylethedesigner) on twitter </br>

[lyle okoth](https://medium.com/@lyle-okoth) on medium </br>

My email is lyceokoth@gmail.com </br>

Here is my [GitHub Profile](https://github.com/twyle/)

You can also find me on [LinkedIN](https://www.linkedin.com/feed/)

## License

Distributed under the MIT license. See ``LICENSE`` for more information.
