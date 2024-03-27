pipeline {
    agent any
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                zsh 'docker build -t my-django-app .'
                echo 'Image build'
            }
        }
    }
}