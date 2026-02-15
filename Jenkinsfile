pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                sh 'git clone https://github.com/Abbaskashim/Calculator.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t abbaskashim/pipeline-docker-ci:latest .'
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                      echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                      docker push abbaskashim/pipeline-docker-ci:latest
                    '''
                }
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

