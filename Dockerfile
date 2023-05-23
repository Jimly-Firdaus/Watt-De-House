FROM ubuntu:latest

RUN apt-get update && apt-get install -y curl git

RUN curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | bash && \
    apt-get install -y gitlab-runner


ENV GITLAB_URL=https://gitlab.informatika.org/
ENV REGISTRATION_TOKEN=GR1348941oy7A2edurTGqyPqqZ4PZ
ENV DOCKER_IMAGE=alpine:latest
ENV PRIVILEGED=true
ENV RUNNER_NAME=docker-runner

RUN gitlab-runner register \
  --non-interactive \
  --executor "docker" \
  --docker-image $DOCKER_IMAGE \
  --url $GITLAB_URL \
  --registration-token $REGISTRATION_TOKEN \
  --description "watt-de-house-runner" \
  --maintenance-note "No maintenance note" \
  --tag-list $RUNNER_NAME \
  --run-untagged="true" \
  --locked="true" \
  --access-level="not_protected"

RUN sed -i 's/concurrent = 1/concurrent = 5/g' /etc/gitlab-runner/config.toml

CMD ["gitlab-runner", "run"]
