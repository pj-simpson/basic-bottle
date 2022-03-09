pipeline {
  agent { docker { image 'python:3.8-alpine' } }
  stages {
    stage('build') {
      steps {
        sh '/usr/local/bin/python3 -m pip install -r requirements.txt --user'
      }
    }
    stage('test') {
      steps {
        sh 'pytest'
      }
    }
  }
}