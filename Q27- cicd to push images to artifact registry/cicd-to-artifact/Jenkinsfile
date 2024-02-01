pipeline {
    agent any
    stages {
        stage('Clone Stage') {
            steps {
                echo 'Clone Stage'
                git branch: 'main', url: 'https://github.com/ankitr-c/cicd-to-artifact.git'
            }
        }
        stage('Build Stage') {
            steps {
                echo 'Build Stage'
                script {
                    ver = readFile('version').trim()
                    sh "docker buildx build -t ${ver} ."
                }
            }
        }

        stage('Artifact Push Stage') {
            steps {
                echo 'Artifact Push Stage'
                script {
                    withCredentials([file(credentialsId: 'service_acc', variable: 'service_acc')]) {
                        sh "docker login -u _json_key --password-stdin https://us-docker.pkg.dev < \$service_acc"
                        sh "docker push ${ver}"
                    }
                }
            }
        }
    }
}
