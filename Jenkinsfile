pipeline {
    agent any
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                sh 'docker build -t my-django-app .'
                echo 'Image build'
            }
        }
    }
}