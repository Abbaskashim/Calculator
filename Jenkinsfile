pipeline {
    agent any
    stages {
        stage('Clone Code') {
            steps {
                git 'git@github.com:Abbaskashim/Calculator.git'
            }
        }
        stage('Build Image') {
            steps {
                sh 'docker build -t abbaskashim/jenkins-demo1:latest .'
            }
        }
        stage('Push Image') {
            steps {
                sh '''
                docker push abbaskashim/jenkins-demo1
                '''
            }
        }
    }
    post {
        success {
            mail to: 'netmirrortp@gmail.com',
                 subject: 'Pipeline Success',
                 body: 'Docker image pushed successfully'
        }
    }
}
