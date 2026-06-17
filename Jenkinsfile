pipeline {
agent any

environment {
    APP_NAME = "wheeler4u"
    IMAGE_NAME = "wheeler4u:v1"
}

stages {

    stage('Checkout') {
        steps {
            git branch: 'main',
                url: 'https://github.com/anil280902/wheeler4u.git'
        }
    }

    stage('Build Docker Image') {
        steps {
            sh '''
            docker build --no-cache -t ${IMAGE_NAME} .
            '''
        }
    }

    stage('Stop Old Container') {
        steps {
            sh '''
            docker stop ${APP_NAME} || true
            docker rm ${APP_NAME} || true
            '''
        }
    }

    stage('Run Container') {
        steps {
            sh '''
            docker run -d \
            --name ${APP_NAME} \
            -p 8000:8000 \
            ${IMAGE_NAME}
            '''
        }
    }

    stage('Verify') {
        steps {
            sh '''
            docker ps
            docker logs ${APP_NAME} --tail 20
            '''
        }
    }
}

post {
    success {
        echo 'Deployment completed   successfully'
    }

    failure {
        echo 'Deployment failed'
    }
}


}
