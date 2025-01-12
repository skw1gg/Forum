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
                bat 'docker build -t forum-app -f Dockerfile .'
            }
        }

        stage('Run Tests') {
            steps {
                withEnv(["PYTHONPATH=${WORKSPACE}"]) {
                    bat '''
                    powershell -Command "if (!(Test-Path reports)) { New-Item -ItemType Directory -Path reports }"
                    pytest tests/ --junitxml=reports/test-results.xml
                    '''
                }
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
            junit '**/reports/test-results.xml'
        }
    }
}
