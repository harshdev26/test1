pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/harshdev26/test1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t enterprise-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name enterprise-container enterprise-app'
            }
        }
    }
}