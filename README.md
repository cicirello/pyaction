# pyaction
A base Docker image for Github Actions implemented in Python

[![Docker Image Version (latest by date)](https://img.shields.io/docker/v/cicirello/pyaction?label=Docker%20Hub&logo=docker)](https://hub.docker.com/r/cicirello/pyaction)
[![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/cicirello/pyaction?logo=docker)](https://hub.docker.com/r/cicirello/pyaction)
[![Docker Pulls](https://img.shields.io/docker/pulls/cicirello/pyaction?logo=docker)](https://hub.docker.com/r/cicirello/pyaction)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/cicirello/pyaction?logo=github)](https://github.com/cicirello/pyaction/releases)
[![build](https://github.com/cicirello/pyaction/workflows/build/badge.svg)](https://github.com/cicirello/pyaction/actions?query=workflow%3Abuild)
[![GitHub](https://img.shields.io/github/license/cicirello/pyaction)](https://github.com/cicirello/pyaction/blob/master/LICENSE)

## Summary

This Docker image is designed to support implementing Github Actions 
with Python. As of version 4.0.0., it starts with 
the [official python docker image](https://hub.docker.com/_/python) as the base,
which is a Debian OS. It specifically uses python:3-slim to keep the image size 
down for faster loading of Github Actions that use pyaction. On top of the 
base, we've installed [curl](https://curl.se/), 
[gpg](https://gnupg.org/), [git](https://git-scm.com/), and the 
[GitHub CLI](https://cli.github.com/). We added curl and gpg because they
are needed to install the GitHub CLI, and they may come in handy anyway 
(especially curl) when implementing a GitHub Action.

Note: Up through pyaction:3.14.0, we previously used Alpine Linux. However,
the GitHub CLI isn't currently supported on Alpine, which is why we have
switched the base image.

## Multiplatform Image

__Version 4.0.0 and Newer__: pyaction supports the following 
platforms:
* linux/386
* linux/amd64
* linux/arm/v7
* linux/arm64

__Version 3.14.0 and Earlier__: earlier releases supported the
above as well as the following (these are not supported by the GitHub CLI
at the present time):
* linux/arm/v6
* linux/ppc64le
* linux/s390x 

## Source Repository and Builds

The [source repository](https://github.com/cicirello/pyaction) is 
maintained on GitHub. The images are built on Github and pushed 
to [Docker Hub](https://hub.docker.com/r/cicirello/pyaction), as 
well as the 
[Github Container Registry](https://github.com/cicirello?ecosystem=container&tab=packages) 
using Github Actions.

We have twice monthly, automated builds so that we can pick up any
updates to the base image, such as Python updates, as well as any updates
to the GitHub CLI, etc.

## Docker Tags and Versioning Scheme

We use [Semantic Versioning](https://semver.org/) for our tags.
[Semantic Versioning](https://semver.org/) uses version numbers 
of the form: MAJOR.MINOR.PATCH, where differences in 
MAJOR correspond to incompatible changes, differences in MINOR 
correspond to introduction of backwards compatible new functionality, 
and PATCH corresponds to backwards compatible bug fixes.

Each image pushed to Docker Hub and the Github Container Registry is tagged as follows:
* The tag `latest` indicates, well, the latest image.
* Tags of the form MAJOR.MINOR.PATCH (e.g., 4.0.0).
* Tags of the form MAJOR.MINOR (e.g., 4.0).
* Tags of the form MAJOR (e.g., 4).

## Installation and Usage

The pre-built image is hosted on both Docker Hub and the Github 
Container Registry. You can use it in the following ways.

### Docker Pull Command

Pull the latest image from Docker Hub with the following (replace `latest` with 
a specific version number if you prefer):

```
docker pull cicirello/pyaction:latest
```

Pull from the Github Container Registry with:

```
docker pull ghcr.io/cicirello/pyaction:latest
```


### Use as a base image in a Dockerfile

Use as a base image in a Dockerfile (replace `latest` with 
a specific version number if you prefer):

```Dockerfile
FROM cicirello/pyaction:latest

# The rest of your Dockerfile would go here.
```

Or you can use as a base image (via the Github Container Registry) with:

```Dockerfile
FROM ghcr.io/cicirello/pyaction:latest

# The rest of your Dockerfile would go here.
```


## License

### Source Code License
The source code, including the Dockerfile and anything
else within the [Github repository for pyaction](https://github.com/cicirello/pyaction), 
is licensed under the
[MIT License](https://github.com/cicirello/pyaction/blob/master/LICENSE).

### Image Licenses
As with all pre-built Docker images, the image itself (once built, or obtained from
Docker Hub or the Github Container Registry) contains software that is covered by a
variety of licenses. See the license information for the 
[python docker image](https://hub.docker.com/_/python),
the [license for git](https://git-scm.com/), 
the [GitHub CLI](https://github.com/cli/cli/blob/trunk/LICENSE),
and the [license for Python](https://docs.python.org/3/license.html).  

If you build and distribute an image containing your software, 
using pyaction as the base image, it
is your responsibility to follow the licenses of all of the
software contained within the image.  
