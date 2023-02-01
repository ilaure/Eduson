pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        build 'Build'
        echo 'Test'
      }
    }

    stage('smoke tests') {
      steps {
        sh 'echo "hello world"'
      }
    }

    stage('api tests') {
      steps {
        sh 'echo "hello world"'
      }
    }

    stage('ui tests') {
      steps {
        sh 'echo "hello world"'
      }
    }

    stage('release') {
      steps {
        sh 'echo "hello world"'
      }
    }

  }
}