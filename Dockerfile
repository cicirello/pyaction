# Copyright (c) 2020 Vincent A. Cicirello
# https://www.cicirello.org
# Source repository: https://github.com/cicirello/pyaction
# Source licensed under the MIT License: https://github.com/cicirello/pyaction/blob/master/LICENSE
FROM alpine:3.13.3
LABEL maintainer="development@cicirello.org" \
    org.opencontainers.image.description="A base Docker image for Github Actions implemented in Python" \
    org.opencontainers.image.authors="Vincent A Cicirello, development@cicirello.org, https://www.cicirello.org/" \
    org.opencontainers.image.source="https://github.com/cicirello/pyaction" \
    org.opencontainers.image.title="pyaction" 
RUN apk update && apk add \
    git \
    python3 \
    && rm -rf /var/cache/apk/*
