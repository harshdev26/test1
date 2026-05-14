pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/harshdev26/test1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t enterprise-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run -d -p 5000:5000 --name enterprise-container enterprise-app'
            }
        }
    }
}