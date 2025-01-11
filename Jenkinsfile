pipeline {
    agent any

    environment {
        IMAGE_NAME = 'forum-app' // Название Docker-образа
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/skw1gg/Forum'
            }
        }

        stage('Check Docker Installation') {
            steps {
                sh 'docker --version'
                sh 'docker-compose --version'
            }
        }

        stage('Clean Up') {
            steps {
                sh 'docker-compose down || true'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests inside Docker...'
                sh 'docker-compose run --rm web pytest --maxfail=1 --disable-warnings'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        always {
            sh 'docker-compose down'
        }
    }
}
