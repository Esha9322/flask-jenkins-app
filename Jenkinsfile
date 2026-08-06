pipeline {

    agent any

    environment {
        IMAGE_NAME = "flask-app"
        IMAGE_TAG  = "v1"
        CONTAINER_NAME = "flask-container"
    }

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
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }

        stage('Remove Old Container') {
            steps {
                sh '''
                docker stop ${CONTAINER_NAME} || true
                docker rm ${CONTAINER_NAME} || true
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                docker run -d \
                --name ${CONTAINER_NAME} \
                -p 5000:5000 \
                ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }

        stage('Verify Running Container') {
            steps {
                sh 'docker ps'
            }
        }

    }

    post {

        success {
            echo "Application deployed successfully using Docker."
        }

        failure {
            echo "Pipeline Failed."
        }

        always {
            echo "Pipeline Finished."
        }
    }

}
