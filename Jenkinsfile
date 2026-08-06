pipeline {

    agent any

    stages {

        stage('Clone Information') {

            steps {

                echo "Repository cloned successfully."

                echo "Workspace: ${env.WORKSPACE}"

            }

        }

        stage('Python Version') {

            steps {

                sh 'python3 --version'

                sh 'pip3 --version'

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

                echo "Flask verified successfully."

            }

        }

    }

    post {

        success {

            echo "Pipeline completed successfully."

        }

        failure {

            echo "Pipeline failed."

        }

        always {

            echo "Build Finished."

        }

    }

}
