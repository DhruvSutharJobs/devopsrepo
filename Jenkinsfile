pipeline {
    agent any
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
            steps {
                sh 'docker build -t my-django-app .'
            }
            steps {
                echo 'Image build'
            }
        }
    }
}