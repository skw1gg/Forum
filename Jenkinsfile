pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'master', url: 'https://github.com/skw1gg/Forum.git', credentialsId: 'git-credentials-id'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t forum-app .'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest tests/'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker-compose up -d'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/logs/*.log', allowEmptyArchive: true
            junit '**/reports/*.xml'
        }
        failure {
            mail to: 'your-email@example.com',
                 subject: "Build failed: ${env.JOB_NAME} - ${env.BUILD_NUMBER}",
                 body: "Check Jenkins for details."
        }
    }
}
