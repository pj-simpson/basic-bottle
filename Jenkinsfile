pipeline {
  agent { docker { image 'python:3.8-alpine' } }
  stages {
    stage('build') {
      steps {
        sh """
        virtualenv jenkinsbuild -p python3 && \
        source jenkinsbuild/bin/activate && \
        python3 -m pip install -r requirements.txt
        """
      }
    }
    stage('test') {
      steps {
        sh 'pytest'
      }
    }
  }
}