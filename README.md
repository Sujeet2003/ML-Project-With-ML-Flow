# ML-Project-With-ML-Flow

## Workflow of this project
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update entity
5. Update configuration manager in src config
6. Update components
7. Update pipeline
8. Update main.py
9. Update app.py


## How to run the project
1. Clone the repository: 
    - https://github.com/Sujeet2003/ML-Project-With-ML-Flow.git

2. Create an `environemt` and `activate` it

3. Install the `requirements`
    - pip install -r requirements.txt

4. Run the `app.py` file as:
    - python app.py

5. Open up you at `local host` or `port`

## DagsHub Tracking
[dagshub] (https://dagshub.com/)
    - MLFLOW_TRACKING_URI = https://dagshub.com/Sujeet2003/ML-Project-With-ML-Flow.mlflow
    - MLFLOW_TRACKING_USERNAME = Sujeet2003
    - MLFLOW_TRACKING_PASSWORD = 64c0a69eb84c6b0b4a56e46d0044dd34370fd8eb

    - for `Mac`:
        -- export MLFLOW_TRACKING_URI="https://dagshub.com/Sujeet2003/ML-Project-With-ML-Flow.mlflow"
        -- export MLFLOW_TRACKING_USERNAME="Sujeet2003"
        -- export MLFLOW_TRACKING_PASSWORD="64c0a69eb84c6b0b4a56e46d0044dd34370fd8eb"
    
    - for `Windows`:
        -- set MLFLOW_TRACKING_URI="https://dagshub.com/Sujeet2003/ML-Project-With-ML-Flow.mlflow"
        -- set MLFLOW_TRACKING_USERNAME="Sujeet2003"
        -- set MLFLOW_TRACKING_PASSWORD="64c0a69eb84c6b0b4a56e46d0044dd34370fd8eb"


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model


