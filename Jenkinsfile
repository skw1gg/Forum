pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'mydockerhub'
        DOCKER_IMAGE = 'forum-app'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/skw1gg/Forum.git', credentialsId: 'git-credentials-id'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker-compose down'
                    bat 'docker-compose build'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    bat 'docker-compose up -d'
                    bat 'docker exec python-web pytest tests/'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    bat 'docker-compose up -d --remove-orphans'
                }
            }
        }

    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
            junit 'reports/test-results.xml'
        }

        failure {
            echo "Pipeline failed!"
        }

        success {
            echo "Pipeline succeeded!"
        }
    }
}
