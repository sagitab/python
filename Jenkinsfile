pipeline {
    agent any
    
    environment {
        KEY = credentials('key')  // Reference the credentials ID
    }

    triggers {
        pollSCM('* * * * *') // Poll SCM every minute
    }

    stages {
        stage('Clean') {
            steps {
                sh '''
                rm -rf python
                '''
            }
        }
        stage('Clone Code') {
            steps {
                echo 'Clone Code Stage: Cloning repository...'
                sh '''
                git clone https://github.com/sagitab/python.git
                cd python
                '''
            }
        }
        stage('Build') {
            steps {
                echo 'Build Stage: Building the project...' 
            }
        }
        stage('Test') {
            steps {
                echo 'Test Stage: Running tests...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploy Stage: Deploying application...'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
    }
}
