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
                // Указываем PYTHONPATH для поиска модуля forum_app
                withEnv(["PYTHONPATH=${WORKSPACE}\\python"]) {
                    bat '''
                    mkdir reports
                    pytest python/tests/ --junitxml=reports/test-results.xml
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
            // Архивация логов и отчетов
            archiveArtifacts artifacts: '**/logs/*.log', allowEmptyArchive: true
            junit '**/reports/test-results.xml'
        }
        failure {
            // Отключите, если SMTP не настроен
            // mail to: 'your-email@example.com',
            //      subject: "Build failed: ${env.JOB_NAME} - ${env.BUILD_NUMBER}",
            //      body: "Check Jenkins for details."
        }
    }
}
