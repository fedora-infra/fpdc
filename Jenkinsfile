pipeline {
    agent { docker { image 'fedora:28' } }
    stages {
        stage('setup') {
            steps {
                sh 'pip3 install -r requirements-dev.txt'
            }
        }

        stage('unit tests') {
            steps {
                sh 'tox -e py36'
            }
        }

        stage('lint') {
            steps {
                sh 'tox -e lint'
            }
        }

        stage('format') {
            steps {
                sh 'tox -e format'
            }
        }

        stage('django-migrations') {
            steps {
                sh 'tox -e django-migrations'
            }
        }

        stage('licenses') {
            steps {
                sh 'tox -e lisenses'
            }
        }
    }
}
