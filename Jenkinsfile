pipeline {

    agent any

    stages {

        stage('Clone Repository') {
            steps {
                echo "Repository cloned successfully."
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Verify Flask') {
            steps {
                sh 'python3 -c "import flask; print(flask.__version__)"'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app:v1 .'
            }
        }

        stage('Tag Docker Image') {
            steps {
                sh 'docker tag flask-app:v1 esha93/flask-app:v1'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push esha93/flask-app:v1'
            }
        }

        stage('Deploy to EC2') {
            steps {
                sh '''
ssh -o StrictHostKeyChecking=no ubuntu@54.173.179.56 "
docker pull esha93/flask-app:v1 &&
docker stop flask-container || true &&
docker rm flask-container || true &&
docker run -d --name flask-container -p 5000:5000 esha93/flask-app:v1
"
'''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
ssh -o StrictHostKeyChecking=no ubuntu@54.173.179.56 "docker ps"
'''
            }
        }

    }

    post {

        success {
            echo "====================================="
            echo "Pipeline Completed Successfully!"
            echo "Application deployed to EC2."
            echo "====================================="
        }

        failure {
            echo "====================================="
            echo "Pipeline Failed."
            echo "====================================="
        }

        always {
            echo "CI/CD Pipeline Finished."
        }
    }

}
