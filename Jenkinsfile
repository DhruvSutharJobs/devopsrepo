pipeline {
    agent any
    stages {
    //     stage('Initialize'){
    //     def dockerHome = tool 'my_docker'
    //     env.PATH = "${dockerHome}/bin:${env.PATH}"

        stage('Hello') {
            steps {
                sh '${WORKSPACE}/jenkins/pipeline/update-jenkins-plugins-ppln/update-plugins.sh'
                echo 'Hello World'
                sh 'docker build -t my-django-app .'
                echo 'Image build'
            }
        }
    }
}