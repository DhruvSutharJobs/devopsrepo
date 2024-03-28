pipeline {
    agent any
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('build docker image'){
            script{
                sh 'sudo -A docker build -t my-django-app .'
            }
        }
    }
}