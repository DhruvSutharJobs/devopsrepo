pipeline {
    agent any
    stages {
        stage('Initialize'){
        def dockerHome = tool 'myDocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
    }
        stage('Hello') {
            steps {
                echo 'Hello World'
                sh 'docker build -t my-django-app .'
                echo 'Image build'
            }
        }
    }
}