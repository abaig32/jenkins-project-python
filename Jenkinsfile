pipeline {
  agent any
  tools {
    git 'git'
  }
  stages {
    stage("MirzaBaig-BuildDockerImage") {
      steps {
        script {
          sh 'docker build -t mirzabaig42324/jenkins-python-app .'
        }
      }
    }

    stage("MirzaBaig-LoginToDockerHub") {
      steps {
        script {
          withCredentials([string(credentialsId: 'dockerhubpwd', variable: 'dockerhubpwd')]) {
            sh 'docker login -u mirzabaig42324 -p {dockerhubpwd}'
          }
        }
      }
    }

    stage("MirzaBaig-PushImageToDocker") {
      steps {
        sh 'docker push mirzabaig42324/jenkins-python-app'
      }
    }
  }
}
