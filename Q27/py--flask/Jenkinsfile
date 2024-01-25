pipeline {
    agent any
    stages {
        stage('Clone Stage') {
            steps {
                echo 'Clone Stage'
                git branch: 'main', credentialsId: 'git-pat', url: 'https://github.com/ankitr-c/py-flask.git'
            }
        }
        stage('Build Stage') {
            steps {
                echo 'Build Stage'
                script {
                    ver = readFile('version').trim()
                    sh "docker build -t ${ver} ."
                }
            }
        }

        stage('Artifact Push Stage') {
            steps {
                echo 'Artifact Push Stage'
                script {
                    withCredentials([file(credentialsId: 'service_acc', variable: 'service_acc')]) {
                        sh "docker login -u _json_key --password-stdin https://asia-south1-docker.pkg.dev < \$service_acc"
                        sh "docker push ${ver}"
                    }
                }
            }
        }
    }
}
