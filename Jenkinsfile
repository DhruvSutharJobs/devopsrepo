pipeline {
    agent any
    tools{
        docker 'docker'
    }

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