pipeline {
    agent any
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                sh 'sudo -A docker build -t my-django-app .'
                echo 'Image build'
            }
        }
    }
}