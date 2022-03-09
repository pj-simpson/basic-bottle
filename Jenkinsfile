pipeline {
  agent {
    dockerfile { filename 'Dockerfile' }
  }
  stages {
    stage('build and test') {
      steps {
        sh 'pytest'
      }
    }
  }
}