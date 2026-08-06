pipeline {

    agent any

    environment {
        IMAGE_NAME = "flask-app"
        IMAGE_TAG = "v1"
        CONTAINER_NAME = "flask-container"
        DOCKER_REPO = "esha93/flask-app"
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
                echo "Building Docker Image..."
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }

        stage('Tag Docker Image') {
            steps {
                echo "Tagging Docker Image..."
                sh 'docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${DOCKER_REPO}:${IMAGE_TAG}'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "Pushing Docker Image to Docker Hub..."
                sh 'docker push ${DOCKER_REPO}:${IMAGE_TAG}'
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
            echo "===================================="
            echo "Pipeline Executed Successfully!"
            echo "Docker Image pushed to Docker Hub."
            echo "Flask Application is Running."
            echo "===================================="
        }

        failure {
            echo "===================================="
            echo "Pipeline Failed!"
            echo "Check the Jenkins Console Output."
            echo "===================================="
        }

        always {
            echo "Pipeline Finished."
        }
    }
}
