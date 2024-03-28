pipeline {
    agent any
    enviroment {
        AWS_ACCOUNT_ID = '211125505548'
        AWS_DEFAULT_REGION = 'ap-south-1'
        IMAGE_REPO_NAME = 'jenkin-demo'
        IMAGE_TAG = 'latest'
        REPOSITORY_URI = '${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}'
    }
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Logging into AWS ECR') {
            steps {
                script {
                sh "aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"
                }
                 
            }
        }
        stage('Cloning Git') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/DhruvSutharJobs/devopsrepo.git']])
            }
        }
        stage('Building image') {
            steps{
                script {
                    dockerImage = docker.build "${IMAGE_REPO_NAME}:${IMAGE_TAG}"
                }       
            }
        }
        stage('Pushing to ECR') {
            steps{  
                script {
                        sh "docker tag ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:$IMAGE_TAG"
                        sh "docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:${IMAGE_TAG}"
                }
            }
        }   
    }
}