
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out by Jenkins.'
            }
        }

        stage('Check Python') {
            steps {
                bat '"C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" --version'
            }
        }

        stage('Run Automated Tests') {
            steps {
                bat '"C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m unittest -v test_html.py'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All HTML form tests passed!'
        }
        failure {
            echo 'FAILURE: Please check the Console Output.'
        }
    }
}
