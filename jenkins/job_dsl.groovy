#!/usr/bin/env groovy

folder("Whanos_base_img") {
    displayName("Whanos_base_img")
}
folder("Projects") {
    displayName("Projects")
}

freeStyleJob("Whanos_base_img/whanos-c") {
    steps {
        shell('docker build -t whanos-c - < /images/c/Dockerfile.base')
        shell('docker tag whanos-c localhost:5000/whanos-c')
        shell('docker push localhost:5000/whanos-c')
        shell('docker pull localhost:5000/whanos-c')
        shell('docker rmi whanos-c')
    }

    triggers {
        upstream('Build all base images')
    }
}

freeStyleJob("Whanos_base_img/whanos-java") {
    steps {
        shell('docker build -t whanos-java - < /images/java/Dockerfile.base')
        shell('docker tag whanos-java localhost:5000/whanos-java')
        shell('docker push localhost:5000/whanos-java')
        shell('docker pull localhost:5000/whanos-java')
        shell('docker rmi whanos-java')
    }

    triggers {
        upstream('Build all base images')
    }
}

freeStyleJob("Whanos_base_img/whanos-javascript") {
    steps {
        shell('docker build -t whanos-javascript - < /images/javascript/Dockerfile.base')
        shell('docker tag whanos-javascript localhost:5000/whanos-javascript')
        shell('docker push localhost:5000/whanos-javascript')
        shell('docker pull localhost:5000/whanos-javascript')
        shell('docker rmi whanos-javascript')
    }

    triggers {
        upstream('Build all base images')
    }
}

freeStyleJob("Whanos_base_img/whanos-befunge") {
    steps {
        shell('docker build -t whanos-befunge - < /images/befunge/Dockerfile.base')
        shell('docker tag whanos-befunge localhost:5000/whanos-befunge')
        shell('docker push localhost:5000/whanos-befunge')
        shell('docker pull localhost:5000/whanos-befunge')
        shell('docker rmi whanos-befunge')
    }

    triggers {
        upstream('Build all base images')
    }
}

freeStyleJob("Whanos_base_img/whanos-python") {
    steps {
        shell('docker build -t whanos-python - < /images/python/Dockerfile.base')
        shell('docker tag whanos-python localhost:5000/whanos-python')
        shell('docker push localhost:5000/whanos-python')
        shell('docker pull localhost:5000/whanos-python')
        shell('docker rmi whanos-python')
    }

    triggers {
        upstream('Build all base images')
    }
}

freeStyleJob("Build all base images") {}

freeStyleJob("link-project") {
    parameters {
        stringParam('GIT_REPOSITORY_URL', '', 'Git URL of the repository to link')
        stringParam('JOB_LABEL', '', 'Display name for the job')
    }

    steps {
        dsl {
            text('''
        freeStyleJob(\"Projects/$JOB_LABEL\") {
            scm {
                github(\"$GIT_REPOSITORY_URL\")
            }
            triggers {
                cron(\'* * * * *\')
            }
            steps {
                shell(\"/var/jenkins_home/whanos.sh $JOB_LABEL\")
            }
            wrappers {
                preBuildCleanup()
            }
        }
            ''')
        }
    }
}