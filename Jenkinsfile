pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                sh '''
                  rm -rf Calculator
                  git clone https://github.com/Abbaskashim/Calculator.git
                '''
            }
        }

        stage('Build Image') {
            steps {
                sh '''
                  cd Calculator
                  docker build -t abbaskashim/pipeline-docker-ci:latest .
                '''
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
             subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
             body: """
Hello Team,

The Jenkins pipeline executed successfully.

Job Details:
------------------------------------
Job Name       : ${env.JOB_NAME}
Build Number   : ${env.BUILD_NUMBER}
Build Status   : SUCCESS
Build URL      : ${env.BUILD_URL}
Executed On    : ${env.NODE_NAME}
Workspace Path : ${env.WORKSPACE}

Docker Image:
------------------------------------
Image Name     : abbaskashim/pipeline-docker-ci:latest
Registry       : Docker Hub

Regards,
Jenkins CI/CD
"""
    }
}
        }
    }
}


