pipeline {
  agent { docker { image 'python:3.8-alpine' } }
  stages {
    stage('build') {
      steps {
        sh """
        apt-get install python3-pip && \
        pip3 install virtualenv && \
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