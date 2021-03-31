# MqttService

This project contains source code and supporting files for a serverless application using **FastApi** that you can deploy with the SAM CLI.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

Mangum is used as an adapter for ASGI applications for AWS Lambda functions to handle API Gateway requests and responses.

## Setup
Install requirements

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Testing the application locally

```bash
uvicorn app:main.app --reload
```

## Deploy to AWS

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

```bash
pip install -r requirements.txt
sam --build 
sam --deploy 
```

## Deploy via Github Actions

Github Actions will deploy application to AWS Lambda on push to master branch. Configure github secrets with these environment variables to allow configuration of AWS CLI during deployment.

- AWS_SECRET_KEY
- AWS_SECRET_ACCESS_KEY

## Deploy via Travis CI

Travis CI will build application via **Docker** and deploy to AWS Lambda on push to master branch. Configure the corresponding repository in Travis CI console with these environment variables to allow configuration of AWS CLI during deployment.

- AWS_SECRET_KEY
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION

## Cleanup

To delete the resouces used in the application.

```bash
aws cloudformation delete-stack --stack-name <stackName>
```

