pipeline {
    agent {
        lable 'main-host'
    }
    stages {
    //     stage('Initialize'){
    //     def dockerHome = tool 'my_docker'
    //     env.PATH = "${dockerHome}/bin:${env.PATH}"

        stage('Hello') {
            steps {
                echo 'Hello World'
                sh 'docker build -t my-django-app .'
                echo 'Image build'
            }
        }
    }
}