FROM jenkins/jenkins:lts-jdk11

COPY --from=docker usr/local/bin/docker /usr/local/bin/docker

COPY images/ images/

ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false

USER root

RUN apt-get update && \
    apt-get -qy full-upgrade && \
    apt-get install -qy curl && \
    curl -sSL https://get.docker.com/ | sh

ENV ADMIN_PASSWORD=test 


COPY ./jenkins/jenkins.yml /var/jenkins_home/jenkins.yml
COPY ./jenkins/job_dsl.groovy /var/job_dsl.groovy
COPY ./jenkins/getLanguage.sh /var/getLanguage.sh

ENV CASC_JENKINS_CONFIG=/var/jenkins_home/jenkins.yml


COPY ./plugins.txt /usr/share/jenkins/plugins.txt

RUN jenkins-plugin-cli -f /usr/share/jenkins/plugins.txt