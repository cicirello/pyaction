# Copyright (c) 2020-2022 Vincent A. Cicirello
# https://www.cicirello.org
# Source repository: https://github.com/cicirello/pyaction
# Source licensed under the MIT License: https://github.com/cicirello/pyaction/blob/master/LICENSE

# Base image is a Python 3 Slim image
FROM python:3.10.7-slim

LABEL maintainer="development@cicirello.org" \
    org.opencontainers.image.description="A base Docker image for Github Actions implemented in Python" \
    org.opencontainers.image.authors="Vincent A Cicirello, development@cicirello.org, https://www.cicirello.org/" \
    org.opencontainers.image.source="https://github.com/cicirello/pyaction" \
    org.opencontainers.image.title="pyaction" 

# Install git and the GitHub CLI (gh), and their dependencies.
# Note that curl and gpg are installed here because they are
# required for the installation of gh.
RUN true \
    && apt-get update && apt-get install -y \
       curl \
       gpg \
       git \
    && curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    && apt-get update && apt-get install -y gh \
    && rm -rf /var/lib/apt/lists/* \
    && true

## BELOW VERSION WILL DOWNLOAD GH FROM RELEASES
## && t="/tmp/gh-$$.deb" && curl -sSLo "$t" "https://github.com$(curl -sSL "https://github.com/cli/cli/releases/latest" | grep -Po "(?<=href=\")/cli/cli/releases/download/[^\"]*$(dpkg --print-architecture)[.]deb(?=\")")" && apt-get install -y "$t" && rm "$t" \
## END RELEASES VERSION
