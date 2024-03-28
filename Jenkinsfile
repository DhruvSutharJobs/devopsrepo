pipeline {
    agent any
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('build docker image'){
            steps{
                script{
                    sh 'docker build -t my-django-app .'
                }
            }
        }
    }
}